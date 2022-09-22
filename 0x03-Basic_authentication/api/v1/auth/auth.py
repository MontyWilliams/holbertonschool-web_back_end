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
		return False


	def authorization_header(self, request=None) -> str:
		""" ath header
		"""
		return None


	def current_user(self, request=None) -> TypeVar('User'):
		""" current user
		"""
		return None
	
	