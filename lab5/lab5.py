
# coding: utf-8

# In[3]:

print (1+1)
print (1/2)
print (1.0/2.0)
print ('Hello world')

from vpython import *

g = 9.8
height = 15.0
size = 0.25


scene = canvas(width = 800, height = 800, center = vector(0,height,0), background = vector(0.5,0.5,0))
floor = box(length = 30, height = 0.01, width = 10, color = color.blue)
ball = sphere(radius = size, color = color.red)
arrowV = arrow(shaftwidth = 0.1, color = color.cyan)

ball.pos = vector(-15,2,0)
ball.v = vector(8,8,0)
arrowV.pos = vector(-15,2,size)
arrowV.axis = ball.v

dt = 0.001
t = 0
while ball.pos.y>=size:
    rate(1000)
    
    ball.pos += ball.v*dt
    arrowV.pos = ball.pos + vector(0,0,size)
    ball.v.y += -g*dt
    arrowV.axis = ball.v
    t += dt
    
print('How much time stay in the air: '+str(t))


# In[ ]:




# In[ ]:



