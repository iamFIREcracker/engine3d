#!/usr/bin/env python

from __future__ import division

from OpenGL import GL as gl

class Light(object):
  def __init__(self, id, center):
    self.lid = getattr(gl, 'GL_LIGHT%d' % id) 
    self.center = center
    
  def draw(self):
    gl.glLightfv(self.lid, gl.GL_POSITION, self.center)

class LightSystem(object):
  def __init__(self):
    self.lights = []
    self._toggle = False
  
  def toggle(self):
    if self._toggle:
      gl.glDisable(gl.GL_LIGHTING)
    else:
      gl.glEnable(gl.GL_LIGHTING)
    self._toggle = not self._toggle

  def add(self, light):
    gl.glEnable(light.lid)
    self.lights.append(light)

  def remove(self, id):
    lid = getattr(gl, 'GL_LIGHT%d' % id) 
    for (i, item) in enumerate(self.lights):
      if item.lid == lid:
        gl.glDisable(item.lid)
        self.lights.pop(i)
        break

  def draw(self):
    for item in self.lights:
      item.draw()
