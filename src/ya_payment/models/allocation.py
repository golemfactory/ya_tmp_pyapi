# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE:** This specification is work-in-progress.   # noqa: E501

    The version of the OpenAPI document: 1.6.3
    Generated by: https://openapi-generator.tech
"""


from datetime import datetime, timezone
import pprint
import re  # noqa: F401


from ya_payment.configuration import Configuration



class Allocation(object):
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
        'allocation_id': 'str',
        'address': 'str',
        'payment_platform': 'str',
        'total_amount': 'str',
        'spent_amount': 'str',
        'remaining_amount': 'str',
        'timestamp': 'datetime',
        'timeout': 'datetime',
        'make_deposit': 'bool',
        'deposit': 'Deposit',
    }

    attribute_map = {
        'allocation_id': 'allocationId',
        'address': 'address',
        'payment_platform': 'paymentPlatform',
        'total_amount': 'totalAmount',
        'spent_amount': 'spentAmount',
        'remaining_amount': 'remainingAmount',
        'timestamp': 'timestamp',
        'timeout': 'timeout',
        'make_deposit': 'makeDeposit',
        'deposit': 'deposit',
    }

    def __init__(self, allocation_id=None, address=None, payment_platform=None, total_amount=None, spent_amount=None, remaining_amount=None, timestamp=None, timeout=None, make_deposit=None, local_vars_configuration=None, deposit=None):  # noqa: E501
        """Allocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_id = None
        self._address = None
        self._payment_platform = None
        self._total_amount = None
        self._spent_amount = None
        self._remaining_amount = None
        self._timestamp = None
        self._timeout = None
        self._make_deposit = None
        self.discriminator = None

        self.allocation_id = allocation_id
        if address is not None:
            self.address = address
        if payment_platform is not None:
            self.payment_platform = payment_platform
        self.total_amount = total_amount
        self.spent_amount = spent_amount
        self.remaining_amount = remaining_amount
        if timestamp is not None:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now(timezone.utc)
        if timeout is not None:
            self.timeout = timeout
        self.make_deposit = make_deposit
        self._deposit = None
        self.deposit = deposit

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        self._deposit = deposit

    @property
    def allocation_id(self):
        """Gets the allocation_id of this Allocation.  # noqa: E501


        :return: The allocation_id of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this Allocation.


        :param allocation_id: The allocation_id of this Allocation.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and allocation_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `allocation_id`, must not be `None`"
            )  # noqa: E501

        self._allocation_id = allocation_id

    @property
    def address(self):
        """Gets the address of this Allocation.  # noqa: E501


        :return: The address of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Allocation.


        :param address: The address of this Allocation.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def payment_platform(self):
        """Gets the payment_platform of this Allocation.  # noqa: E501


        :return: The payment_platform of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._payment_platform

    @payment_platform.setter
    def payment_platform(self, payment_platform):
        """Sets the payment_platform of this Allocation.


        :param payment_platform: The payment_platform of this Allocation.  # noqa: E501
        :type: str
        """

        self._payment_platform = payment_platform

    @property
    def total_amount(self):
        """Gets the total_amount of this Allocation.  # noqa: E501


        :return: The total_amount of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Allocation.


        :param total_amount: The total_amount of this Allocation.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and total_amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `total_amount`, must not be `None`"
            )  # noqa: E501

        self._total_amount = total_amount

    @property
    def spent_amount(self):
        """Gets the spent_amount of this Allocation.  # noqa: E501


        :return: The spent_amount of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._spent_amount

    @spent_amount.setter
    def spent_amount(self, spent_amount):
        """Sets the spent_amount of this Allocation.


        :param spent_amount: The spent_amount of this Allocation.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and spent_amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `spent_amount`, must not be `None`"
            )  # noqa: E501

        self._spent_amount = spent_amount

    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this Allocation.  # noqa: E501


        :return: The remaining_amount of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, remaining_amount):
        """Sets the remaining_amount of this Allocation.


        :param remaining_amount: The remaining_amount of this Allocation.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and remaining_amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `remaining_amount`, must not be `None`"
            )  # noqa: E501

        self._remaining_amount = remaining_amount

    @property
    def timestamp(self):
        """Gets the timestamp of this Allocation.  # noqa: E501


        :return: The timestamp of this Allocation.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Allocation.


        :param timestamp: The timestamp of this Allocation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def timeout(self):
        """Gets the timeout of this Allocation.  # noqa: E501


        :return: The timeout of this Allocation.  # noqa: E501
        :rtype: datetime
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Allocation.


        :param timeout: The timeout of this Allocation.  # noqa: E501
        :type: datetime
        """

        self._timeout = timeout

    @property
    def make_deposit(self):
        """Gets the make_deposit of this Allocation.  # noqa: E501


        :return: The make_deposit of this Allocation.  # noqa: E501
        :rtype: bool
        """
        return self._make_deposit

    @make_deposit.setter
    def make_deposit(self, make_deposit):
        """Sets the make_deposit of this Allocation.


        :param make_deposit: The make_deposit of this Allocation.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and make_deposit is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `make_deposit`, must not be `None`"
            )  # noqa: E501

        self._make_deposit = make_deposit

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
        if not isinstance(other, Allocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Allocation):
            return True

        return self.to_dict() != other.to_dict()
