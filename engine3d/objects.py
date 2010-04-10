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

  @property
  def vertex_array(self):
    va = []
    for (v, c, n) in zip(self.vertices, self.colors, self.normals):
      va.append((v, c, n))
    return array(va, 'f')

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

class Cube(Object):
  def __init__(self, center, angle, size):
    super(Cube, self).__init__(center, angle, size)
    self.shape = GL_QUADS
    self.vertices = [[1, -1, 1], [1, 1, 1], # front
                     [-1, 1, 1], [-1, -1, 1],
                     [-1, -1, 1], [-1, 1, 1], # left
                     [-1, 1, -1], [-1, -1, -1],
                     [-1, -1, -1], [-1, 1, -1], # rear
                     [1, 1, -1], [1, -1, -1],
                     [1, -1, -1], [1, 1, -1], # right
                     [1, 1, 1], [1, -1, 1],
                     [1, 1, 1], [1, 1, -1], # top
                     [-1, 1, -1], [-1, 1, 1],
                     [1, -1, -1], [1, -1, 1], # bottom
                     [-1, -1, 1], [-1, -1, -1],
                    ]
    self.colors = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], # front
                   [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], # left
                   [0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1], # rear
                   [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], # right
                   [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], # top
                   [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], # bottom
                  ]
    self.normals = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], # front
                    [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], # left
                    [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1], # rear
                    [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], # right
                    [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], # top
                    [0, -1, 0], [0, -1, 0], [0, -1, 0], [0, -1, 0], # bottom
                   ]
    self.vbo = vbo.VBO(self.vertex_array)

class Wall(Object):
  def __init__(self, center, angle, width, height):
    super(Wall, self).__init__(center, angle, 1)
    self.shape = GL_TRIANGLES
    self.vertices = []
    self.colors = []
    self.normals = []
    for x in arange(-width / 2, width / 2, 1.0):
      for y in arange(height / 2, -height / 2, -1.0):
        self.vertices += [[x, y, 0], [x, y - 1, 0], [x + 1, y - 1, 0],
                          [x + 1, y - 1, 0], [x + 1, y, 0], [x, y, 0],
                         ]
        self.colors += [[0.6, 0.6, 0.6]] * 6
        self.normals += [[0, 0, 1]] * 6
    self.vbo = vbo.VBO(self.vertex_array)

class WireWall(Wall):
  def __init__(self, center, angle, width, height):
    super(WireWall, self).__init__(center, angle, width, height)
    self.shape = GL_LINES
