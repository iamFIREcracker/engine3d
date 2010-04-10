#!/usr/bin/env python

from engine3d.objects import Object
from engine3d.objects import GL_QUADS

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