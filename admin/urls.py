# -*- coding: utf-8 -*-
from admin import adminBlueprint
from admin.views import UserInformationView, UserCommodityView, commUpdate

adminBlueprint.add_url_rule(
    "/<int:page>",
    endpoint="admin",
    view_func=UserInformationView,
    methods=["POST", "GET"],
)

adminBlueprint.add_url_rule(
    "/Userinformation/<int:page>",
    endpoint="Userinformation",
    view_func=UserInformationView,
    methods=["POST", "GET"],
)

adminBlueprint.add_url_rule(
    "/UserCommodity/<int:page>",
    endpoint="UserCommodity",
    view_func=UserCommodityView,
    methods=["POST", "GET"],
)

adminBlueprint.add_url_rule(
    rule="/commUpdate",
    endpoint="commUpdate",
    view_func=commUpdate,
    methods=[
        "POST",
    ],
)
