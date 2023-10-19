import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    from importlib_metadata import metadata

from scramp.core import (
    ScramClient,
    ScramException,
    ScramMechanism,
    make_channel_binding,
)

__all__ = [ScramClient, ScramMechanism, ScramException, make_channel_binding]

__version__ = metadata.version("scramp")
