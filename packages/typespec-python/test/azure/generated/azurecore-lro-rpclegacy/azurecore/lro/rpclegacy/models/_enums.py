# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the processing job."""

    NOT_STARTED = "notStarted"
    """The operation is not started."""
    RUNNING = "running"
    """The operation is in progress."""
    SUCCEEDED = "succeeded"
    """The operation has completed successfully."""
    FAILED = "failed"
    """The operation has failed."""
    CANCELED = "canceled"
    """The operation has been canceled by the user."""
    PARTIALLY_COMPLETED = "partiallyCompleted"
    """The operation has partially completed."""
