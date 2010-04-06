#!/usr/bin/env python

from __future__ import division

from OpenGL import GL as gl

class Light(object):
  def __init__(self, center):
    self.lid = None
    self.center = center
    
  def enable(self):
    gl.glEnable(self.lid)

  def place(self):
    gl.glLightfv(self.lid, gl.GL_POSITION, self.center)
    print gl.glGetLightfv(self.lid, gl.GL_POSITION)

class LightSystem(object):
  def __init__(self):
    self._lid = 0
    self.lights = []
    self._toggle = False
  
  def toggle(self):
    if self._toggle:
      gl.glDisable(gl.GL_LIGHTING)
    else:
      gl.glEnable(gl.GL_LIGHTING)
    self._toggle = not self._toggle

  def add(self, light):
    light.lid = getattr(gl, 'GL_LIGHT%d' % self._lid) 
    self.lights.append(light)
    self._lid += 1

  def enable(self):
    for item in self.lights:
      item.enable()

  def place(self):
    for item in self.lights:
      item.place()
