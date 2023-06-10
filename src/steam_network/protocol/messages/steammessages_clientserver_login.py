# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_clientserver_login.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from steammessages_base import CMsgIPAddress


@dataclass
class CMsgClientHeartBeat(betterproto.Message):
    send_reply: bool = betterproto.bool_field(1)


@dataclass
class CMsgClientServerTimestampRequest(betterproto.Message):
    client_request_timestamp: int = betterproto.uint64_field(1)


@dataclass
class CMsgClientServerTimestampResponse(betterproto.Message):
    client_request_timestamp: int = betterproto.uint64_field(1)
    server_timestamp_ms: int = betterproto.uint64_field(2)


@dataclass
class CMsgClientSecret(betterproto.Message):
    version: int = betterproto.uint32_field(1)
    appid: int = betterproto.uint32_field(2)
    deviceid: int = betterproto.uint32_field(3)
    nonce: float = betterproto.fixed64_field(4)
    hmac: bytes = betterproto.bytes_field(5)


@dataclass
class CMsgClientHello(betterproto.Message):
    protocol_version: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientLogon(betterproto.Message):
    protocol_version: int = betterproto.uint32_field(1)
    deprecated_obfustucated_private_ip: int = betterproto.uint32_field(2)
    cell_id: int = betterproto.uint32_field(3)
    last_session_id: int = betterproto.uint32_field(4)
    client_package_version: int = betterproto.uint32_field(5)
    client_language: str = betterproto.string_field(6)
    client_os_type: int = betterproto.uint32_field(7)
    should_remember_password: bool = betterproto.bool_field(8)
    wine_version: str = betterproto.string_field(9)
    deprecated_10: int = betterproto.uint32_field(10)
    obfuscated_private_ip: "CMsgIPAddress" = betterproto.message_field(11)
    deprecated_public_ip: int = betterproto.uint32_field(20)
    qos_level: int = betterproto.uint32_field(21)
    client_supplied_steam_id: float = betterproto.fixed64_field(22)
    public_ip: "CMsgIPAddress" = betterproto.message_field(23)
    machine_id: bytes = betterproto.bytes_field(30)
    launcher_type: int = betterproto.uint32_field(31)
    ui_mode: int = betterproto.uint32_field(32)
    chat_mode: int = betterproto.uint32_field(33)
    steam2_auth_ticket: bytes = betterproto.bytes_field(41)
    email_address: str = betterproto.string_field(42)
    rtime32_account_creation: float = betterproto.fixed32_field(43)
    account_name: str = betterproto.string_field(50)
    password: str = betterproto.string_field(51)
    game_server_token: str = betterproto.string_field(52)
    login_key: str = betterproto.string_field(60)
    was_converted_deprecated_msg: bool = betterproto.bool_field(70)
    anon_user_target_account_name: str = betterproto.string_field(80)
    resolved_user_steam_id: float = betterproto.fixed64_field(81)
    eresult_sentryfile: int = betterproto.int32_field(82)
    sha_sentryfile: bytes = betterproto.bytes_field(83)
    auth_code: str = betterproto.string_field(84)
    otp_type: int = betterproto.int32_field(85)
    otp_value: int = betterproto.uint32_field(86)
    otp_identifier: str = betterproto.string_field(87)
    steam2_ticket_request: bool = betterproto.bool_field(88)
    sony_psn_ticket: bytes = betterproto.bytes_field(90)
    sony_psn_service_id: str = betterproto.string_field(91)
    create_new_psn_linked_account_if_needed: bool = betterproto.bool_field(92)
    sony_psn_name: str = betterproto.string_field(93)
    game_server_app_id: int = betterproto.int32_field(94)
    steamguard_dont_remember_computer: bool = betterproto.bool_field(95)
    machine_name: str = betterproto.string_field(96)
    machine_name_userchosen: str = betterproto.string_field(97)
    country_override: str = betterproto.string_field(98)
    is_steam_box: bool = betterproto.bool_field(99)
    client_instance_id: int = betterproto.uint64_field(100)
    two_factor_code: str = betterproto.string_field(101)
    supports_rate_limit_response: bool = betterproto.bool_field(102)
    web_logon_nonce: str = betterproto.string_field(103)
    priority_reason: int = betterproto.int32_field(104)
    embedded_client_secret: "CMsgClientSecret" = betterproto.message_field(105)
    disable_partner_autogrants: bool = betterproto.bool_field(106)
    is_steam_deck: bool = betterproto.bool_field(107)
    access_token: str = betterproto.string_field(108)
    is_chrome_os: bool = betterproto.bool_field(109)
    is_tesla: bool = betterproto.bool_field(110)


@dataclass
class CMsgClientLogonResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    legacy_out_of_game_heartbeat_seconds: int = betterproto.int32_field(2)
    heartbeat_seconds: int = betterproto.int32_field(3)
    deprecated_public_ip: int = betterproto.uint32_field(4)
    rtime32_server_time: float = betterproto.fixed32_field(5)
    account_flags: int = betterproto.uint32_field(6)
    cell_id: int = betterproto.uint32_field(7)
    email_domain: str = betterproto.string_field(8)
    steam2_ticket: bytes = betterproto.bytes_field(9)
    eresult_extended: int = betterproto.int32_field(10)
    webapi_authenticate_user_nonce: str = betterproto.string_field(11)
    cell_id_ping_threshold: int = betterproto.uint32_field(12)
    deprecated_use_pics: bool = betterproto.bool_field(13)
    vanity_url: str = betterproto.string_field(14)
    public_ip: "CMsgIPAddress" = betterproto.message_field(15)
    user_country: str = betterproto.string_field(16)
    client_supplied_steamid: float = betterproto.fixed64_field(20)
    ip_country_code: str = betterproto.string_field(21)
    parental_settings: bytes = betterproto.bytes_field(22)
    parental_setting_signature: bytes = betterproto.bytes_field(23)
    count_loginfailures_to_migrate: int = betterproto.int32_field(24)
    count_disconnects_to_migrate: int = betterproto.int32_field(25)
    ogs_data_report_time_window: int = betterproto.int32_field(26)
    client_instance_id: int = betterproto.uint64_field(27)
    force_client_update_check: bool = betterproto.bool_field(28)
    agreement_session_url: str = betterproto.string_field(29)
    token_id: int = betterproto.uint64_field(30)


@dataclass
class CMsgClientRequestWebAPIAuthenticateUserNonce(betterproto.Message):
    token_type: int = betterproto.int32_field(1)


@dataclass
class CMsgClientRequestWebAPIAuthenticateUserNonceResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    webapi_authenticate_user_nonce: str = betterproto.string_field(11)
    token_type: int = betterproto.int32_field(3)


@dataclass
class CMsgClientLogOff(betterproto.Message):
    pass


@dataclass
class CMsgClientLoggedOff(betterproto.Message):
    eresult: int = betterproto.int32_field(1)


@dataclass
class CMsgClientNewLoginKey(betterproto.Message):
    unique_id: int = betterproto.uint32_field(1)
    login_key: str = betterproto.string_field(2)


@dataclass
class CMsgClientNewLoginKeyAccepted(betterproto.Message):
    unique_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgClientAccountInfo(betterproto.Message):
    persona_name: str = betterproto.string_field(1)
    ip_country: str = betterproto.string_field(2)
    count_authed_computers: int = betterproto.int32_field(5)
    account_flags: int = betterproto.uint32_field(7)
    facebook_id: int = betterproto.uint64_field(8)
    facebook_name: str = betterproto.string_field(9)
    steamguard_machine_name_user_chosen: str = betterproto.string_field(15)
    is_phone_verified: bool = betterproto.bool_field(16)
    two_factor_state: int = betterproto.uint32_field(17)
    is_phone_identifying: bool = betterproto.bool_field(18)
    is_phone_needing_reverify: bool = betterproto.bool_field(19)


@dataclass
class CMsgClientChallengeRequest(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CMsgClientChallengeResponse(betterproto.Message):
    challenge: float = betterproto.fixed64_field(1)
