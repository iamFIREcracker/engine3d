#!/usr/bin/env python

from engine3d.objects import Object
from engine3d.objects import GL_QUADS
from engine3d.objects import GL_LINE_STRIP
from numpy import arange

class Wall(Object):
  def __init__(self, center, angle, width, height):
    super(Wall, self).__init__(center, angle, 1)
    self.shape = GL_QUADS
    self.vertices = []
    self.colors = []
    self.normals = []
    for y in arange(height / 2, -height / 2, -1.0):
      for x in arange(-width / 2, width / 2, 1.0):
        self.vertices += [[x, y, 0], [x, y - 1, 0],
                          [x + 1, y - 1, 0], [x + 1, y, 0],
                         ]
        self.colors += [[0.6, 0.6, 0.6]] * 4
        self.normals += [[0, 0, 1]] * 4

class Checkerboard(Wall):
  def __init__(self, center, angle, width, height):
    super(Wall, self).__init__(center, angle, 1)
    self.shape = GL_QUADS
    self.vertices = []
    self.colors = []
    self.normals = []
    for (i, y) in enumerate(arange(height / 2, -height / 2, -1.0)):
      for (j, x) in enumerate(arange(-width / 2, width / 2, 1.0)):
        if (i + j) % 2:
          self.vertices += [[x, y, 0], [x, y - 1, 0],
                            [x + 1, y - 1, 0], [x + 1, y, 0],
                           ]
          self.colors += [[0.6, 0.6, 0.6]] * 4
          self.normals += [[0, 0, 1]] * 4
