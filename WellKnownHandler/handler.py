#!/usr/bin/python3
from requests import get
from json import loads
#### Internal constants
_WELL_KNOWN_ENDPOINT = "/.well-known"
_OIDC_ENDPOINT = "/openid-configuration"
_SCIM_ENDPOINT = "/scim-configuration"
_UMA_2_ENDPOINT = "/uma2-configuration"

### Constants used externally
## Types
TYPE_OIDC = _OIDC_ENDPOINT
TYPE_SCIM = _SCIM_ENDPOINT
TYPE_UMA_V2 = _UMA_2_ENDPOINT

## Keys
# OIDC
KEY_OIDC_AUTHORIZATION_ENDPOINT = "authorization_endpoint"
KEY_OIDC_TOKEN_ENDPOINT = "token_endpoint"
KEY_OIDC_USERINFO_ENDPOINT = "userinfo_endpoint"
KEY_OIDC_END_SESSION_ENDPOINT = "end_session_endpoint"
KEY_OIDC_CLIENTINFO_ENDPOINT = "clientinfo_endpoint"
KEY_OIDC_INTROSPECTION_ENDPOINT = "introspection_endpoint"
KEY_OIDC_JWKS_ENDPOINT = "jwks_uri"
KEY_OIDC_REGISTRATION_ENDPOINT = "registration_endpoint"
KEY_OIDC_OP_POLICY_ENDPOINT = "op_policy_uri"
KEY_OIDC_OP_TOS_ENDPOINT = "op_tos_uri"
KEY_OIDC_ID_GENERATION_ENDPOINT = "id_generation_endpoint"

KEY_OIDC_SUPPORTED_RESPONSE_TYPES = "response_types_supported"
KEY_OIDC_SUPPORTED_SCOPES = "scopes_supported"
KEY_OIDC_SUPPORTED_GRANT_TYPES = "grant_types_supported"
KEY_OIDC_SUPPORTED_CLAIMS_PARAMETER = "claims_parameter_supported"
KEY_OIDC_SUPPORTED_REQUEST_PARAMETER = "request_parameter_supported"
KEY_OIDC_SUPPORTED_REQUEST_URI_PARAMETER = "request_uri_parameter_supported"
KEY_OIDC_SUPPORTED_SUBJECT_TYPES = "subject_types_supported"
KEY_OIDC_SUPPORTED_USERINFO_SIGNING_ALG_VALUES = "userinfo_signing_alg_values_supported"
KEY_OIDC_SUPPORTED_ID_TOKEN_SIGNING_ALG_VALUES = "id_token_signing_alg_values_supported"
KEY_OIDC_SUPPORTED_USERINFO_ENCRYPTION_ALG_VALUES = "userinfo_encryption_alg_values_supported"
KEY_OIDC_SUPPORTED_USERINFO_ENCRYPTION_ENC_VALUES = "userinfo_encryption_enc_values_supported"
KEY_OIDC_SUPPORTED_ID_TOKEN_ENCRYPTION_ALG_VALUES = "id_token_encryption_alg_values_supported"
KEY_OIDC_SUPPORTED_ID_TOKEN_ENCRYPTION_ENC_VALUES = "id_token_encryption_enc_values_supported"
KEY_OIDC_SUPPORTED_REQUEST_OBJ_SIGNING_ALG_VALUES = "request_object_signing_alg_values_supported"
KEY_OIDC_SUPPORTED_REQUEST_OBJ_ENCRYPTION_ALG_VALUES = "request_object_encryption_alg_values_supported"
KEY_OIDC_SUPPORTED_REQUEST_OBJ_ENCRYPTION_ENC_VALUES = "request_object_encryption_enc_values_supported"
KEY_OIDC_SUPPORTED_AUTH_METHODS_TOKEN_ENDPOINT = "token_endpoint_auth_methods_supported"
KEY_OIDC_SUPPORTED_TOKEN_ENDPOINT_AUTH_SIGNING_ALG_VALUES = "token_endpoint_auth_signing_alg_values_supported"
KEY_OIDC_SUPPORTED_DISPLAY_VALUES = "display_values_supported"
KEY_OIDC_SUPPORTED_CLAIM_TYPES = "claim_types_supported"
KEY_OIDC_SUPPORTED_CLAIMS = "claims_supported"
KEY_OIDC_SUPPORTED_CLAIMS_LOCALES = "claims_locales_supported"
KEY_OIDC_SUPPORTED_ACR_VALUES = "acr_values_supported"
KEY_OIDC_SUPPORTED_UI_LOCALES = "ui_locales_supported"
KEY_OIDC_SUPPORTED_FRONTCHANNEL_LOGOUT = "frontchannel_logout_supported"
KEY_OIDC_SUPPORTED_FRONTCHANNEL_LOGOUT_SESSION = "frontchannel_logout_session_supported"

KEY_OIDC_CHECK_SESSION_IFRAME = "check_session_iframe"
KEY_OIDC_AUTH_LEVEL_MAPPING = "auth_level_mapping"
KEY_OIDC_SERVICE_DOCUMENTATION = "service_documentation"
KEY_OIDC_SCOPE_TO_CLAIMS_MAPPING = "scope_to_claims_mapping"
KEY_OIDC_REQUIRE_REQUEST_URI_REGISTRATION = "require_request_uri_registration"

# SCIM
KEY_SCIM_VERSION = "version"
KEY_SCIM_SUPPORTED_AUTH = "authorization_supported"

KEY_SCIM_USER_ENDPOINT = "user_endpoint"
KEY_SCIM_GROUP_ENDPOINT = "group_endpoint"
KEY_SCIM_BULK_ENDPOINT = "bulk_endpoint"
KEY_SCIM_SERVICE_PROVIDER_ENDPOINT = "service_provider_endpoint"
KEY_SCIM_RESOURCE_TYPES_ENDPOINT = "resource_types_endpoint"
KEY_SCIM_FIDO_DEVICES_ENDPOINT = "fido_devices_endpoint"
KEY_SCIM_SCHEMAS_ENDPOINT = "schemas_endpoint"

# UMA
KEY_UMA_V2_AUTHORIZATION_ENDPOINT = "authorization_endpoint"
KEY_UMA_V2_TOKEN_ENDPOINT = "token_endpoint"
KEY_UMA_V2_REGISTRATION_ENDPOINT = "registration_endpoint"
KEY_UMA_V2_JWKS_ENDPOINT = "jwks_uri"
KEY_UMA_V2_INTROSPECTION_ENDPOINT = "introspection_endpoint"
KEY_UMA_V2_CLAIMS_INTERACTION_ENDPOINT = "claims_interaction_endpoint"
KEY_UMA_V2_PERMISSION_ENDPOINT = "permission_endpoint"
KEY_UMA_V2_RESOURCE_REGISTRATION_ENDPOINT = "resource_registration_endpoint"
KEY_UMA_V2_SCOPE_ENDPOINT = "scope_endpoint"

KEY_UMA_V2_SUPPORTED_RESPONSE_TYPES = "response_types_supported"
KEY_UMA_V2_SUPPORTED_GRANT_TYPES = "grant_types_supported"
KEY_UMA_V2_SUPPORTED_AUTH_METHODS_TOKEN_ENDPOINT = "token_endpoint_auth_methods_supported"
KEY_UMA_V2_SUPPORTED_AUTH_SIGNING_ALG_VALUES_TOKEN_ENDPOINT = "token_endpoint_auth_signing_alg_values_supported"
KEY_UMA_V2_SUPPORTED_UI_LOCALES = "ui_locales_supported"
KEY_UMA_V2_SUPPORTED_CODE_CHALLENGE_METHODS = "code_challenge_methods_supported"
KEY_UMA_V2_SUPPORTED_UMA_PROFILES = "uma_profiles_supported"


class WellKnownHandler:
    """
    Utility class that parses the well-known endpoint and allows easy access using keys and types.
    """
    data = {}

    def __init__(self, sso_url, secure=False):
        """
        Creates a new WellKnownHandler object, querying the sso for information.

        Toggling the "secure" flag will enable SSL certificate checks, which is highly recommended in production environments.
        """
        if not secure:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

        for ep in [_OIDC_ENDPOINT, _SCIM_ENDPOINT, _UMA_2_ENDPOINT]:
            retrieved = get(sso_url+_WELL_KNOWN_ENDPOINT+ep, verify=secure)
            if retrieved.text:
                tmp = loads(retrieved.text)
                # SCIM information comes in an array with a single value, at least in the servers this was tested on
                if ep == _SCIM_ENDPOINT:
                    tmp = tmp[0]

                self.data[ep] = tmp
            else:
                raise Exception("Got no information from SSO. Returned ->" + retrieved.text + "--" + retrieved.reason)

    def get(self, type, key):
        """
        Gets the requested information from the data gathered in well-known.

        Args:
            Type: OIDC, UMA, ... -> Use constants named TYPE_*
            Key: -> Use constants named KEY_<TYPE>_*,
                    or a string if there is no key available for it and you know the field name

        Returns:
            The data requested (string, dict or list), OR None if not found
        """
        try:
            return self.data[type][key]
        except:
            return None