# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import SimpleModelValueOperations
from ._operations import ModelWithSimpleArraysValueOperations
from ._operations import ModelWithArrayOfModelValueOperations
from ._operations import ModelWithOptionalFieldValueOperations
from ._operations import ModelWithAttributesValueOperations
from ._operations import ModelWithUnwrappedArrayValueOperations
from ._operations import ModelWithRenamedArraysValueOperations
from ._operations import ModelWithRenamedFieldsValueOperations
from ._operations import ModelWithEmptyArrayValueOperations
from ._operations import ModelWithTextValueOperations
from ._operations import ModelWithDictionaryValueOperations
from ._operations import ModelWithEncodedNamesValueOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "SimpleModelValueOperations",
    "ModelWithSimpleArraysValueOperations",
    "ModelWithArrayOfModelValueOperations",
    "ModelWithOptionalFieldValueOperations",
    "ModelWithAttributesValueOperations",
    "ModelWithUnwrappedArrayValueOperations",
    "ModelWithRenamedArraysValueOperations",
    "ModelWithRenamedFieldsValueOperations",
    "ModelWithEmptyArrayValueOperations",
    "ModelWithTextValueOperations",
    "ModelWithDictionaryValueOperations",
    "ModelWithEncodedNamesValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
