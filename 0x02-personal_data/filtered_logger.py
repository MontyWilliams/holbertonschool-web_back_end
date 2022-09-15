#!/usr/bin/env python3
""" Obfuscate and return log message
"""
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    """ replace occurrences of certain fields
        the log message passed in will be replaced
        with xxx
    """
    for field in fields:
        message = re.sub(field + '=' + '.+?' + separator,
                         field + '=' + redaction + separator,
                         message)
        
    return(message)
