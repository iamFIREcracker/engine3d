#!/usr/bin/env python

from OpenGL import GL as gl

def draw_quads(obj):
  gl.glBegin(gl.GL_QUADS)
  for (face, normal, color) in zip(obj.faces, obj.normals, obj.colors):
    gl.glNormal3fv(normal)
    gl.glColor3fv(color)
    for p in face:
      gl.glVertex3fv(obj.points[p])
  gl.glEnd()

class Object(object):
  def render(self):
    (ax, ay, az) = self.angle

    gl.glPushMatrix()
    
    gl.glTranslatef(*self.center)
    gl.glRotatef(ax, 1, 0, 0)
    gl.glRotatef(ay, 0, 1, 0)
    gl.glRotatef(az, 0, 0, 1)
    self.draw()

    gl.glPopMatrix()

  def rotate(self, angle):
    self.angle = map(sum, zip(self.angle, angle))

class Cube(Object):
  def __init__(self, center, angle, r=1):
    self.center = center
    self.angle = (0.0, 0.0, 0.0)
    self.points = ((r, -r, r), (r, r, r),
                   (-r, r, r), (-r, -r, r),
                   (r, -r, -r), (r, r, -r),
                   (-r, r, -r), (-r, -r, -r),
                  )
    self.faces = ((0, 1, 2, 3),
                  (3, 2, 6, 7),
                  (7, 6, 5, 4),
                  (4, 5, 1, 0),
                  (1, 5, 6, 2),
                  (4, 0, 3, 7),
                 )
    self.normals = ((0, 0, 1),
                    (-1, 0, 0),
                    (0, 0, -1),
                    (1, 0, 0),
                    (0, 1, 0),
                    (0, -1, 0),
                   )
    self.colors = ((0, 0, 1),
                   (0, 1, 0),
                   (0, 1, 1),
                   (1, 0, 0),
                   (1, 0, 1),
                   (1, 1, 0),
                  )

  def draw(self):
    draw_quads(self)
    
class Wall(Object):
  def __init__(self, center, angle, width, height):
    self.center = center
    self.angle = angle
    self.points = ((width / 2, -height / 2, 0),
                   (width / 2, height / 2, 0),
                   (-width / 2, height / 2, 0),
                   (-width / 2, -height / 2, 0),
                  )
    self.faces = ((0, 1, 2, 3),
                 )
    self.normals = ((0, 0, 1),
                   )
    self.colors = ((.6, .6, .6),
                  )

  def draw(self):
    draw_quads(self)
