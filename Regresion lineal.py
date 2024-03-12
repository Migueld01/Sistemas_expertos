# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:36:51 2023

@author: Usuario
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.array([-2,-1,0,1,2])
y=x*2

w=0

m=5
e=np.zeros((5,1))
for w in range(5):
    y_e=w*x
    e[w]=np.sum(np.power(y_e-y,2))/(2*m)
    
w=np.array([0,1,2,3,4])
plt.plot(w,e)














































