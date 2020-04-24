#!/usr/bin/env python3
from WellKnownHandler.handler import WellKnownHandler

from WellKnownHandler.handler import TYPE_OIDC, TYPE_SCIM

# ENDPOINTS
from WellKnownHandler.handler import KEY_OIDC_AUTHORIZATION_ENDPOINT, KEY_OIDC_TOKEN_ENDPOINT, KEY_OIDC_USERINFO_ENDPOINT, KEY_OIDC_END_SESSION_ENDPOINT, KEY_OIDC_CLIENTINFO_ENDPOINT, KEY_OIDC_INTROSPECTION_ENDPOINT

# SCOPES
from WellKnownHandler.handler import KEY_OIDC_SUPPORTED_SCOPES

# SCIM
from WellKnownHandler.handler import KEY_SCIM_VERSION, KEY_SCIM_SUPPORTED_AUTH, KEY_SCIM_USER_ENDPOINT, KEY_SCIM_GROUP_ENDPOINT, KEY_SCIM_BULK_ENDPOINT, KEY_SCIM_SERVICE_PROVIDER_ENDPOINT, KEY_SCIM_RESOURCE_TYPES_ENDPOINT, KEY_SCIM_FIDO_DEVICES_ENDPOINT, KEY_SCIM_SCHEMAS_ENDPOINT