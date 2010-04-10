#!/usr/bin/env python

import sys

from engine3d.scene import Scene
from engine3d.lights import Light
import pygame

from objects import Cube
from objects import Wall

class MyScene(Scene):
  def __init__(self, width, height, framerate):
    super(MyScene, self).__init__(width, height, framerate)

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.done = True
      elif event.type == pygame.VIDEOEXPOSE:
        pygame.mouse.get_rel()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.done = True
        elif event.key == pygame.K_l:
          self.light_system.toggle()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
          self.camera.forward(1)
        elif event.button == 5:
          self.camera.forward(-1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.camera.forward(1)
    if keys[pygame.K_s]:
      self.camera.forward(-1)
    if keys[pygame.K_LSHIFT]:
      self.camera.up(1)
    if keys[pygame.K_c]:
      self.camera.up(-1)
    if keys[pygame.K_d]:
      self.camera.right(1)
    if keys[pygame.K_a]:
      self.camera.right(-1)
    if keys[pygame.K_UP]:
      self.camera.pitch(3)
    if keys[pygame.K_DOWN]:
      self.camera.pitch(-3)
    if keys[pygame.K_LEFT]:
      self.camera.yaw(3)
    if keys[pygame.K_RIGHT]:
      self.camera.yaw(-3)

    (cx, cy) = self.center
    (dx, dy) = pygame.mouse.get_rel()
    (x, y) = (dx / cx, -dy / cy)
    self.camera.rotate((y * 22.5, -x * 22.5, 0))

def main(argv):
  if (len(argv) != 4):
    print "Usage: %s <width> <height> <framerate>" % argv[0]
    print "Switching defaults: 400, 400, 30"
    (width, height, framerate) = (400, 400, 30)
  else:
    (width, height, framerate) = map(int, argv[1:])

  s = MyScene(width, height, framerate)

  s.camera.center = (0, 0, 10)
  s.light_system.add(Light((0, 1, 0, 1))),
  s.object_system.add(Cube((0.0, 0.0, 0.0),
                           (0.0, 0.0, 0.0),
                           1))
  s.object_system.add(Wall((0, 5, 0),
                           (90, 0, 0),
                           50.0,
                           50.0))
  s.object_system.add(Wall((0, -5, 0),
                           (-90, 0, 0),
                           50.0,
                           50.0))

  s.mainloop()

if __name__ == '__main__':
  sys.exit(main(sys.argv))
