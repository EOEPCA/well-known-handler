#!/usr/bin/python3
from requests import get
from json import loads
#### Internal constants
_WELL_KNOWN_ENDPOINT = "/.well-known"
_OIDC_ENDPOINT = "/openid-configuration"
_SCIM_ENDPOINT = "/scim-configuration"


### Constants used externally
## Types
TYPE_OIDC = _OIDC_ENDPOINT
TYPE_SCIM = _SCIM_ENDPOINT

## Keys
# OIDC
KEY_OIDC_AUTHORIZATION_ENDPOINT = "authorization_endpoint"
KEY_OIDC_TOKEN_ENDPOINT = "token_endpoint"
KEY_OIDC_USERINFO_ENDPOINT = "userinfo_endpoint"
KEY_OIDC_END_SESSION_ENDPOINT = "end_session_endpoint"
KEY_OIDC_CLIENTINFO_ENDPOINT = "clientinfo_endpoint"
KEY_OIDC_INTROSPECTION_ENDPOINT = "introspection_endpoint"
KEY_OIDC_SUPPORTED_SCOPES = "scopes_supported"

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

        for ep in [_OIDC_ENDPOINT, _SCIM_ENDPOINT]:
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