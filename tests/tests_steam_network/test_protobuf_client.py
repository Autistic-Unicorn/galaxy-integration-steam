from base64 import b64encode
from unittest.mock import MagicMock, PropertyMock

import pytest
import websockets
from galaxy.unittest.mock import AsyncMock
from websockets.protocol import State

from steam_network.protocol.protobuf_client import ProtobufClient

ACCOUNT_NAME = "john"
PASSWORD = b"testing123"
ENCIPHERED_PASSWORD = b64encode(PASSWORD)
TWO_FACTOR = "AbCdEf"
TOKEN = "TOKEN"
CELL_ID = 12121212
CELL_ID_ENCODED = b"\xfc\xe8\xe3\x05"
MACHINE_ID = "machine_id"
OS_VALUE = 1
PRIVATE_IP = 1
HOST_NAME = "john pc"
STEAM_ID = 12345664321
STEAM_ID_ENCODED = STEAM_ID.to_bytes(8, "little")  # fixed64 are encoded as I64 in protobuf
PROTOCOL_VERSION = ProtobufClient._MSG_PROTOCOL_VERSION
CLIENT_PACKAGE_VERSION = ProtobufClient._MSG_CLIENT_PACKAGE_VERSION
CLIENT_LANGUAGE = "english"
TWO_FACTOR_TYPE = 'email'
TIMESTAMP = 1672531200  # Sun 1 January 2023 00:00:00 UTC
TIMESTAMP_ENCODED = b"\x80\x9a\xc3\x9d\x06"  # protobuf uses VARINT encoding

@pytest.fixture
def websocket():
    websocket_ = MagicMock()
    websocket_.send = AsyncMock()
    return websocket_


@pytest.fixture
async def client(websocket, mocker):
    protobuf_client = ProtobufClient(websocket)
    mocker.patch(
        "socket.gethostname", return_value=HOST_NAME
    )
    return protobuf_client


@pytest.mark.asyncio
async def test_log_on_token_message(client, websocket, mocker):
    client._get_obfuscated_private_ip = AsyncMock(return_value=PRIVATE_IP)
    mocker.patch("socket.gethostname", new=MagicMock(return_value=HOST_NAME))
    await client.send_log_on_token_message(ACCOUNT_NAME, STEAM_ID, TOKEN, CELL_ID, MACHINE_ID.encode('utf-8'), OS_VALUE)
    msg_to_send = websocket.send.call_args[0][0]
    assert ACCOUNT_NAME.encode("utf-8") in msg_to_send
    assert STEAM_ID_ENCODED in msg_to_send
    assert TOKEN.encode("utf-8") in msg_to_send
    assert CELL_ID_ENCODED in msg_to_send
    assert MACHINE_ID.encode("utf-8") in msg_to_send
    assert OS_VALUE in msg_to_send
    assert PRIVATE_IP in msg_to_send
    assert HOST_NAME.encode("utf-8") in msg_to_send
    assert CLIENT_LANGUAGE.encode("utf-8") in msg_to_send


@pytest.mark.asyncio
async def test_log_on_password_message(client, websocket, mocker):
    mocker.patch("socket.gethostname", new=MagicMock(return_value=HOST_NAME))
    await client.log_on_password(ACCOUNT_NAME, PASSWORD, TIMESTAMP, OS_VALUE)
    msg_to_send = websocket.send.call_args[0][0]
    assert ACCOUNT_NAME.encode("utf-8") in msg_to_send
    assert ENCIPHERED_PASSWORD in msg_to_send
    assert OS_VALUE in msg_to_send
    assert HOST_NAME.encode("utf-8") in msg_to_send
    assert TIMESTAMP_ENCODED in msg_to_send


@pytest.mark.asyncio
@pytest.mark.parametrize("socket_state", [State.CLOSED, State.CONNECTING, State.CLOSING])
async def test_ensure_open_exception(client, socket_state, monkeypatch, mocker):

    mocker.patch('asyncio.shield', AsyncMock(return_value=MagicMock()))
    client = ProtobufClient(websockets.WebSocketCommonProtocol())
    type(client._socket).close_code = PropertyMock(return_value=1)
    type(client._socket).close_reason = PropertyMock(return_value="Close reason")
    client._socket.close_connection_task = MagicMock()
    client._socket.state = socket_state

    with pytest.raises((websockets.ConnectionClosedError, websockets.InvalidState)):
        await client._get_obfuscated_private_ip()
