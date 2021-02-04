# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.automation.actions.configuration import Configuration


class ActionFunctionIdentifier(object):
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
    openapi_types = {"function_type": "str", "id": "str"}

    attribute_map = {"function_type": "functionType", "id": "id"}

    def __init__(
        self, function_type=None, id=None, local_vars_configuration=None
    ):  # noqa: E501
        """ActionFunctionIdentifier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._function_type = None
        self._id = None
        self.discriminator = None

        self.function_type = function_type
        if id is not None:
            self.id = id

    @property
    def function_type(self):
        """Gets the function_type of this ActionFunctionIdentifier.  # noqa: E501

        The type of function. This determines when the function will be called.  # noqa: E501

        :return: The function_type of this ActionFunctionIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this ActionFunctionIdentifier.

        The type of function. This determines when the function will be called.  # noqa: E501

        :param function_type: The function_type of this ActionFunctionIdentifier.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and function_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `function_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "PRE_ACTION_EXECUTION",
            "PRE_FETCH_OPTIONS",
            "POST_FETCH_OPTIONS",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and function_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `function_type` ({0}), must be one of {1}".format(  # noqa: E501
                    function_type, allowed_values
                )
            )

        self._function_type = function_type

    @property
    def id(self):
        """Gets the id of this ActionFunctionIdentifier.  # noqa: E501

        The ID qualifier for the function. This is used to specify which input field a function is associated with for `PRE_FETCH_OPTIONS` and `POST_FETCH_OPTIONS` function types.  # noqa: E501

        :return: The id of this ActionFunctionIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionFunctionIdentifier.

        The ID qualifier for the function. This is used to specify which input field a function is associated with for `PRE_FETCH_OPTIONS` and `POST_FETCH_OPTIONS` function types.  # noqa: E501

        :param id: The id of this ActionFunctionIdentifier.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ActionFunctionIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionFunctionIdentifier):
            return True

        return self.to_dict() != other.to_dict()