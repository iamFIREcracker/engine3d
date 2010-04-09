#!/usr/bin/env python

from __future__ import division
from math import cos
from math import sin

from OpenGL import GL as gl

pidiv180 = 0.017453292519943295

class Camera(object):
  def __init__(self):
    self.center = (0.0, 0.0, 0.0)
    self.angle = (0.0, 0.0, 0.0)
    self._directions = ((0.0, 0.0, -1.0), (1.0, 0.0, 0.0))
    self._rotated = True

  @property
  def directions(self):
    if self._rotated:
      (cx, cy, cz) = map(lambda v: cos(v * pidiv180), self.angle)
      (sx, sy, sz) = map(lambda v: sin(v * pidiv180), self.angle)
      self._directions = ((cy * cz,
                           cy * sz,
                           -sy,
                          ),
                          (
                          ),
                          (cx * cz * sy + sx * sz,
                           -cz * sx + cx * sy * sz,
                           cx * cy,
                          ),
                         )
      self._rotated = False
    return self._directions

  def place(self):
    (cx, cy, cz) = self.center
    (ax, ay, az) = self.angle

    gl.glLoadIdentity()
    gl.glRotatef(-ax, 1, 0, 0)
    gl.glRotatef(-ay, 0, 1, 0)
    gl.glRotatef(-az, 0, 0, 1)
    gl.glTranslatef(-cx, -cy, -cz)
  
  def move(self, direction):
    self.center = map(sum, zip(self.center, direction))

  def rotate(self, angle):
    self.angle = map(sum, zip(self.angle, angle))
    self._rotated = True

  def forward(self, offset):
    (_, _, dz) = self.directions
    self.move(map(lambda v: v * -offset, dz))

  def up(self, offset):
    direction = (0,
                 offset,
                 0,
                )
    self.move(direction)
    
  def right(self, offset):
    (dx, _, _) = self.directions
    self.move(map(lambda v: v * offset, dx))

  def pitch(self, angle):
    self.rotate((angle, 0, 0))

  def yaw(self, angle):
    self.rotate((0, angle, 0))

  def roll(self, angle):
    self.rotate((0, 0, angle))
