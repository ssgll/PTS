# -*- coding: utf-8 -*-
from admin import adminBlueprint
from admin.views import UserinformationView, UserCommodityView

adminBlueprint.add_url_rule(
    "/", endpoint="admin", view_func=UserinformationView, methods=["POST", "GET"]
)

adminBlueprint.add_url_rule(
    "/Userinformation", endpoint="Userinformation", view_func=UserinformationView, methods=["POST", "GET"]
)

adminBlueprint.add_url_rule(
    "/UserCommodity/<int:page>", endpoint="UserCommodity", view_func=UserCommodityView, methods=["POST", "GET"]
)
