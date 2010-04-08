#!/usr/bin/env python

from __future__ import division

import pygame
from OpenGL import GL as gl
from OpenGL import GLU as glu

from engine3d.camera import Camera
from engine3d.lights import LightSystem

class Scene(object):
  def __init__(self, width, height, framerate):
    self.width = width
    self.height = height
    self.center = (width / 2, height / 2)
    self.framerate = framerate
    self.camera = Camera()

    self.light_system = LightSystem()
    self.objects = []

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
    gl.glFrontFace(gl.GL_CCW)
    gl.glEnable(gl.GL_CULL_FACE)
    gl.glEnable(gl.GL_COLOR_MATERIAL);
    gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)

  def convert_dev_to_user(self, x, y):
    (centerx, centery) = self.center
    x -= centerx
    y = (self.height - 1 - y) - centery
    return (x / (centerx / 2), y / (centery / 2))

  def handle_events(self):
    pass

  def render(self):
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    self.camera.place()
    self.light_system.place()
    for item in self.objects:
      item.render()

  def mainloop(self):
    video_flags = pygame.OPENGL | pygame.DOUBLEBUF
    pygame.init()
    pygame.display.set_mode((self.width, self.height), video_flags)
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    self.resize()
    self.gl_init()
    self.light_system.enable()

    clock = pygame.time.Clock()
    self.done = False
    while not self.done:
      self.handle_events()
      self.render()
      pygame.display.flip()
      clock.tick(self.framerate)
