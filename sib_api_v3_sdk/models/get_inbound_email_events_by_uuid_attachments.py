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


class GetInboundEmailEventsByUuidAttachments(object):
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
        'name': 'str',
        'content_type': 'str',
        'content_id': 'str',
        'content_length': 'int'
    }

    attribute_map = {
        'name': 'name',
        'content_type': 'contentType',
        'content_id': 'contentId',
        'content_length': 'contentLength'
    }

    def __init__(self, name=None, content_type=None, content_id=None, content_length=None):  # noqa: E501
        """GetInboundEmailEventsByUuidAttachments - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._content_type = None
        self._content_id = None
        self._content_length = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if content_type is not None:
            self.content_type = content_type
        if content_id is not None:
            self.content_id = content_id
        if content_length is not None:
            self.content_length = content_length

    @property
    def name(self):
        """Gets the name of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501

        filename specified in the Content-Disposition header of the attachment  # noqa: E501

        :return: The name of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetInboundEmailEventsByUuidAttachments.

        filename specified in the Content-Disposition header of the attachment  # noqa: E501

        :param name: The name of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def content_type(self):
        """Gets the content_type of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501

        value of the Content-Type header of the attachment  # noqa: E501

        :return: The content_type of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this GetInboundEmailEventsByUuidAttachments.

        value of the Content-Type header of the attachment  # noqa: E501

        :param content_type: The content_type of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def content_id(self):
        """Gets the content_id of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501

        value of the Content-ID header of the attachment.  # noqa: E501

        :return: The content_id of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this GetInboundEmailEventsByUuidAttachments.

        value of the Content-ID header of the attachment.  # noqa: E501

        :param content_id: The content_id of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :type: str
        """

        self._content_id = content_id

    @property
    def content_length(self):
        """Gets the content_length of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501

        size of the attachment in bytes  # noqa: E501

        :return: The content_length of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this GetInboundEmailEventsByUuidAttachments.

        size of the attachment in bytes  # noqa: E501

        :param content_length: The content_length of this GetInboundEmailEventsByUuidAttachments.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

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
        if issubclass(GetInboundEmailEventsByUuidAttachments, dict):
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
        if not isinstance(other, GetInboundEmailEventsByUuidAttachments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
