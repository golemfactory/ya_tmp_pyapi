# coding: utf-8

"""
    Yagna Activity API

     The Activity API can be perceived as controls which a Requestor-side application has to steer the execution of an Activity as specified in an Agreement which has been negotiated via the Market API/Protocol. This defines possible interactions between the Requestor application (via Activity API) and the generic components running on the Provider node, which host the Provider-side application code. The possible interactions imply a logical “execution environment” component, which is the host/container for the “payload” code. The “execution environment” is specified as an ExeUnit, with a generic interface via which a Provider node’s Activity Controller can operate the hosted code. It conforms with capability level 1 of the [Activity API specification] (https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from ya_activity.configuration import Configuration


class CommandOutputBinAllOf(object):
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
        '_bin': 'list[file]'
    }

    attribute_map = {
        '_bin': 'bin'
    }

    def __init__(self, _bin=None, local_vars_configuration=None):  # noqa: E501
        """CommandOutputBinAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bin = None
        self.discriminator = None

        self._bin = _bin

    @property
    def bin(self):
        """Gets the _bin of this CommandOutputBinAllOf.  # noqa: E501


        :return: The _bin of this CommandOutputBinAllOf.  # noqa: E501
        :rtype: list[file]
        """
        return self._bin

    @bin.setter
    def bin(self, _bin):
        """Sets the _bin of this CommandOutputBinAllOf.


        :param _bin: The _bin of this CommandOutputBinAllOf.  # noqa: E501
        :type: list[file]
        """
        if self.local_vars_configuration.client_side_validation and _bin is None:  # noqa: E501
            raise ValueError("Invalid value for `bin`, must not be `None`")  # noqa: E501

        self._bin = _bin

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
        if not isinstance(other, CommandOutputBinAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommandOutputBinAllOf):
            return True

        return self.to_dict() != other.to_dict()
