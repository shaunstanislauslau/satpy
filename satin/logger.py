#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2010.

# SMHI,
# Folkborgsvägen 1,
# Norrköping, 
# Sweden

# Author(s):
 
#   Martin Raspaud <martin.raspaud@smhi.se>

# This file is part of mpop.

# mpop is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# mpop is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# mpop.  If not, see <http://www.gnu.org/licenses/>.

"""Basic logging facility.
"""

import logging

class NullHandler(logging.Handler):
    """Empty handler.
    """
    def emit(self, record):
        """Record a message.
        """
        pass

LOG = logging.getLogger("satin")
LOG.addHandler(NullHandler())
# Enable logging to console

#LOG.setLevel(logging.DEBUG)
#CONSOLE_HANDLER = logging.StreamHandler()
#CONSOLE_HANDLER.setLevel(logging.DEBUG)
#LOG.addHandler(CONSOLE_HANDLER)


