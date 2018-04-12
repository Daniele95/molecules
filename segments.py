import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np

#TODO: implementare classi segmentList e pointList con metodo print

class point( object ):
  x = 0
  y = 0
  def __init__( self, x, y ):
    self.x = x
    self.y = y
  def x():
    return x
  def y():
    return x
	
	
class segment( object ):
  p1 = point( 0, 0 )
  p2 = point( 1, 0 )
  def __init__( self, p1, p2 ):
    self.p1 = p1
    self.p2 = p2
  def p1():
    return p1
  def p2():
    return p2

N = 30
segmentsRange = range( 0, N )
pointsRange = range( 0, N+1 )

def f( x ):
  return 0

segmentList = [ segment( point(i,f(i)), point(i+1,f(i+1)) ) for i in pointsRange ]

#creo anche una lista di punti, che per ora non utilizzo
pointList = [ segmentList[i].p1 for i in pointsRange ]
pointList.append(segmentList[N].p2)

s = segmentList


for i in pointsRange:
  plt.plot(segmentList[i].p1.x,segmentList[i].p1.y, 'bo' )
  
for i in segmentsRange:
  plt.plot([s[i].p1.x, s[i+1].p1.x], [s[i].p1.y, s[i+1].p1.y], color='k', linestyle='-', linewidth=2)
  


plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.show()