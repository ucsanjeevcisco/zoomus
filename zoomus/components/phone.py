"""Zoom.us REST API Python Client -- Phone component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class PhoneComponentV2(base.BaseComponent):
    def numbers_list(self, **kwargs):
        return self.get_request("/phone/numbers", params=kwargs)

    def numbers_get(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request(
            "/phone/numbers/{}".format(kwargs.get("id")), params=kwargs
        )

    def call_logs(self, **kwargs):
        """
        Retrieve call logs for an account.

        Scopes: phone:read:admin

        Prerequisite:
        * Business or Enterprise account
        * A Zoom Phone license
        * Account Owner and a  with Zoom Phone Management

        :param page_size: The number of records returned within a single API call,
        default=30, max=300
        :param page_number: The current page number of returned records, default=1
        :param start_time: Start date from which you would like to get the call logs. The start date should be within past six months.
        :param end_time: The end date upto which you would like to get the call logs for.
        The end date should be within past six months.
        :param type: The type of the call logs. The value can be either "all" or "missed".
        :return: request object with json data
        """

        if 'start_date' in kwargs:
            kwargs["from"] = util.date_to_str(kwargs["start_date"])
            del kwargs["start_date"]
        
        if 'end_date' in kwargs:
            kwargs["to"] = util.date_to_str(kwargs["end_date"])
            del kwargs["end_date"]


        return self.get_request("/phone/call_logs", params=kwargs)

    def calling_plans(self, **kwargs):
        return self.get_request("/phone/calling_plans", params=kwargs)

    def users(self, **kwargs):
        return self.get_request("/phone/users", params=kwargs)

    def user_call_logs(self, **kwargs):
        util.require_keys(kwargs, "email")

        if 'start_date' in kwargs:
            kwargs["from"] = util.date_to_str(kwargs["start_date"])
            del kwargs["start_date"]
        
        if 'end_date' in kwargs:
            kwargs["to"] = util.date_to_str(kwargs["end_date"])
            del kwargs["end_date"]

        return self.get_request("/phone/users/{}/call_logs".format(kwargs.get("email")), params=kwargs)