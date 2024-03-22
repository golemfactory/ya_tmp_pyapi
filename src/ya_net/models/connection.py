# coding: utf-8

"""
    Yagna Net API

     Yagna Net API   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_net.configuration import Configuration


class Connection(object):
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
        'protocol': 'int',
        'local_ip': 'str',
        'local_port': 'int',
        'remote_ip': 'str',
        'remote_port': 'int'
    }

    attribute_map = {
        'protocol': 'protocol',
        'local_ip': 'localIp',
        'local_port': 'localPort',
        'remote_ip': 'remoteIp',
        'remote_port': 'remotePort'
    }

    def __init__(self, protocol=None, local_ip=None, local_port=None, remote_ip=None, remote_port=None, local_vars_configuration=None):  # noqa: E501
        """Connection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._protocol = None
        self._local_ip = None
        self._local_port = None
        self._remote_ip = None
        self._remote_port = None
        self.discriminator = None

        self.protocol = protocol
        self.local_ip = local_ip
        self.local_port = local_port
        self.remote_ip = remote_ip
        self.remote_port = remote_port

    @property
    def protocol(self):
        """Gets the protocol of this Connection.  # noqa: E501


        :return: The protocol of this Connection.  # noqa: E501
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Connection.


        :param protocol: The protocol of this Connection.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def local_ip(self):
        """Gets the local_ip of this Connection.  # noqa: E501


        :return: The local_ip of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this Connection.


        :param local_ip: The local_ip of this Connection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and local_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `local_ip`, must not be `None`")  # noqa: E501

        self._local_ip = local_ip

    @property
    def local_port(self):
        """Gets the local_port of this Connection.  # noqa: E501


        :return: The local_port of this Connection.  # noqa: E501
        :rtype: int
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """Sets the local_port of this Connection.


        :param local_port: The local_port of this Connection.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and local_port is None:  # noqa: E501
            raise ValueError("Invalid value for `local_port`, must not be `None`")  # noqa: E501

        self._local_port = local_port

    @property
    def remote_ip(self):
        """Gets the remote_ip of this Connection.  # noqa: E501


        :return: The remote_ip of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this Connection.


        :param remote_ip: The remote_ip of this Connection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and remote_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_ip`, must not be `None`")  # noqa: E501

        self._remote_ip = remote_ip

    @property
    def remote_port(self):
        """Gets the remote_port of this Connection.  # noqa: E501


        :return: The remote_port of this Connection.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this Connection.


        :param remote_port: The remote_port of this Connection.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and remote_port is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_port`, must not be `None`")  # noqa: E501

        self._remote_port = remote_port

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
        if not isinstance(other, Connection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Connection):
            return True

        return self.to_dict() != other.to_dict()