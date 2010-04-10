#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.arrays import vbo
from numpy import array

class Object(object):
  def render(self):
    (ax, ay, az) = self.angle

    glPushMatrix()
    
    glTranslatef(*self.center)
    glRotatef(ax, 1, 0, 0)
    glRotatef(ay, 0, 1, 0)
    glRotatef(az, 0, 0, 1)
    self.draw()

    glPopMatrix()

  @property
  def vertex_array(self):
    return array([v + c + n for (v, c, n) in zip(self.vertices,
                                                 self.colors,
                                                 self.normals)], 'f')

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
      glDrawArrays(GL_TRIANGLES, 0, len(self.vertices))
    finally:
      self.vbo.unbind()
      glDisableClientState(GL_VERTEX_ARRAY)
      glDisableClientState(GL_COLOR_ARRAY);
      glDisableClientState(GL_NORMAL_ARRAY);

class Cube(Object):
  def __init__(self, center, angle, r=1):
    self.center = center
    self.angle = (0.0, 0.0, 0.0)
    self.vertices = [[1, -1, 1], [1, 1, 1], [-1, 1, 1], # front
                     [-1, 1, 1], [-1, -1, 1], [1, -1, 1],
                     [-1, -1, 1], [-1, 1, 1], [-1, 1, -1], # left
                     [-1, 1, -1], [-1, -1, -1], [-1, -1, 1],
                     [-1, -1, -1], [-1, 1, -1], [1, 1, -1], # rear
                     [1, 1, -1], [1, -1, -1], [-1, -1, -1],
                     [1, -1, -1], [1, 1, -1], [1, 1, 1], # right
                     [1, 1, 1], [1, -1, 1], [1,-1, -1],
                     [1, 1, 1], [1, 1, -1], [-1, 1, -1], # top
                     [-1, 1, -1], [-1, 1, 1], [1, 1, 1],
                     [1, -1, -1], [1, -1, 1], [-1, -1, 1], # bottom
                     [-1, -1, 1], [-1, -1, -1], [1, -1, -1],
                    ]
    self.colors = [[0, 0, 1], [0, 0, 1], [0, 0, 1], # front
                   [0, 0, 1], [0, 0, 1], [0, 0, 1],
                   [0, 1, 0], [0, 1, 0], [0, 1, 0], # left
                   [0, 1, 0], [0, 1, 0], [0, 1, 0],
                   [0, 1, 1], [0, 1, 1], [0, 1, 1], # rear
                   [0, 1, 1], [0, 1, 1], [0, 1, 1],
                   [1, 0, 0], [1, 0, 0], [1, 0, 0], # right
                   [1, 0, 0], [1, 0, 0], [1, 0, 0],
                   [1, 0, 1], [1, 0, 1], [1, 0, 1], # top
                   [1, 0, 1], [1, 0, 1], [1, 0, 1],
                   [1, 1, 0], [1, 1, 0], [1, 1, 0], # bottom
                   [1, 1, 0], [1, 1, 0], [1, 1, 0],
                  ]
    self.normals = [[0, 0, 1], [0, 0, 1], [0, 0, 1], # front
                    [0, 0, 1], [0, 0, 1], [0, 0, 1], 
                    [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], # left
                    [-1, 0, 0], [-1, 0, 0], [-1, 0, 0],
                    [0, 0, -1], [0, 0, -1], [0, 0, -1], # rear
                    [0, 0, -1], [0, 0, -1], [0, 0, -1],
                    [0, 0, 1], [0, 0, 1], [0, 0, 1], # right
                    [0, 0, 1], [0, 0, 1], [0, 0, 1],
                    [0, 1, 0], [0, 1, 0], [0, 1, 0], # top
                    [0, 1, 0], [0, 1, 0], [0, 1, 0],
                    [0, -1, 0], [0, -1, 0], [0, -1, 0], # bottom
                    [0, -1, 0], [0, -1, 0], [0, -1, 0],
                   ]
    self.vbo = vbo.VBO(self.vertex_array)

class Wall(Object):
  def __init__(self, center, angle, width, height):
    self.center = center
    self.angle = angle
    self.vertices = [[width / 2, -height / 2, 0],
                     [width / 2, height / 2, 0],
                     [-width / 2, height / 2, 0],
                     [-width / 2, height / 2, 0],
                     [-width / 2, -height /2, 0],
                     [width / 2, -height / 2, 0],
                    ]
    self.colors = [[0.6, 0.6, 0.6], [0.6, 0.6, 0.6], [0.6, 0.6, 0.6],
                   [0.6, 0.6, 0.6], [0.6, 0.6, 0.6], [0.6, 0.6, 0.6],
                  ]
    self.normals = [[0, 0, 1], [0, 0, 1], [0, 0, 1],
                    [0, 0, 1], [0, 0, 1], [0, 0, 1],
                   ]
    self.vbo = vbo.VBO(self.vertex_array)
