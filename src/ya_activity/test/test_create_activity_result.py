# coding: utf-8

"""
    Yagna Activity API

     The Activity API can be perceived as controls which a Requestor-side application has to steer the execution of an Activity as specified in an Agreement which has been negotiated via the Market API/Protocol. This defines possible interactions between the Requestor application (via Activity API) and the generic components running on the Provider node, which host the Provider-side application code. The possible interactions imply a logical “execution environment” component, which is the host/container for the “payload” code. The “execution environment” is specified as an ExeUnit, with a generic interface via which a Provider node’s Activity Controller can operate the hosted code. It conforms with capability level 1 of the [Activity API specification] (https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ya_activity
from ya_activity.models.create_activity_result import CreateActivityResult  # noqa: E501
from ya_activity.rest import ApiException

class TestCreateActivityResult(unittest.TestCase):
    """CreateActivityResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateActivityResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ya_activity.models.create_activity_result.CreateActivityResult()  # noqa: E501
        if include_optional :
            return CreateActivityResult(
                activity_id = '0', 
                credentials = ya_activity.models.credentials.Credentials(
                    sgx = ya_activity.models.sgx_credentials.SgxCredentials(
                        enclave_pub_key = '0', 
                        requestor_pub_key = '0', 
                        payload_hash = '0', 
                        ias_report = '0', 
                        ias_sig = '0', ), )
            )
        else :
            return CreateActivityResult(
                activity_id = '0',
        )

    def testCreateActivityResult(self):
        """Test CreateActivityResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()