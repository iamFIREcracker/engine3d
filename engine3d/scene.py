#!/usr/bin/env python

from __future__ import division

import pygame
from OpenGL import GL as gl
from OpenGL import GLU as glu

from engine3d.camera import Camera

class Scene(object):
  def __init__(self, width, height, framerate, objects, lights):
    self.width = width
    self.height = height
    self.center = (width / 2, height / 2)
    self.framerate = framerate
    self.camera = Camera()

    self.objects = objects
    self.lights = lights

  def resize(self):
    if self.height == 0:
      self.height = 1
    gl.glViewport(0, 0, self.width, self.height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45, self.width / self.height, 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

  def gl_init(self):
    gl.glShadeModel(gl.GL_SMOOTH)
    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    gl.glClearDepth(1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glDepthFunc(gl.GL_LEQUAL)
    gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)
    #gl.glEnable(gl.GL_LIGHTING)

  def convert_dev_to_user(self, x, y):
    (centerx, centery) = self.center
    x -= centerx
    y = (self.height - 1 - y) - centery
    return (x / (centerx / 2), y / (centery / 2))

  def handle_events(self):
    pass

  def draw(self):
    self.camera.draw()

    for item in self.lights:
      item.draw()

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    for item in self.objects:
      gl.glPushMatrix()
      item.draw()
      gl.glPopMatrix()

  def mainloop(self):
    video_flags = pygame.OPENGL | pygame.DOUBLEBUF
    pygame.init()
    pygame.display.set_mode((self.width, self.height), video_flags)
    pygame.mouse.set_visible(False)
    pygame.mouse.set_pos(self.center)

    self.resize()
    self.gl_init()

    clock = pygame.time.Clock()
    self.done = False
    while not self.done:
      for event in pygame.event.get():
        yield event
      self.draw()
      pygame.display.flip()
      pygame.mouse.set_pos(self.center)
      clock.tick(self.framerate)