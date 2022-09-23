#!/usr/bin/env python3
"""
Basic Authenication
"""
import base64
from api.v1.auth.auth import Auth, TypeVar


class BasicAuth(Auth):
    """ inherit from auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ extract authorization header and do some checks on it
        """
        if authorization_header == None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        
        base = authorization_header.split(' ')
        return base[1]
