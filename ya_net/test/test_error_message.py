# coding: utf-8

"""
    Yagna Net API

     Yagna Net API   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest
import datetime

import ya_net
from ya_net.models.error_message import ErrorMessage  # noqa: E501
from ya_net.rest import ApiException

class TestErrorMessage(unittest.TestCase):
    """ErrorMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ErrorMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ya_net.models.error_message.ErrorMessage()  # noqa: E501
        if include_optional :
            return ErrorMessage(
                message = '0'
            )
        else :
            return ErrorMessage(
        )

    def testErrorMessage(self):
        """Test ErrorMessage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()