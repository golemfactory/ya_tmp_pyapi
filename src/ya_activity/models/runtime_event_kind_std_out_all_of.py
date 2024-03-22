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


class RuntimeEventKindStdOutAllOf(object):
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
        'stdout': 'object'
    }

    attribute_map = {
        'stdout': 'stdout'
    }

    def __init__(self, stdout=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeEventKindStdOutAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stdout = None
        self.discriminator = None

        self.stdout = stdout

    @property
    def stdout(self):
        """Gets the stdout of this RuntimeEventKindStdOutAllOf.  # noqa: E501


        :return: The stdout of this RuntimeEventKindStdOutAllOf.  # noqa: E501
        :rtype: object
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this RuntimeEventKindStdOutAllOf.


        :param stdout: The stdout of this RuntimeEventKindStdOutAllOf.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and stdout is None:  # noqa: E501
            raise ValueError("Invalid value for `stdout`, must not be `None`")  # noqa: E501

        self._stdout = stdout

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
        if not isinstance(other, RuntimeEventKindStdOutAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeEventKindStdOutAllOf):
            return True

        return self.to_dict() != other.to_dict()
