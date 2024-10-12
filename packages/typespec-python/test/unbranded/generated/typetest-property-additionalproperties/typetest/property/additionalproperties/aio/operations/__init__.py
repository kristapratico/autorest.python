# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import ExtendsUnknownOperations
from ._operations import ExtendsUnknownDerivedOperations
from ._operations import ExtendsUnknownDiscriminatedOperations
from ._operations import IsUnknownOperations
from ._operations import IsUnknownDerivedOperations
from ._operations import IsUnknownDiscriminatedOperations
from ._operations import ExtendsStringOperations
from ._operations import IsStringOperations
from ._operations import SpreadStringOperations
from ._operations import ExtendsFloatOperations
from ._operations import IsFloatOperations
from ._operations import SpreadFloatOperations
from ._operations import ExtendsModelOperations
from ._operations import IsModelOperations
from ._operations import SpreadModelOperations
from ._operations import ExtendsModelArrayOperations
from ._operations import IsModelArrayOperations
from ._operations import SpreadModelArrayOperations
from ._operations import SpreadDifferentStringOperations
from ._operations import SpreadDifferentFloatOperations
from ._operations import SpreadDifferentModelOperations
from ._operations import SpreadDifferentModelArrayOperations
from ._operations import ExtendsDifferentSpreadStringOperations
from ._operations import ExtendsDifferentSpreadFloatOperations
from ._operations import ExtendsDifferentSpreadModelOperations
from ._operations import ExtendsDifferentSpreadModelArrayOperations
from ._operations import MultipleSpreadOperations
from ._operations import SpreadRecordUnionOperations
from ._operations import SpreadRecordDiscriminatedUnionOperations
from ._operations import SpreadRecordNonDiscriminatedUnionOperations
from ._operations import SpreadRecordNonDiscriminatedUnion2Operations
from ._operations import SpreadRecordNonDiscriminatedUnion3Operations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ExtendsUnknownOperations",
    "ExtendsUnknownDerivedOperations",
    "ExtendsUnknownDiscriminatedOperations",
    "IsUnknownOperations",
    "IsUnknownDerivedOperations",
    "IsUnknownDiscriminatedOperations",
    "ExtendsStringOperations",
    "IsStringOperations",
    "SpreadStringOperations",
    "ExtendsFloatOperations",
    "IsFloatOperations",
    "SpreadFloatOperations",
    "ExtendsModelOperations",
    "IsModelOperations",
    "SpreadModelOperations",
    "ExtendsModelArrayOperations",
    "IsModelArrayOperations",
    "SpreadModelArrayOperations",
    "SpreadDifferentStringOperations",
    "SpreadDifferentFloatOperations",
    "SpreadDifferentModelOperations",
    "SpreadDifferentModelArrayOperations",
    "ExtendsDifferentSpreadStringOperations",
    "ExtendsDifferentSpreadFloatOperations",
    "ExtendsDifferentSpreadModelOperations",
    "ExtendsDifferentSpreadModelArrayOperations",
    "MultipleSpreadOperations",
    "SpreadRecordUnionOperations",
    "SpreadRecordDiscriminatedUnionOperations",
    "SpreadRecordNonDiscriminatedUnionOperations",
    "SpreadRecordNonDiscriminatedUnion2Operations",
    "SpreadRecordNonDiscriminatedUnion3Operations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
