#!/usr/bin/env python3
"""
Basic Authenication
"""
import base64
from api.v1.auth.auth import Auth, TypeVar


class BasicAuth(Auth):
    """ inherit from auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """ extract authorization header and do some checks on it
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base = authorization_header.split(' ')
        return base[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """ Decode bru
        """
        if base64_authorization_header is None:
            return None
        if not type(base64_authorization_header) == str:
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = base64.b64decode(baseEncode)
            return baseDecode.decode('utf-8')
        except Exception:
            return None
