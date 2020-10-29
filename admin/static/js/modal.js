<!--处理模态框 -->
$(() => {
    let obj_list = $("#userList tr:gt(0)");
    $.each(obj_list, (index, item) => {
        $(item).dblclick(() => {
            $("#openMD").click();
            let current_userID = $($(item).children("td").get(0)).text();
            let current_userName = $($(item).children("td").get(1)).text();
            let current_name = $($(item).children("td").get(2)).text();
            let current_birthDate = $($(item).children("td").get(3)).text();
            let current_telephone = $($(item).children("td").get(4)).text();
            let current_email = $($(item).children("td").get(5)).text();
            let current_status = $($(item).children("td").get(6)).text();
            let current_type = $($(item).children("td").get(7)).text();
            let current_remark = $($(item).children("td").get(8)).text();
            $("#change_userID").val(current_userID);
            $("#change_userName").val(current_userName);
            $("#change_name").val(current_name);
            $("#change_birthDate").val(current_birthDate);
            $("#change_telephone").val(current_telephone);
            $("#change_email").val(current_email);
            $("#change_status").val(current_status);
            $("#change_type").val(current_type);
            $("#change_remark").val(current_remark);
        })
    })
})
