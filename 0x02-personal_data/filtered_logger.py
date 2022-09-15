#!/usr/bin/env python3
""" Obfuscate and return log message
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """ replace occurrences of certain field
        the log message passed in will be replaced
        with xxx
    """
    for field in fields:
        message = re.sub(field + '=' + '.+?' + separator,
                         field + '=' + redaction + separator,
                         message)
    return(message)
