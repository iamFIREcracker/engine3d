#!/usr/bin/env python

import sys

import pygame

from engine3d.scene import Scene
from engine3d.light import Light
from engine3d.objects import Axis
from engine3d.objects import Cube
from engine3d.objects import Wall

class MyScene(Scene):
  def __init__(self, width, height, framerate, objects, lights):
    super(MyScene, self).__init__(width, height, framerate, objects, lights)
    
    self.old = self.convert_dev_to_user(*self.center)

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.done = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.done = True
        elif event.key == pygame.K_w:
          self.camera.forward(1)
        elif event.key == pygame.K_s:
          self.camera.forward(-1)
        elif event.key == pygame.K_LSHIFT:
          self.camera.up(1)
        elif event.key == pygame.K_c:
          self.camera.up(-1)
        elif event.key == pygame.K_d:
          self.camera.right(1)
        elif event.key == pygame.K_a:
          self.camera.right(-1)
        elif event.key == pygame.K_UP:
          self.camera.pitch(5)
        elif event.key == pygame.K_DOWN:
          self.camera.pitch(-5)
        elif event.key == pygame.K_LEFT:
          self.camera.yaw(5)
        elif event.key == pygame.K_RIGHT:
          self.camera.yaw(-5)
      elif event.type == pygame.MOUSEMOTION:
        (ox, oy) = self.old
        (x, y) = self.convert_dev_to_user(*event.pos)
        self.camera.rotate(((y - oy) * 22.5, -(x - ox) * 22.5, 0))
        if x > 0.8 or x < 0.8 or y > 0.8 or y < -0.8:
          self.old = self.convert_dev_to_user(*self.center)
          pygame.mouse.set_pos(*self.center)
        else:
          self.old = (x, y)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.camera.forward(1)
    elif keys[pygame.K_s]:
      self.camera.forward(-1)
    elif keys[pygame.K_LSHIFT]:
      self.camera.up(1)
    elif keys[pygame.K_c]:
      self.camera.up(-1)
    elif keys[pygame.K_d]:
      self.camera.right(1)
    elif keys[pygame.K_a]:
      self.camera.right(-1)
    elif keys[pygame.K_UP]:
      self.camera.pitch(5)
    elif keys[pygame.K_DOWN]:
      self.camera.pitch(-5)
    elif keys[pygame.K_LEFT]:
      self.camera.yaw(5)
    elif keys[pygame.K_RIGHT]:
      self.camera.yaw(-5)

def main(argv):
  if (len(argv) != 4):
    print "Usage: %s <width> <height> <framerate>" % argv[0]
    print "Switching defaults: 400, 400, 30"
    (width, height, framerate) = (400, 400, 30)
  else:
    (width, height, framerate) = map(int, argv[1:])

  objects = [Axis((0, 0, 0)),
             Cube((1, 1, 1)),
             Cube((-1, 0, 0)),
             #Wall((0, 0, 15), (0, 0, 0), 10.0, 10.0, 1.0),  # front
             Wall((0, 0, -5), (0, 0, 0), 10.0, 10.0, 1.0),  # rear
             Wall((-5, 0, 5), (0, 90, 0), 20.0, 10.0, 1.0), # left
             Wall((5, 0, 5), (0, 90, 0), 20.0, 10.0, 1.0),  # right
             Wall((0, -5, 5), (90, 0, 0), 10.0, 20.0, 1.0), # bottom
             Wall((0, 5, 5), (90, 0, 0), 10.0, 20.0, 1.0),  # top
            ] 
  lights = [Light(id=0,
                  center=(0.0, 0.0, 10.0, 1.0),
                  ambient=(1.0, 1.0, 1.0, 1.0),
                  diffuse=(1.0, 1.0, 1.0, 1.0),
                 ),
           ]
  s = MyScene(width, height, framerate, objects, lights)
  s.camera.center = (0, 0, 10)
  s.mainloop()

if __name__ == '__main__':
  sys.exit(main(sys.argv))
