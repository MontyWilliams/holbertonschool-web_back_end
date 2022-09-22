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
		# if not path or not excluded_paths:
		# 	return True
		# if path[-1] != '/':
		# 	path += '/'
		# if path in excluded_paths:
		# 	return False
		return False

	def authorization_header(self, request=None) -> str:
		return None

	def current_user(self, request=None) -> TypeVar('User'):
		return None
	
	