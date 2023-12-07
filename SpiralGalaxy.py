import random
from math import *
from pylab import *
import numpy as np

n=1000
a=0.5
b=0.6
th=np.random.randn(n)
x=a*exp(b*th)*cos(th)
y=a*exp(b*th)*sin(th)
x1=a*exp(b*(th))*cos(th+pi)
y1=a*exp(b*(th))*sin(th+pi)

sx=np.random.normal(0, a*0.25, n)
sy=np.random.normal(0, a*0.25, n)
plot(x+sy,y+sx,"*")
plot(x1+sx, y1+sy,"*")

show()
