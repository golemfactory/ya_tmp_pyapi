# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE:** This specification is work-in-progress.   # noqa: E501

    The version of the OpenAPI document: 1.6.3
    Generated by: https://openapi-generator.tech
"""


import unittest

import ya_payment
from ya_payment.api.requestor_api import RequestorApi  # noqa: E501
from ya_payment.rest import ApiException


class TestRequestorApi(unittest.TestCase):
    """RequestorApi unit test stubs"""

    def setUp(self):
        self.api = ya_payment.api.requestor_api.RequestorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_debit_note(self):
        """Test case for accept_debit_note

        Accept received Debit Note.  # noqa: E501
        """
        pass

    def test_accept_invoice(self):
        """Test case for accept_invoice

        Accept received Invoice.  # noqa: E501
        """
        pass

    def test_amend_allocation(self):
        """Test case for amend_allocation

        Amend Allocation.  # noqa: E501
        """
        pass

    def test_create_allocation(self):
        """Test case for create_allocation

        Create Allocation.  # noqa: E501
        """
        pass

    def test_get_allocation(self):
        """Test case for get_allocation

        Get Allocation.  # noqa: E501
        """
        pass

    def test_get_allocations(self):
        """Test case for get_allocations

        Get Allocations.  # noqa: E501
        """
        pass

    def test_get_debit_note(self):
        """Test case for get_debit_note

        Get Debit Note.  # noqa: E501
        """
        pass

    def test_get_debit_note_events(self):
        """Test case for get_debit_note_events

        Get Debit Note events.  # noqa: E501
        """
        pass

    def test_get_debit_notes(self):
        """Test case for get_debit_notes

        Get Debit Notes known by this node (either issued by this Provider or received by this Requestor).  # noqa: E501
        """
        pass

    def test_get_demand_decorations(self):
        """Test case for get_demand_decorations

        Obtain Demand elements specific to the given allocations, to be appended to a market Demand.  # noqa: E501
        """
        pass

    def test_get_invoice(self):
        """Test case for get_invoice

        Get Invoice.  # noqa: E501
        """
        pass

    def test_get_invoice_events(self):
        """Test case for get_invoice_events

        Get Invoice events.  # noqa: E501
        """
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        Get Invoices known to this node (either issued by this Provider or received by this Requestor).  # noqa: E501
        """
        pass

    def test_get_payment(self):
        """Test case for get_payment

        Get Payment.  # noqa: E501
        """
        pass

    def test_get_payments(self):
        """Test case for get_payments

        Get Payments.  # noqa: E501
        """
        pass

    def test_get_payments_for_debit_note(self):
        """Test case for get_payments_for_debit_note

        Get Payments for Debit Note.  # noqa: E501
        """
        pass

    def test_get_payments_for_invoice(self):
        """Test case for get_payments_for_invoice

        Get Payments for Invoice.  # noqa: E501
        """
        pass

    def test_get_requestor_accounts(self):
        """Test case for get_requestor_accounts

        Get available accounts for sending payments.  # noqa: E501
        """
        pass

    def test_issue_invoice(self):
        """Test case for issue_invoice

        Issue an Invoice.  # noqa: E501
        """
        pass

    def test_reject_debit_note(self):
        """Test case for reject_debit_note

        Reject received Debit Note.  # noqa: E501
        """
        pass

    def test_reject_invoice(self):
        """Test case for reject_invoice

        Reject received Invoice.  # noqa: E501
        """
        pass

    def test_release_allocation(self):
        """Test case for release_allocation

        Release Allocation.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
