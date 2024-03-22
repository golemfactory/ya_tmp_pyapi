# coding: utf-8

"""
    Yagna Market API

     ## Yagna Market The Yagna Market is a core component of the Yagna Network, which enables computational Offers and Demands circulation. The Market is open for all entities willing to buy computations (Demands) or monetize computational resources (Offers). ## Yagna Market API The Yagna Market API is the entry to the Yagna Market through which Requestors and Providers can publish their Demands and Offers respectively, find matching counterparty, conduct negotiations and make an agreement.  This version of Market API conforms with capability level 1 of the <a href=\"https://docs.google.com/document/d/1Zny_vfgWV-hcsKS7P-Kdr3Fb0dwfl-6T_cYKVQ9mkNg\"> Market API specification</a>.  Market API contains two roles: Requestors and Providers which are symmetrical most of the time (excluding agreement phase).   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_market.configuration import Configuration


class AgreementProposal(object):
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
    openapi_types = {"proposal_id": "str", "valid_to": "datetime"}

    attribute_map = {"proposal_id": "proposalId", "valid_to": "validTo"}

    def __init__(
        self, proposal_id=None, valid_to=None, local_vars_configuration=None
    ):  # noqa: E501
        """AgreementProposal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._proposal_id = None
        self._valid_to = None
        self.discriminator = None

        self.proposal_id = proposal_id
        self.valid_to = valid_to

    @property
    def proposal_id(self):
        """Gets the proposal_id of this AgreementProposal.  # noqa: E501

        id of the proposal to be promoted to the Agreement  # noqa: E501

        :return: The proposal_id of this AgreementProposal.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this AgreementProposal.

        id of the proposal to be promoted to the Agreement  # noqa: E501

        :param proposal_id: The proposal_id of this AgreementProposal.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and proposal_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `proposal_id`, must not be `None`"
            )  # noqa: E501

        self._proposal_id = proposal_id

    @property
    def valid_to(self):
        """Gets the valid_to of this AgreementProposal.  # noqa: E501

        End of validity period.  Agreement needs to be approved, rejected or cancelled before this date; otherwise will expire.   # noqa: E501

        :return: The valid_to of this AgreementProposal.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this AgreementProposal.

        End of validity period.  Agreement needs to be approved, rejected or cancelled before this date; otherwise will expire.   # noqa: E501

        :param valid_to: The valid_to of this AgreementProposal.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and valid_to is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `valid_to`, must not be `None`"
            )  # noqa: E501

        self._valid_to = valid_to

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
        if not isinstance(other, AgreementProposal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgreementProposal):
            return True

        return self.to_dict() != other.to_dict()
