"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "collective.backend_addon"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
