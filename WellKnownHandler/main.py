#!/usr/bin/env python3
""" EXAMPLE: """
import requests
from WellKnownHandler import WellKnownHandler, TYPE_OIDC, KEY_OIDC_SUPPORTED_SCOPES

def main():
    # Replace:
    sso_url = "http://my_sso.com"

    h = WellKnownHandler(sso_url)
    # use the lookup directly on requests!
    print(h.get(TYPE_OIDC, KEY_OIDC_SUPPORTED_SCOPES))
    # Output: ['openid', ... ]

if __name__ == "__main__":
    main()