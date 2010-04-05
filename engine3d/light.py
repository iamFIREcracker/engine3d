#!/usr/bin/env python

from __future__ import division

from OpenGL import GL as gl

class Light(object):
  def __init__(self, id, center, ambient, diffuse):
    self.id = eval('gl.GL_LIGHT%d' % id)
    gl.glEnable(self.id)
    self.center = center
    self.ambient = ambient
    self.diffuse = diffuse

  def draw(self):
    gl.glLightfv(self.id, gl.GL_POSITION, self.center)
    gl.glLightfv(self.id, gl.GL_AMBIENT, self.ambient)
    gl.glLightfv(self.id, gl.GL_DIFFUSE, self.diffuse)
