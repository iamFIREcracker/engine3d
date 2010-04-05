#!/usr/bin/env python

from __future__ import division

from OpenGL import GL as gl

class Light(object):
  def __init__(self, id, center, ambient, diffuse):
    self.id = id
    self.lid = eval('gl.GL_LIGHT%d' % id) 
    self.center = center
    self.ambient = ambient
    self.diffuse = diffuse

  def draw(self):
    gl.glLightfv(self.lid, gl.GL_POSITION, self.center)

class LightSystem(object):
  def __init__(self):
    self.lights = []

  def add(self, light):
    self.lights.append(light)
    gl.glEnable(light.lid)

  def remove(self, id):
    for item in self.lights:
      if item.id == id:
        gl.glDisable(item.lid)
        break

  def draw(self):
    for item in self.lights:
      item.draw()
