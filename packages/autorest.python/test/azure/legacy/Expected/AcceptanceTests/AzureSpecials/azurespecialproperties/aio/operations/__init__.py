# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._xms_client_request_id_operations import XMsClientRequestIdOperations
from ._subscription_in_credentials_operations import SubscriptionInCredentialsOperations
from ._subscription_in_method_operations import SubscriptionInMethodOperations
from ._api_version_default_operations import ApiVersionDefaultOperations
from ._api_version_local_operations import ApiVersionLocalOperations
from ._skip_url_encoding_operations import SkipUrlEncodingOperations
from ._odata_operations import OdataOperations
from ._header_operations import HeaderOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "XMsClientRequestIdOperations",
    "SubscriptionInCredentialsOperations",
    "SubscriptionInMethodOperations",
    "ApiVersionDefaultOperations",
    "ApiVersionLocalOperations",
    "SkipUrlEncodingOperations",
    "OdataOperations",
    "HeaderOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
