#!/usr/bin/env python

from numpy import array
from numpy import arange
from OpenGL.arrays import vbo
from OpenGL.GL import *

class Object(object):
  def __init__(self, center, angle, size):
    self.center = center
    self.angle = angle
    self.size = size
    self._vbo = None

  @property
  def vbo(self):
    if self._vbo is None:
      va = []
      for (v, c, n) in zip(self.vertices, self.colors, self.normals):
        va.append((v, c, n))
      self._vbo = vbo.VBO(array(va, 'f'))
    return self._vbo

  def render(self):
    (ax, ay, az) = self.angle

    glPushMatrix()
    
    glTranslatef(*self.center)
    glRotatef(ax, 1, 0, 0)
    glRotatef(ay, 0, 1, 0)
    glRotatef(az, 0, 0, 1)
    glScalef(self.size, self.size, self.size)
    self.draw()

    glPopMatrix()

  def rotate(self, angle):
    self.angle = map(sum, zip(self.angle, angle))

  def draw(self):
    self.vbo.bind()
    try:
      glEnableClientState(GL_VERTEX_ARRAY);
      glEnableClientState(GL_COLOR_ARRAY);
      glEnableClientState(GL_NORMAL_ARRAY);
      glVertexPointer(3, GL_FLOAT, 36, self.vbo)
      glColorPointer(3, GL_FLOAT, 36, self.vbo + 12)
      glNormalPointer(GL_FLOAT, 36, self.vbo + 24)
      glDrawArrays(self.shape, 0, len(self.vertices))
    finally:
      self.vbo.unbind()
      glDisableClientState(GL_VERTEX_ARRAY)
      glDisableClientState(GL_COLOR_ARRAY);
      glDisableClientState(GL_NORMAL_ARRAY);

class ObjectSystem(object):
  def __init__(self):
    self.objects = []

  def add(self, item):
    self.objects.append(item)

  def render(self):
    for item in self.objects:
      item.render()
