# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BytesProperty(_model_base.Model):
    """Template type for testing models with nullable property. Pass in the type of the property you
    are looking for.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: bytes
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: bytes = rest_field(name="nullableProperty", format="base64")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: bytes,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsByteProperty(_model_base.Model):
    """Model with collection bytes properties.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: list[bytes]
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: List[bytes] = rest_field(name="nullableProperty", format="base64")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: List[bytes],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_model_base.Model):
    """Model with collection models properties.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: list[~typetest.property.nullable.models.InnerModel]
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: List["_models.InnerModel"] = rest_field(name="nullableProperty")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: List["_models.InnerModel"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DatetimeProperty(_model_base.Model):
    """Model with a datetime property.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: ~datetime.datetime
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: datetime.datetime = rest_field(name="nullableProperty", format="rfc3339")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: datetime.datetime,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DurationProperty(_model_base.Model):
    """Model with a duration property.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: ~datetime.timedelta
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: datetime.timedelta = rest_field(name="nullableProperty")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: datetime.timedelta,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerModel(_model_base.Model):
    """Inner model used in collections model property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Inner model property. Required.
    :vartype property: str
    """

    property: str = rest_field()
    """Inner model property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class StringProperty(_model_base.Model):
    """Template type for testing models with nullable property. Pass in the type of the property you
    are looking for.

    All required parameters must be populated in order to send to Azure.

    :ivar required_property: Required property. Required.
    :vartype required_property: str
    :ivar nullable_property: Property. Required.
    :vartype nullable_property: str
    """

    required_property: str = rest_field(name="requiredProperty")
    """Required property. Required."""
    nullable_property: str = rest_field(name="nullableProperty")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: str,
        nullable_property: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
