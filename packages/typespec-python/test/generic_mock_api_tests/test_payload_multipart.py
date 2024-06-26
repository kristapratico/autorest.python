# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Any
from pathlib import Path
import pytest
from payload.multipart import MultiPartClient, models
from payload.multipart._model_base import Model

JPG = Path(__file__).parent / "data/image.jpg"
PNG = Path(__file__).parent / "data/image.png"


@pytest.fixture
def client():
    with MultiPartClient(endpoint="http://localhost:3000") as client:
        yield client


@pytest.mark.parametrize(
    "op_name,model_class,data,file",
    [
        ("basic", models.MultiPartRequest, {"id": "123"}, {"profileImage": JPG}),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG, "picture": PNG},
        ),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG},
        ),
        (
            "json_part",
            models.JsonPartRequest,
            {"address": models.Address(city="X")},
            {"profileImage": JPG},
        ),
        (
            "json_array_parts",
            models.JsonArrayPartsRequest,
            {"previousAddresses": [models.Address(city="Y"), models.Address(city="Z")]},
            {"profileImage": JPG},
        ),
    ],
)
def test_multi_part(client: MultiPartClient, op_name, model_class, data, file):
    op = getattr(client.form_data, op_name)
    # test bytes
    body = {k: open(str(v), "rb").read() for k, v in file.items()}
    body.update(data)
    op(body)
    op(model_class(body))

    # test io
    body = {k: open(str(v), "rb") for k, v in file.items()}
    body.update(data)
    op(body)

    body = {k: open(str(v), "rb") for k, v in file.items()}
    body.update(data)
    with pytest.raises(TypeError):
        # caused by deepcopy when DPG model init
        op(model_class(body))
