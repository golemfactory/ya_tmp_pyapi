# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE:** This specification is work-in-progress.   # noqa: E501

    The version of the OpenAPI document: 1.6.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_payment.configuration import Configuration


class Invoice(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'invoice_id': 'str',
        'issuer_id': 'str',
        'recipient_id': 'str',
        'payee_addr': 'str',
        'payer_addr': 'str',
        'payment_platform': 'str',
        'timestamp': 'datetime',
        'agreement_id': 'str',
        'activity_ids': 'list[str]',
        'amount': 'str',
        'payment_due_date': 'datetime',
        'status': 'InvoiceStatus'
    }

    attribute_map = {
        'invoice_id': 'invoiceId',
        'issuer_id': 'issuerId',
        'recipient_id': 'recipientId',
        'payee_addr': 'payeeAddr',
        'payer_addr': 'payerAddr',
        'payment_platform': 'paymentPlatform',
        'timestamp': 'timestamp',
        'agreement_id': 'agreementId',
        'activity_ids': 'activityIds',
        'amount': 'amount',
        'payment_due_date': 'paymentDueDate',
        'status': 'status'
    }

    def __init__(self, invoice_id=None, issuer_id=None, recipient_id=None, payee_addr=None, payer_addr=None, payment_platform=None, timestamp=None, agreement_id=None, activity_ids=None, amount=None, payment_due_date=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Invoice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._invoice_id = None
        self._issuer_id = None
        self._recipient_id = None
        self._payee_addr = None
        self._payer_addr = None
        self._payment_platform = None
        self._timestamp = None
        self._agreement_id = None
        self._activity_ids = None
        self._amount = None
        self._payment_due_date = None
        self._status = None
        self.discriminator = None

        self.invoice_id = invoice_id
        self.issuer_id = issuer_id
        self.recipient_id = recipient_id
        self.payee_addr = payee_addr
        self.payer_addr = payer_addr
        self.payment_platform = payment_platform
        self.timestamp = timestamp
        self.agreement_id = agreement_id
        if activity_ids is not None:
            self.activity_ids = activity_ids
        self.amount = amount
        self.payment_due_date = payment_due_date
        self.status = status

    @property
    def invoice_id(self):
        """Gets the invoice_id of this Invoice.  # noqa: E501


        :return: The invoice_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this Invoice.


        :param invoice_id: The invoice_id of this Invoice.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and invoice_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `invoice_id`, must not be `None`"
            )  # noqa: E501

        self._invoice_id = invoice_id

    @property
    def issuer_id(self):
        """Gets the issuer_id of this Invoice.  # noqa: E501


        :return: The issuer_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this Invoice.


        :param issuer_id: The issuer_id of this Invoice.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and issuer_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `issuer_id`, must not be `None`"
            )  # noqa: E501

        self._issuer_id = issuer_id

    @property
    def recipient_id(self):
        """Gets the recipient_id of this Invoice.  # noqa: E501


        :return: The recipient_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this Invoice.


        :param recipient_id: The recipient_id of this Invoice.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and recipient_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `recipient_id`, must not be `None`"
            )  # noqa: E501

        self._recipient_id = recipient_id

    @property
    def payee_addr(self):
        """Gets the payee_addr of this Invoice.  # noqa: E501


        :return: The payee_addr of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payee_addr

    @payee_addr.setter
    def payee_addr(self, payee_addr):
        """Sets the payee_addr of this Invoice.


        :param payee_addr: The payee_addr of this Invoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payee_addr is None:  # noqa: E501
            raise ValueError("Invalid value for `payee_addr`, must not be `None`")  # noqa: E501

        self._payee_addr = payee_addr

    @property
    def payer_addr(self):
        """Gets the payer_addr of this Invoice.  # noqa: E501


        :return: The payer_addr of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payer_addr

    @payer_addr.setter
    def payer_addr(self, payer_addr):
        """Sets the payer_addr of this Invoice.


        :param payer_addr: The payer_addr of this Invoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payer_addr is None:  # noqa: E501
            raise ValueError("Invalid value for `payer_addr`, must not be `None`")  # noqa: E501

        self._payer_addr = payer_addr

    @property
    def payment_platform(self):
        """Gets the payment_platform of this Invoice.  # noqa: E501


        :return: The payment_platform of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_platform

    @payment_platform.setter
    def payment_platform(self, payment_platform):
        """Sets the payment_platform of this Invoice.


        :param payment_platform: The payment_platform of this Invoice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_platform is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_platform`, must not be `None`")  # noqa: E501

        self._payment_platform = payment_platform

    @property
    def timestamp(self):
        """Gets the timestamp of this Invoice.  # noqa: E501


        :return: The timestamp of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Invoice.


        :param timestamp: The timestamp of this Invoice.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and timestamp is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def agreement_id(self):
        """Gets the agreement_id of this Invoice.  # noqa: E501


        :return: The agreement_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, agreement_id):
        """Sets the agreement_id of this Invoice.


        :param agreement_id: The agreement_id of this Invoice.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and agreement_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `agreement_id`, must not be `None`"
            )  # noqa: E501

        self._agreement_id = agreement_id

    @property
    def activity_ids(self):
        """Gets the activity_ids of this Invoice.  # noqa: E501


        :return: The activity_ids of this Invoice.  # noqa: E501
        :rtype: list[str]
        """
        return self._activity_ids

    @activity_ids.setter
    def activity_ids(self, activity_ids):
        """Sets the activity_ids of this Invoice.


        :param activity_ids: The activity_ids of this Invoice.  # noqa: E501
        :type: list[str]
        """

        self._activity_ids = activity_ids

    @property
    def amount(self):
        """Gets the amount of this Invoice.  # noqa: E501


        :return: The amount of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Invoice.


        :param amount: The amount of this Invoice.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def payment_due_date(self):
        """Gets the payment_due_date of this Invoice.  # noqa: E501


        :return: The payment_due_date of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        """Sets the payment_due_date of this Invoice.


        :param payment_due_date: The payment_due_date of this Invoice.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation
            and payment_due_date is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_due_date`, must not be `None`"
            )  # noqa: E501

        self._payment_due_date = payment_due_date

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: InvoiceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: InvoiceStatus
        """
        if (
            self.local_vars_configuration.client_side_validation and status is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `status`, must not be `None`"
            )  # noqa: E501

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Invoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invoice):
            return True

        return self.to_dict() != other.to_dict()