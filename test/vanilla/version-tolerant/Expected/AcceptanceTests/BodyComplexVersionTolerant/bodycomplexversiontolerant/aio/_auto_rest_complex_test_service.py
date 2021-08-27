# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import AutoRestComplexTestServiceConfiguration
from .operations import (
    ArrayOperations,
    BasicOperations,
    DictionaryOperations,
    FlattencomplexOperations,
    InheritanceOperations,
    PolymorphicrecursiveOperations,
    PolymorphismOperations,
    PrimitiveOperations,
    ReadonlypropertyOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestComplexTestService:
    """Test Infrastructure for AutoRest.

    :ivar basic: BasicOperations operations
    :vartype basic: bodycomplexversiontolerant.aio.operations.BasicOperations
    :ivar primitive: PrimitiveOperations operations
    :vartype primitive: bodycomplexversiontolerant.aio.operations.PrimitiveOperations
    :ivar array: ArrayOperations operations
    :vartype array: bodycomplexversiontolerant.aio.operations.ArrayOperations
    :ivar dictionary: DictionaryOperations operations
    :vartype dictionary: bodycomplexversiontolerant.aio.operations.DictionaryOperations
    :ivar inheritance: InheritanceOperations operations
    :vartype inheritance: bodycomplexversiontolerant.aio.operations.InheritanceOperations
    :ivar polymorphism: PolymorphismOperations operations
    :vartype polymorphism: bodycomplexversiontolerant.aio.operations.PolymorphismOperations
    :ivar polymorphicrecursive: PolymorphicrecursiveOperations operations
    :vartype polymorphicrecursive:
     bodycomplexversiontolerant.aio.operations.PolymorphicrecursiveOperations
    :ivar readonlyproperty: ReadonlypropertyOperations operations
    :vartype readonlyproperty: bodycomplexversiontolerant.aio.operations.ReadonlypropertyOperations
    :ivar flattencomplex: FlattencomplexOperations operations
    :vartype flattencomplex: bodycomplexversiontolerant.aio.operations.FlattencomplexOperations
    :keyword endpoint: Service URL. Default value is 'http://localhost:3000'.
    :paramtype endpoint: str
    """

    def __init__(self, *, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        self._config = AutoRestComplexTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.basic = BasicOperations(self._client, self._config, self._serialize, self._deserialize)
        self.primitive = PrimitiveOperations(self._client, self._config, self._serialize, self._deserialize)
        self.array = ArrayOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dictionary = DictionaryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inheritance = InheritanceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphism = PolymorphismOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphicrecursive = PolymorphicrecursiveOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.readonlyproperty = ReadonlypropertyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.flattencomplex = FlattencomplexOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestComplexTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)