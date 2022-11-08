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


class GetSmsEventReportEvents(object):
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
        'phone_number': 'str',
        '_date': 'str',
        'message_id': 'str',
        'event': 'str',
        'reason': 'str',
        'reply': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'phone_number': 'phoneNumber',
        '_date': 'date',
        'message_id': 'messageId',
        'event': 'event',
        'reason': 'reason',
        'reply': 'reply',
        'tag': 'tag'
    }

    def __init__(self, phone_number=None, _date=None, message_id=None, event=None, reason=None, reply=None, tag=None):  # noqa: E501
        """GetSmsEventReportEvents - a model defined in Swagger"""  # noqa: E501

        self._phone_number = None
        self.__date = None
        self._message_id = None
        self._event = None
        self._reason = None
        self._reply = None
        self._tag = None
        self.discriminator = None

        if phone_number is not None:
            self.phone_number = phone_number
        if _date is not None:
            self._date = _date
        if message_id is not None:
            self.message_id = message_id
        if event is not None:
            self.event = event
        if reason is not None:
            self.reason = reason
        if reply is not None:
            self.reply = reply
        if tag is not None:
            self.tag = tag

    @property
    def phone_number(self):
        """Gets the phone_number of this GetSmsEventReportEvents.  # noqa: E501

        Phone number which has generated the event  # noqa: E501

        :return: The phone_number of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this GetSmsEventReportEvents.

        Phone number which has generated the event  # noqa: E501

        :param phone_number: The phone_number of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def _date(self):
        """Gets the _date of this GetSmsEventReportEvents.  # noqa: E501

        UTC date-time on which the event has been generated  # noqa: E501

        :return: The _date of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetSmsEventReportEvents.

        UTC date-time on which the event has been generated  # noqa: E501

        :param _date: The _date of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def message_id(self):
        """Gets the message_id of this GetSmsEventReportEvents.  # noqa: E501

        Message ID which generated the event  # noqa: E501

        :return: The message_id of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this GetSmsEventReportEvents.

        Message ID which generated the event  # noqa: E501

        :param message_id: The message_id of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def event(self):
        """Gets the event of this GetSmsEventReportEvents.  # noqa: E501

        Event which occurred  # noqa: E501

        :return: The event of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this GetSmsEventReportEvents.

        Event which occurred  # noqa: E501

        :param event: The event of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """
        allowed_values = ["bounces", "hardBounces", "softBounces", "delivered", "sent", "accepted", "unsubscription", "replies", "blocked"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"  # noqa: E501
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def reason(self):
        """Gets the reason of this GetSmsEventReportEvents.  # noqa: E501

        Reason of bounce (only available if the event is hardbounce or softbounce)  # noqa: E501

        :return: The reason of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetSmsEventReportEvents.

        Reason of bounce (only available if the event is hardbounce or softbounce)  # noqa: E501

        :param reason: The reason of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def reply(self):
        """Gets the reply of this GetSmsEventReportEvents.  # noqa: E501


        :return: The reply of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._reply

    @reply.setter
    def reply(self, reply):
        """Sets the reply of this GetSmsEventReportEvents.


        :param reply: The reply of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self._reply = reply

    @property
    def tag(self):
        """Gets the tag of this GetSmsEventReportEvents.  # noqa: E501

        Tag of the SMS which generated the event  # noqa: E501

        :return: The tag of this GetSmsEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GetSmsEventReportEvents.

        Tag of the SMS which generated the event  # noqa: E501

        :param tag: The tag of this GetSmsEventReportEvents.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if issubclass(GetSmsEventReportEvents, dict):
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
        if not isinstance(other, GetSmsEventReportEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
