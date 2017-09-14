
# coding: utf-8

# In[1]:

from vpython import *
canvas()
face = sphere()
right_ear = sphere(pos=vector(0.8,0.8,0.8), radius=0.3, color=color.yellow)
left_ear = sphere(pos=vector(-0.8,0.8,0.8), radius=0.3, color=color.yellow)
rightEye= sphere(pos=vector(0.35,0.35,1),radius=0.2, color=color.red)
leftEye= sphere(pos=vector(-0.35,0.35,1),radius=0.2, color=color.red)
nose = sphere(pos=vector(0,0,1.1),radius=0.1,color=color.green)
mouse=ellipsoid(pos=vector(0,-0.3,1),length=0.8,height=0.15,weigth=1,color=color.blue)


# In[ ]:



