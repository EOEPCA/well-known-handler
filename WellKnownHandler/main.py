#!/usr/bin/env python3
""" EXAMPLE: """
import requests
from WellKnownHandler import WellKnownHandler, TYPE_OIDC, KEY_OIDC_SUPPORTED_SCOPES
from WellKnownHandler import TYPE_SCIM, KEY_SCIM_VERSION, KEY_SCIM_BULK_ENDPOINT

def main():
    # Replace:
    sso_url = "http://my_sso.com"

    # Initialize
    h = WellKnownHandler(sso_url, secure=False) # USE 'secure=True' IN PRODUCTION, TO CHECK SSL CERTS!
    
    # OIDC!
    print(h.get(TYPE_OIDC, KEY_OIDC_SUPPORTED_SCOPES))
    # Output: ['openid', ... ]

    # Maybe you want to use SCIM?
    print(h.get(TYPE_SCIM, KEY_SCIM_VERSION))
    # Output: '2.0' (or your version)
    print(h.get(TYPE_SCIM, KEY_SCIM_BULK_ENDPOINT))
    # Output: 'https://<domain>/<path>/Bulk'

if __name__ == "__main__":
    main()