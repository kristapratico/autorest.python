# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_create_ap_true_request
    from ._request_builders_py3 import build_create_cat_ap_true_request
    from ._request_builders_py3 import build_create_ap_object_request
    from ._request_builders_py3 import build_create_ap_string_request
    from ._request_builders_py3 import build_create_ap_in_properties_request
    from ._request_builders_py3 import build_create_ap_in_properties_with_ap_string_request
except (SyntaxError, ImportError):
    from ._request_builders import build_create_ap_true_request  # type: ignore
    from ._request_builders import build_create_cat_ap_true_request  # type: ignore
    from ._request_builders import build_create_ap_object_request  # type: ignore
    from ._request_builders import build_create_ap_string_request  # type: ignore
    from ._request_builders import build_create_ap_in_properties_request  # type: ignore
    from ._request_builders import build_create_ap_in_properties_with_ap_string_request  # type: ignore

__all__ = [
    "build_create_ap_true_request",
    "build_create_cat_ap_true_request",
    "build_create_ap_object_request",
    "build_create_ap_string_request",
    "build_create_ap_in_properties_request",
    "build_create_ap_in_properties_with_ap_string_request",
]