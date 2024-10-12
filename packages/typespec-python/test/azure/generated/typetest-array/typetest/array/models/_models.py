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


class InnerModel(_model_base.Model):
    """Array inner model.


    :ivar property: Required string property. Required.
    :vartype property: str
    :ivar children:
    :vartype children: list[~typetest.array.models.InnerModel]
    """

    property: str = rest_field()
    """Required string property. Required."""
    children: Optional[List["_models.InnerModel"]] = rest_field()

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
        children: Optional[List["_models.InnerModel"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
