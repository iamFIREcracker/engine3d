#!/usr/bin/env python

from __future__ import division

from OpenGL.GL import *

class Light(object):
  def __init__(self, ambient, diffuse, specular, position, attenuation):
    self.lid = None
    self.ambient = ambient
    self.diffuse = diffuse
    self.specular = specular
    self.position = position
    self.attenuation = attenuation
    
  def enable(self):
    glEnable(self.lid)

  def place(self):
    (ac, al, aq) = self.attenuation
    glLightfv(self.lid, GL_AMBIENT, self.ambient)
    glLightfv(self.lid, GL_DIFFUSE, self.diffuse)
    glLightfv(self.lid, GL_SPECULAR, self.specular)
    glLightfv(self.lid, GL_CONSTANT_ATTENUATION, ac)
    glLightfv(self.lid, GL_LINEAR_ATTENUATION, al)
    glLightfv(self.lid, GL_QUADRATIC_ATTENUATION, aq)
    glLightfv(self.lid, GL_POSITION, self.position)

class LightSystem(object):
  def __init__(self):
    self._lid = 0
    self.lights = []
    self._toggle = False
  
  def toggle(self):
    if self._toggle:
      glDisable(GL_LIGHTING)
    else:
      glEnable(GL_LIGHTING)
    self._toggle = not self._toggle

  def add(self, item):
    item.lid = eval('GL_LIGHT%d' % self._lid) 
    self.lights.append(item)
    self._lid += 1

  def enable(self):
    for item in self.lights:
      item.enable()

  def place(self):
    for item in self.lights:
      item.place()
