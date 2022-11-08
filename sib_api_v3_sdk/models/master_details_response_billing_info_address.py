# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MasterDetailsResponseBillingInfoAddress(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'street_address': 'str',
        'locality': 'str',
        'postal_code': 'str',
        'state_code': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'street_address': 'streetAddress',
        'locality': 'locality',
        'postal_code': 'postalCode',
        'state_code': 'stateCode',
        'country_code': 'countryCode'
    }

    def __init__(self, street_address=None, locality=None, postal_code=None, state_code=None, country_code=None):  # noqa: E501
        """MasterDetailsResponseBillingInfoAddress - a model defined in Swagger"""  # noqa: E501

        self._street_address = None
        self._locality = None
        self._postal_code = None
        self._state_code = None
        self._country_code = None
        self.discriminator = None

        if street_address is not None:
            self.street_address = street_address
        if locality is not None:
            self.locality = locality
        if postal_code is not None:
            self.postal_code = postal_code
        if state_code is not None:
            self.state_code = state_code
        if country_code is not None:
            self.country_code = country_code

    @property
    def street_address(self):
        """Gets the street_address of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501

        Street address  # noqa: E501

        :return: The street_address of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this MasterDetailsResponseBillingInfoAddress.

        Street address  # noqa: E501

        :param street_address: The street_address of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def locality(self):
        """Gets the locality of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501

        Locality  # noqa: E501

        :return: The locality of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this MasterDetailsResponseBillingInfoAddress.

        Locality  # noqa: E501

        :param locality: The locality of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def postal_code(self):
        """Gets the postal_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this MasterDetailsResponseBillingInfoAddress.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_code(self):
        """Gets the state_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501

        State code  # noqa: E501

        :return: The state_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this MasterDetailsResponseBillingInfoAddress.

        State code  # noqa: E501

        :param state_code: The state_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def country_code(self):
        """Gets the country_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501

        Country code  # noqa: E501

        :return: The country_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this MasterDetailsResponseBillingInfoAddress.

        Country code  # noqa: E501

        :param country_code: The country_code of this MasterDetailsResponseBillingInfoAddress.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MasterDetailsResponseBillingInfoAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MasterDetailsResponseBillingInfoAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other