# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class DifferentSpreadFloatDerived(_model_base.Model):
    """The model extends from a model that spread Record:code:`<float32>` with the different known
    property type.

    All required parameters must be populated in order to send to server.

    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: float
    """

    derived_prop: float = rest_field(name="derivedProp")
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        derived_prop: float,
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


class DifferentSpreadModelArrayDerived(_model_base.Model):
    """The model extends from a model that spread Record<ModelForRecord[]> with the different known
    property type.

    All required parameters must be populated in order to send to server.

    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    derived_prop: List["_models.ModelForRecord"] = rest_field(name="derivedProp")
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        derived_prop: List["_models.ModelForRecord"],
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


class DifferentSpreadModelDerived(_model_base.Model):
    """The model extends from a model that spread Record:code:`<ModelForRecord>` with the different
    known property type.

    All required parameters must be populated in order to send to server.

    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    derived_prop: "_models.ModelForRecord" = rest_field(name="derivedProp")
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        derived_prop: "_models.ModelForRecord",
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


class DifferentSpreadStringDerived(_model_base.Model):
    """The model extends from a model that spread Record:code:`<string>` with the different known
    property type.

    All required parameters must be populated in order to send to server.

    :ivar derived_prop: The index property. Required.
    :vartype derived_prop: str
    """

    derived_prop: str = rest_field(name="derivedProp")
    """The index property. Required."""

    @overload
    def __init__(
        self,
        *,
        derived_prop: str,
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


class ExtendsFloatAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<float32>` type.

    All required parameters must be populated in order to send to server.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field()
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
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


class ExtendsModelAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<ModelForRecord>` type.

    All required parameters must be populated in order to send to server.

    :ivar known_prop: Required.
    :vartype known_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    known_prop: "_models.ModelForRecord" = rest_field(name="knownProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: "_models.ModelForRecord",
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


class ExtendsModelArrayAdditionalProperties(_model_base.Model):
    """The model extends from Record<ModelForRecord[]> type.

    All required parameters must be populated in order to send to server.

    :ivar known_prop: Required.
    :vartype known_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    known_prop: List["_models.ModelForRecord"] = rest_field(name="knownProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: List["_models.ModelForRecord"],
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


class ExtendsStringAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<string>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class ExtendsUnknownAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class ExtendsUnknownAdditionalPropertiesDerived(ExtendsUnknownAdditionalProperties):  # pylint: disable=name-too-long
    """The model extends from a type that extends from Record:code:`<unknown>`.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
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


class ExtendsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):  # pylint: disable=name-too-long
    """The model extends from Record:code:`<unknown>` with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ExtendsUnknownAdditionalPropertiesDiscriminatedDerived

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field()
    """The name property. Required."""
    kind: str = rest_discriminator(name="kind")
    """The discriminator. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        kind: str,
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


class ExtendsUnknownAdditionalPropertiesDiscriminatedDerived(
    ExtendsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):  # pylint: disable=name-too-long
    """The derived discriminated type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, kind="derived", **kwargs)


class IsFloatAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<float32>` type.

    All required parameters must be populated in order to send to server.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field()
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
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


class IsModelAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<ModelForRecord>` type.

    All required parameters must be populated in order to send to server.

    :ivar known_prop: Required.
    :vartype known_prop: ~typetest.property.additionalproperties.models.ModelForRecord
    """

    known_prop: "_models.ModelForRecord" = rest_field(name="knownProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: "_models.ModelForRecord",
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


class IsModelArrayAdditionalProperties(_model_base.Model):
    """The model is from Record<ModelForRecord[]> type.

    All required parameters must be populated in order to send to server.

    :ivar known_prop: Required.
    :vartype known_prop: list[~typetest.property.additionalproperties.models.ModelForRecord]
    """

    known_prop: List["_models.ModelForRecord"] = rest_field(name="knownProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        known_prop: List["_models.ModelForRecord"],
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


class IsStringAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<string>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class IsUnknownAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class IsUnknownAdditionalPropertiesDerived(IsUnknownAdditionalProperties):
    """The model extends from a type that is Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
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


class IsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):  # pylint: disable=name-too-long
    """The model is Record:code:`<unknown>` with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    IsUnknownAdditionalPropertiesDiscriminatedDerived

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field()
    """The name property. Required."""
    kind: str = rest_discriminator(name="kind")
    """The discriminator. Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        kind: str,
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


class IsUnknownAdditionalPropertiesDiscriminatedDerived(
    IsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):  # pylint: disable=name-too-long
    """The derived discriminated type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, kind="derived", **kwargs)


class ModelForRecord(_model_base.Model):
    """model for record.

    All required parameters must be populated in order to send to server.

    :ivar state: The state property. Required.
    :vartype state: str
    """

    state: str = rest_field()
    """The state property. Required."""

    @overload
    def __init__(
        self,
        *,
        state: str,
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


class WidgetData0(_model_base.Model):
    """WidgetData0.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar kind: Required. Default value is "kind0".
    :vartype kind: str
    :ivar foo_prop: Required.
    :vartype foo_prop: str
    """

    kind: Literal["kind0"] = rest_field()
    """Required. Default value is \"kind0\"."""
    foo_prop: str = rest_field(name="fooProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        foo_prop: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind0"] = "kind0"


class WidgetData1(_model_base.Model):
    """WidgetData1.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar kind: Required. Default value is "kind1".
    :vartype kind: str
    :ivar start: Required.
    :vartype start: ~datetime.datetime
    :ivar end:
    :vartype end: ~datetime.datetime
    """

    kind: Literal["kind1"] = rest_field()
    """Required. Default value is \"kind1\"."""
    start: datetime.datetime = rest_field(format="rfc3339")
    """Required."""
    end: Optional[datetime.datetime] = rest_field(format="rfc3339")

    @overload
    def __init__(
        self,
        *,
        start: datetime.datetime,
        end: Optional[datetime.datetime] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind1"] = "kind1"


class WidgetData2(_model_base.Model):
    """WidgetData2.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar kind: Required. Default value is "kind1".
    :vartype kind: str
    :ivar start: Required.
    :vartype start: str
    """

    kind: Literal["kind1"] = rest_field()
    """Required. Default value is \"kind1\"."""
    start: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        start: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["kind1"] = "kind1"
