# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Bar
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CustomDomain
from ._models_py3 import Endpoints
from ._models_py3 import Foo
from ._models_py3 import Resource
from ._models_py3 import StorageAccount
from ._models_py3 import StorageAccountCheckNameAvailabilityParameters
from ._models_py3 import StorageAccountCreateParameters
from ._models_py3 import StorageAccountKeys
from ._models_py3 import StorageAccountListResult
from ._models_py3 import StorageAccountRegenerateKeyParameters
from ._models_py3 import StorageAccountUpdateParameters
from ._models_py3 import SubResource
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UsageName

from ._storage_management_client_enums import AccountStatus
from ._storage_management_client_enums import AccountType
from ._storage_management_client_enums import KeyName
from ._storage_management_client_enums import ProvisioningState
from ._storage_management_client_enums import Reason
from ._storage_management_client_enums import UsageUnit
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Bar",
    "CheckNameAvailabilityResult",
    "CustomDomain",
    "Endpoints",
    "Foo",
    "Resource",
    "StorageAccount",
    "StorageAccountCheckNameAvailabilityParameters",
    "StorageAccountCreateParameters",
    "StorageAccountKeys",
    "StorageAccountListResult",
    "StorageAccountRegenerateKeyParameters",
    "StorageAccountUpdateParameters",
    "SubResource",
    "Usage",
    "UsageListResult",
    "UsageName",
    "AccountStatus",
    "AccountType",
    "KeyName",
    "ProvisioningState",
    "Reason",
    "UsageUnit",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
