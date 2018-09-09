# -*- coding: utf-8 -*-
import logging
from actions.basicaction import BasicAction


class LogAction(BasicAction):
    """Action to log a paste to console"""

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def perform(self, paste):
        self.logger.info("New Paste matched: {0}".format(paste))
