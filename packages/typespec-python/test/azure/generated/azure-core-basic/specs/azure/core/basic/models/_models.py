# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class User(_model_base.Model):
    """Details about a user.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar name: The user's name. Required.
    :vartype name: str
    :ivar orders: The user's order list.
    :vartype orders: list[~specs.azure.core.basic.models.UserOrder]
    :ivar etag: The entity tag for this resource. Required.
    :vartype etag: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    name: str = rest_field()
    """The user's name. Required."""
    orders: Optional[List["_models.UserOrder"]] = rest_field()
    """The user's order list."""
    etag: str = rest_field(visibility=["read"])
    """The entity tag for this resource. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        orders: Optional[List["_models.UserOrder"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UserList(_model_base.Model):
    """UserList.


    :ivar users: Required.
    :vartype users: list[~specs.azure.core.basic.models.User]
    """

    users: List["_models.User"] = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        users: List["_models.User"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UserOrder(_model_base.Model):
    """UserOrder for testing list with expand.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar user_id: The user's id. Required.
    :vartype user_id: int
    :ivar detail: The user's order detail. Required.
    :vartype detail: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    user_id: int = rest_field(name="userId")
    """The user's id. Required."""
    detail: str = rest_field()
    """The user's order detail. Required."""

    @overload
    def __init__(
        self,
        *,
        user_id: int,
        detail: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
