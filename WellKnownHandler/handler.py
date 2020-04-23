#!/usr/bin/python3
from requests import get
from json import loads
#### Internal constants
_WELL_KNOWN_ENDPOINT = "/.well-known"
_OIDC_ENDPOINT = "/openid-configuration"


### Constants used externally
## Types
TYPE_OIDC = _OIDC_ENDPOINT
# TODO: Add more endpoints, like UMA

## Keys
# OIDC
KEY_OIDC_AUTHORIZATION_ENDPOINT = "authorization_endpoint"
KEY_OIDC_TOKEN_ENDPOINT = "token_endpoint"
KEY_OIDC_USERINFO_ENDPOINT = "userinfo_endpoint"
KEY_OIDC_END_SESSION_ENDPOINT = "end_session_endpoint"
KEY_OIDC_CLIENTINFO_ENDPOINT = "clientinfo_endpoint"
KEY_OIDC_INTROSPECTION_ENDPOINT = "introspection_endpoint"
KEY_OIDC_SUPPORTED_SCOPES = "scopes_supported"

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

        for ep in [_OIDC_ENDPOINT]:
            retrieved = get(sso_url+_WELL_KNOWN_ENDPOINT+ep, verify=secure)
            if retrieved.text:
                self.data[ep] = loads(retrieved.text)
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