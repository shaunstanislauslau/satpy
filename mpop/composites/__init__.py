#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>
#   David Hoese <david.hoese@ssec.wisc.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Base classes for composite objects.
"""

from mpop.projectable import InfoObject, Projectable
import numpy as np

class CompositeBase(InfoObject):

    def __init__(self, uid, format, prerequisites, default_image_config={},
                 **kwargs):
        # Required info
        kwargs["uid"] = uid
        kwargs["format"] = format
        kwargs["prerequisites"] = []
        for prerequisite in prerequisites.split(","):
            try:
                kwargs["prerequisites"].append(float(prerequisite))
            except ValueError:
                kwargs["prerequisites"].append(prerequisite)
        InfoObject.__init__(self, **kwargs)
        for key, value in default_image_config.iteritems():
            self.info.setdefault(key, value)

    @property
    def prerequisites(self):
        # Semi-backward compatible
        return self.info["prerequisites"]

    def __call__(self, projectables, nonprojectables=None, **info):
        raise NotImplementedError()

class RGBCompositor(CompositeBase):
    def __call__(self, projectables, nonprojectables=None, **info):
        if len(projectables) != 3:
            raise ValueError("Expected 3 projectables, got %d" % (len(projectables),))
        the_data = np.rollaxis(np.ma.dstack([projectable.data for projectable in projectables]), axis=2)
        info = projectables[0].info.copy()
        info.update(projectables[1].info)
        info.update(projectables[2].info)
        info.update(self.info)
        info["mode"] = "RGB"
        return Projectable(data=the_data, **info)

class Overview(RGBCompositor):

    def __call__(self, projectables, *args, **kwargs):
        res = RGBCompositor.__call__(self,
                                     (projectables[0],
                                      projectables[1],
                                      -projectables[2]),
                                     *args, **kwargs)
        res.info.setdefault("stretch", "linear")
        return res
