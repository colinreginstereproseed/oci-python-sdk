# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CachingRuleCriteria(object):
    """
    A caching rule criteria condition and value.
    """

    #: A constant which can be used with the condition property of a CachingRuleCriteria.
    #: This constant has a value of "URL_IS"
    CONDITION_URL_IS = "URL_IS"

    #: A constant which can be used with the condition property of a CachingRuleCriteria.
    #: This constant has a value of "URL_STARTS_WITH"
    CONDITION_URL_STARTS_WITH = "URL_STARTS_WITH"

    #: A constant which can be used with the condition property of a CachingRuleCriteria.
    #: This constant has a value of "URL_PART_ENDS_WITH"
    CONDITION_URL_PART_ENDS_WITH = "URL_PART_ENDS_WITH"

    #: A constant which can be used with the condition property of a CachingRuleCriteria.
    #: This constant has a value of "URL_PART_CONTAINS"
    CONDITION_URL_PART_CONTAINS = "URL_PART_CONTAINS"

    def __init__(self, **kwargs):
        """
        Initializes a new CachingRuleCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this CachingRuleCriteria.
            Allowed values for this property are: "URL_IS", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition: str

        :param value:
            The value to assign to the value property of this CachingRuleCriteria.
        :type value: str

        """
        self.swagger_types = {
            'condition': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'condition': 'condition',
            'value': 'value'
        }

        self._condition = None
        self._value = None

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this CachingRuleCriteria.
        The condition of the caching rule criteria.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field.

        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field.

        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.

        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.

        URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&` `?` symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.

        Allowed values for this property are: "URL_IS", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition of this CachingRuleCriteria.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this CachingRuleCriteria.
        The condition of the caching rule criteria.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field.

        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field.

        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.

        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.

        URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&` `?` symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.


        :param condition: The condition of this CachingRuleCriteria.
        :type: str
        """
        allowed_values = ["URL_IS", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS"]
        if not value_allowed_none_or_none_sentinel(condition, allowed_values):
            condition = 'UNKNOWN_ENUM_VALUE'
        self._condition = condition

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CachingRuleCriteria.
        The value of the caching rule criteria.


        :return: The value of this CachingRuleCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CachingRuleCriteria.
        The value of the caching rule criteria.


        :param value: The value of this CachingRuleCriteria.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
