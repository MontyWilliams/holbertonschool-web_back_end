#!/usr/bin/env python3
""" Obfuscate and return log message
"""
import re
from typing import List
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values
        """
        return filter_datum(
            self.fields,
            self.REDACTION, super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Implement a get_logger function that takes no arguments
    and returns a logging.Logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    # Create console handler (ch) set level info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # streamhandler with redacting formatter
    ch.setFormatter(RedactingFormatter)
    # add handler to logger
    logger.addHandler(ch)

    return logger


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
