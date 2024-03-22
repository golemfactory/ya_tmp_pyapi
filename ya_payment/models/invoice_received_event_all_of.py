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


class InvoiceReceivedEventAllOf(object):
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
        'invoice_id': 'str'
    }

    attribute_map = {
        'invoice_id': 'invoiceId'
    }

    def __init__(self, invoice_id=None, local_vars_configuration=None):  # noqa: E501
        """InvoiceReceivedEventAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._invoice_id = None
        self.discriminator = None

        if invoice_id is not None:
            self.invoice_id = invoice_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceReceivedEventAllOf.  # noqa: E501


        :return: The invoice_id of this InvoiceReceivedEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceReceivedEventAllOf.


        :param invoice_id: The invoice_id of this InvoiceReceivedEventAllOf.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.openapi_types:
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, InvoiceReceivedEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceReceivedEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
