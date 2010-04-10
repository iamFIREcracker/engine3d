#!/usr/bin/env python

from __future__ import division

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

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
    glViewport(0, 0, self.width, self.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, self.width / self.height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

  def gl_init(self):
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glFrontFace(GL_CCW)
    glEnable(GL_CULL_FACE)
    glEnable(GL_COLOR_MATERIAL);

  def handle_events(self):
    pass

  def render(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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
