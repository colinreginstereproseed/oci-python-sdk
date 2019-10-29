# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAddressListDetails(object):
    """
    The data used to update the address list: IP addresses and CIDR notations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAddressListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAddressListDetails.
        :type display_name: str

        :param addresses:
            The value to assign to the addresses property of this UpdateAddressListDetails.
        :type addresses: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAddressListDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAddressListDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'addresses': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'addresses': 'addresses',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._addresses = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAddressListDetails.
        A unique user-friendly name for the address list.


        :return: The display_name of this UpdateAddressListDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAddressListDetails.
        A unique user-friendly name for the address list.


        :param display_name: The display_name of this UpdateAddressListDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def addresses(self):
        """
        Gets the addresses of this UpdateAddressListDetails.
        A list of IP addresses or CIDR notations.


        :return: The addresses of this UpdateAddressListDetails.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this UpdateAddressListDetails.
        A list of IP addresses or CIDR notations.


        :param addresses: The addresses of this UpdateAddressListDetails.
        :type: list[str]
        """
        self._addresses = addresses

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAddressListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAddressListDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAddressListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAddressListDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAddressListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAddressListDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAddressListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAddressListDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
