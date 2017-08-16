# -*- coding: utf-8 -*-

"""Client library to interact with Geo temporal API v2 and Geostreaming API in Clowder.

 This module provides methods to simplify writing client code
 against the Geostreaming Clowder API and Geo temporal API V2.

"""

# Set default logging handler to avoid "No handler found" warnings.
# See http://docs.python-guide.org/en/latest/writing/logging/
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
