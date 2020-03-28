# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:57:58 2020

@author: maciej
"""

#ex1
import math
k = 1240*math.sqrt(7)
m = 4467
l = 2j
d = k+m
c = d+l

#ex2
print(d)
print("%0.3f"%d)
print("%0.20f"%d)

#ex3
r = 17
h = 33
V = 2*math.pi*r*h + 2*math.pi*r*r

#ex4

#ex5
def calcB(x1, t, r):
    return ((x1+r)/(r*math.sin(2*x1)+3.3456))*(x1**(t*r))
print(calcB(1, 1, 1))

#ex6
import numpy as np
a = math.sqrt(2)
M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
print(M)
print(np.linalg.inv(M))
print(np.linalg.det(M))
print(M.T)

#ex62
print(M[0,0], M[2,2], M[2,1])
w1 = M[:, 2]
w2 = M[1, :]

#ex7
roots1 = np.roots([1, -7, -3, -43, -28, -60])
print(np.polyval([1, -7, -3, -43, -28, -60], roots1))

#ex8
print(np.arange(1, 3, 0.5))
print(np.linspace(1,3,8))

#ex9

def f1(x):
    return x**3-3*x
import matplotlib.pyplot as plt
x1 = np.linspace(-1, 1, 100)
x2 = np.linspace(-5, 5, 100)
x3 = np.linspace(0, 5, 100)
plt.plot(x1, f1(x1), x2, f1(x2), x3, f1(x3))

#ex10
def heat(m, v):
    return (m*v**2)/2
print(heat(2.5, 600/36))

plt.figure()
x1 = np.linspace(2000/36, 0, 100)
plt.plot(x1, heat(3, x1))
plt.yscale("log")

#ex11
class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def conjugate(self):
        return Quaternion(self.x, -self.y, -self.z, -self.w)
    
    def norm(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
    
    def __add__(self, quat2):
        return Quaternion(self.x+quat2.x, self.y+quat2.y, self.z+quat2.z, self.w+quat2.w)
    
    def __sub__(self, quat2):
        return Quaternion(self.x-quat2.x, self.y-quat2.y, self.z-quat2.z, self.w-quat2.w)
    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z) + ' ' + str(self.w)
    
quat1 = Quaternion(1,1,1,1)
quat2 = Quaternion(2,2,2,2)
print(quat1+quat2)
print(quat1-quat2)        
print(quat1.norm())
print(quat1.conjugate())

