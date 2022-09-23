#!/usr/bin/env python3
""" Athentification
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentification
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Bad documentation for this task
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ ath header. If request doesn’t contain the header key Authorization, returns None
            Otherwise, return the value of the header request Authorizatio
        """
        if request is  None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None
