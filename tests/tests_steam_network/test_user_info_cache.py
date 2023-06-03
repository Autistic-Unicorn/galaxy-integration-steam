import pytest

from steam_network.user_info_cache import UserInfoCache

_STEAM_ID = 123
_ACCOUNT_USERNAME = "😋学中文Не́кот"
_PERSONA_NAME = "Ptester"
_TOKEN = "token"

serialized_creds = {
    'steam_id': 'MTIz',
    'refresh_token': 'dG9rZW4=',
    'account_username': '8J+Yi+WtpuS4reaWh9Cd0LXMgdC60L7Rgg==',
    'persona_name': 'UHRlc3Rlcg=='
}


@pytest.mark.asyncio
async def test_credentials_cache_store():
    user_info_cache = UserInfoCache()
    user_info_cache.steam_id = _STEAM_ID
    user_info_cache.account_username = _ACCOUNT_USERNAME
    user_info_cache.persona_name = _PERSONA_NAME
    user_info_cache.refresh_token = _TOKEN

    assert user_info_cache.initialized.is_set()
    assert serialized_creds == user_info_cache.to_dict()


@pytest.mark.asyncio
async def test_credentials_cache_load():
    user_info_cache = UserInfoCache()
    user_info_cache.from_dict(serialized_creds)

    assert user_info_cache.steam_id == _STEAM_ID
    assert user_info_cache.account_username == _ACCOUNT_USERNAME
    assert user_info_cache.persona_name == _PERSONA_NAME
    assert user_info_cache.refresh_token == _TOKEN
