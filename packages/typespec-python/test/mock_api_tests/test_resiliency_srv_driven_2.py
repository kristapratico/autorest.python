# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from resiliency.servicedriven2 import ServiceDriven2Client

@pytest.fixture
def initial_client():
    with ServiceDriven2Client(api_version="1.0.0") as client:
        yield client

@pytest.fixture
def updated_client():
    with ServiceDriven2Client() as client:
        yield client

def test_added_params(initial_client, updated_client):
    with pytest.raises(ValueError):
        initial_client.get_required(parameter="foo", new_parameter="bar")
    # initial_client.get_required(parameter="foo")
    # updated_client.get_required(parameter="foo")
    # updated_client.get_required(parameter="foo", new_parameter="bar")


def test_added_method(initial_client, updated_client):
    with pytest.raises(ValueError):
        initial_client.get_new_operation()
    # updated_client.get_new_operation()