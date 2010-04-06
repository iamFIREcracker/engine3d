#!/usr/bin/env python

from OpenGL import GL as gl

class Axis(object):
  def __init__(self, center, r=10):
    self.center = center
    self.points = ((0, 0, 0), (r, 0, 0),
                   (0, 0, 0), (0, r, 0),
                   (0, 0, 0), (0, 0, r),
                  )

  def draw(self):
    gl.glTranslatef(*self.center)

    gl.glBegin(gl.GL_LINES)
    gl.glColor3fv((1.0, 0.0, 0.0))
    for p in self.points[0:2]:
        gl.glVertex3fv(p)
    gl.glColor3fv((0.0, 1.0, 0.0))
    for p in self.points[2:4]:
        gl.glVertex3fv(p)
    gl.glColor3fv((0.0, 0.0, 1.0))
    for p in self.points[4:6]:
        gl.glVertex3fv(p)
    gl.glEnd()

class Cube(object):
  def __init__(self, center, r=0.5):
    self.center = center
    self.rotation = (0, 0, 0)
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
    (rx, ry, rz) = self.rotation

    gl.glTranslatef(*self.center)
    gl.glRotatef(rx, 1, 0, 0)
    gl.glRotatef(ry, 0, 1, 0)
    gl.glRotatef(rz, 0, 0, 1)
    
    gl.glBegin(gl.GL_QUADS)
    for (face, normal, color) in zip(self.faces, self.normals, self.colors):
      gl.glNormal3fv(normal)
      gl.glColor3fv(color)
      for p in face:
        gl.glVertex3fv(self.points[p])
    gl.glEnd()

    self.rotate((1.0, 1.0, 0.0))

  def rotate(self, rotation):
    self.rotation = map(sum, zip(self.rotation, rotation))
    
class Wall(object):
  def __init__(self, center, rotation, width, height, delta):
    self.center = center
    self.rotation = rotation
    points = []
    x = -width / 2
    while x <= width / 2:
      points.append((x, height / 2, 0))
      points.append((x, -height / 2, 0))
      x += delta
    y = -height / 2
    while y <= height / 2:
      points.append((-width / 2, y, 0))
      points.append((width / 2, y, 0))
      y += delta
    self.points = tuple(points)

  def draw(self):
    (rx, ry, rz) = self.rotation

    gl.glTranslatef(*self.center)
    gl.glRotatef(rx, 1, 0, 0)
    gl.glRotatef(ry, 0, 1, 0)
    gl.glRotatef(rz, 0, 0, 1)

    gl.glBegin(gl.GL_LINES)
    gl.glColor3fv((1.0, 1.0, 1.0))
    for p in self.points:
        gl.glVertex3fv(p)
    gl.glEnd()
