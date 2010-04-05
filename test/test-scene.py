#!/usr/bin/env python

import sys

import pygame

from engine3d.scene import Scene
from engine3d.light import Light
from engine3d.objects import Axis
from engine3d.objects import Cube
from engine3d.objects import Wall

def myrange(start, stop, step):
  while start < stop:
    yield start
    start += step

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
  s = Scene(width, height, framerate, objects, lights)
  s.camera.center = (0, 0, 10)
  for event in s.mainloop():
    if event.type == pygame.QUIT:
      s.done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        s.done = True
      elif event.key == pygame.K_w:
        s.camera.forward(1)
      elif event.key == pygame.K_s:
        s.camera.forward(-1)
      elif event.key == pygame.K_LSHIFT:
        s.camera.up(1)
      elif event.key == pygame.K_c:
        s.camera.up(-1)
      elif event.key == pygame.K_d:
        s.camera.right(1)
      elif event.key == pygame.K_a:
        s.camera.right(-1)
      elif event.key == pygame.K_UP:
        s.camera.pitch(5)
      elif event.key == pygame.K_DOWN:
        s.camera.pitch(-5)
      elif event.key == pygame.K_LEFT:
        s.camera.yaw(5)
      elif event.key == pygame.K_RIGHT:
        s.camera.yaw(-5)
    elif event.type == pygame.MOUSEMOTION:
      (_, _, az) = s.camera.angle
      (x, y) = s.convert_dev_to_user(*event.pos)
      s.camera.rotate((y * 22.5, -x * 22.5, 0))

if __name__ == '__main__':
  sys.exit(main(sys.argv))
