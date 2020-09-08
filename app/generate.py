# -*- coding: UTF-8 -*-
import sys
import time
import logging


class GenerateId(object):
    def __init__(self, datacenter_id=1, worker_id=2):
        # 初始毫秒级时间戳（2014-08-22）
        self.initial_time_stamp = int(
            time.mktime(time.strptime("2014-08-22 00:00:00", "%Y-%m-%d %H:%M:%S"))
            * 1000
        )
        # 机器 ID 所占的位数
        self.worker_id_bits = 5
        # 数据表示 ID 所占的位数
        self.datacenter_id_bits = 5
        # 支持的最大机器 ID，结果是 31（这个位移算法可以很快的计算出几位二进制数所能表示的最大十进制数）
        # 2**5-1 0b11111
        self.max_worker_id = -1 ^ (-1 << self.worker_id_bits)
        # 支持最大标识 ID，结果是 31
        self.max_datacenter_id = -1 ^ (-1 << self.datacenter_id_bits)
        # 序列号 ID所占的位数
        self.sequence_bits = 12
        # 机器 ID 偏移量（12）
        self.workerid_offset = self.sequence_bits
        # 数据中心 ID 偏移量（12 + 5）
        self.datacenterid_offset = self.sequence_bits + self.datacenter_id_bits
        # 时间戳偏移量（12 + 5 + 5）
        self.timestamp_offset = (
            self.sequence_bits + self.datacenter_id_bits + self.worker_id_bits
        )
        # 生成序列的掩码，这里为 4095（0b111111111111 = 0xfff = 4095）
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)

        # 初始化日志
        self.logger = logging.getLogger("snowflake")

        # 数据中心 ID（0 ~ 31）
        if datacenter_id > self.max_datacenter_id or datacenter_id < 0:
            err_msg = "datacenter_id 不能大于 %d 或小于 0" % self.max_worker_id
            self.logger.error(err_msg)
            sys.exit()
        self.datacenter_id = datacenter_id
        # 工作节点 ID（0 ~ 31）
        if worker_id > self.max_worker_id or worker_id < 0:
            err_msg = "worker_id 不能大于 %d 或小于 0" % self.max_worker_id
            self.logger.error(err_msg)
            sys.exit()
        self.worker_id = worker_id
        # 毫秒内序列（0 ~ 4095）
        self.sequence = 0
        # 上次生成 ID 的时间戳
        self.last_timestamp = -1

    def _gen_timestamp(self):
        """
        生成整数毫秒级时间戳
        :return: 整数毫秒级时间戳
        """
        return int(time.time() * 1000)

    def next_id(self):
        """
        获得下一个ID (用同步锁保证线程安全)
        :return: snowflake_id
        """
        timestamp = self._gen_timestamp()
        # 如果当前时间小于上一次 ID 生成的时间戳，说明系统时钟回退过这个时候应当抛出异常
        if timestamp < self.last_timestamp:
            self.logger.error(
                "clock is moving backwards. Rejecting requests until {}".format(
                    self.last_timestamp
                )
            )
        # 如果是同一时间生成的，则进行毫秒内序列
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.sequence_mask
            # sequence 等于 0 说明毫秒内序列已经增长到最大值
            if self.sequence == 0:
                # 阻塞到下一个毫秒,获得新的时间戳
                timestamp = self._til_next_millis(self.last_timestamp)
        else:
            # 时间戳改变，毫秒内序列重置
            self.sequence = 0

        # 上次生成 ID 的时间戳
        self.last_timestamp = timestamp

        # 移位并通过或运算拼到一起组成 64 位的 ID
        new_id = (
            ((timestamp - self.initial_time_stamp) << self.timestamp_offset)
            | (self.datacenter_id << self.datacenterid_offset)
            | (self.worker_id << self.workerid_offset)
            | self.sequence
        )
        return new_id

    def _til_next_millis(self, last_timestamp):
        """
        阻塞到下一个毫秒，直到获得新的时间戳
        :param last_timestamp: 上次生成 ID 的毫秒级时间戳
        :return: 当前毫秒级时间戳
        """
        timestamp = self._gen_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._gen_timestamp()
        return timestamp
