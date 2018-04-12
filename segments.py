import matplotlib.pyplot as plt

class point( object ):
  x = 0
  y = 0
  def __init__( self, x, y ):
    self.x = x
    self.y = y
	
class segment( object ):
  p1 = point( 0, 0 )
  p2 = point( 1, 0 )
  def __init__( self, p1, p2 ):
    self.p1 = p1
    self.p2 = p2

class membrana( object ):
  points = []
  indices = []
  segments = []
  
  def __init__( self, points, indices ):
    self.points = points
    self.indices = indices
    l = len( points )
    self.segments = [ segment( points[indices[i]], points[indices[i+1]] ) for i in range ( 0, l-1 ) ]
	
  def plot( self ):
    l = len( points )
    for i in range ( 0, l ):
      plt.plot( points[i].x, points[i].y, 'bo' )
    for i in range( 0, l-1 ):
      s = self.segments
      plt.plot( [s[i].p1.x, s[i].p2.x], [s[i].p1.y, s[i].p2.y], color='k', linestyle='-', linewidth=2)


points = [point(1,0), point(2,.5), point(3,2),point(5,.1)]
indices = [0,3,2,1]

m = membrana( points, indices )
m.plot()


plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.show()