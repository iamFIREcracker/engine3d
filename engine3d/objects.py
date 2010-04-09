#!/usr/bin/env python

from OpenGL import GL as gl

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

  def draw(self):
    gl.glBegin(gl.GL_TRIANGLES)
    for (face, normal, color) in zip(self.faces, self.normals, self.colors):
      gl.glNormal3fv(normal)
      gl.glColor3fv(color)
      for p in face:
        gl.glVertex3fv(self.points[p])
    gl.glEnd()

class Cube(Object):
  def __init__(self, center, angle, r=1):
    self.center = center
    self.angle = (0.0, 0.0, 0.0)
    self.points = ((r, -r, r), (r, r, r),
                   (-r, r, r), (-r, -r, r),
                   (r, -r, -r), (r, r, -r),
                   (-r, r, -r), (-r, -r, -r),
                  )
    self.faces = ((0, 1, 2), (2, 3, 0),
                  (3, 2, 6), (6, 7, 3),
                  (7, 6, 5), (5, 4, 7),
                  (4, 5, 1), (1, 0, 4),
                  (1, 5, 6), (6, 2, 1),
                  (4, 0, 3), (3, 7, 4),
                 )
    self.normals = ((0, 0, 1), (0, 0, 1),
                    (-1, 0, 0), (-1, 0, 0),
                    (0, 0, -1), (0, 0, -1),
                    (1, 0, 0), (1, 0, 0),
                    (0, 1, 0), (0, 1, 0),
                    (0, -1, 0), (0, -1, 0),
                   )
    self.colors = ((0, 0, 1), (0, 0, 1),
                   (0, 1, 0), (0, 1, 0),
                   (0, 1, 1), (0, 1, 1),
                   (1, 0, 0), (1, 0, 0),
                   (1, 0, 1), (1, 0, 1),
                   (1, 1, 0), (1, 1, 0),
                  )
    
class Wall(Object):
  def __init__(self, center, angle, width, height):
    self.center = center
    self.angle = angle
    self.points = ((width / 2, -height / 2, 0),
                   (width / 2, height / 2, 0),
                   (-width / 2, height / 2, 0),
                   (-width / 2, -height / 2, 0),
                  )
    self.faces = ((0, 1, 2), (2, 3, 0),
                 )
    self.normals = ((0, 0, 1), (0, 0, 1),
                   )
    self.colors = ((.6, .6, .6), (.6, .6, .6),
                  )
