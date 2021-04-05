# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np 
import scipy.special as sc 
from scipy.special import fresnel
import matplotlib.pyplot as plt
import gdspy
import datetime


# %%
def eulerBend(radius, theta, pts): 
    length = 2*radius*theta 
    
    a = 1/np.sqrt(2 * radius * length)
    s = np.linspace(0, length, pts)
    tprime = s*a*np.sqrt(2/np.pi)
    y, x = fresnel(tprime)
    return (1/a)*x, (1/a)*y

def rotate(x, y, phi):
    a = []
    b = []
    c, s = np.cos(phi), np.sin(phi)
    j = np.array([[c, s], [-s, c]])
    m = [np.dot(j, [x[i], y[i]]) for i in range(len(x))]

    for i in range(len(x)):
        a.append(m[i][0])
        b.append(m[i][1])
    
    return a, b


# %%
theta = np.pi/2
pts = 100
radius = 10
wg_width = 1

x, y = eulerBend(radius, theta/2, pts) #half the angle
a, b = rotate(-x, y, phi = -theta)

xshift = np.abs(a[-1]-x[-1])
yshift = np.abs(b[-1]-y[-1])

xfin = a + xshift
yfin = b + yshift


# %%
lib = gdspy.GdsLibrary()
date = datetime.datetime.now()
cell = lib.new_cell('eulerBend_{}'.format(date))

c = lambda x, y: [c for c in zip(x,y)]
sp1 = gdspy.FlexPath(c(x,y), wg_width, gdsii_path=True)
sp2 = gdspy.FlexPath(c(xfin, yfin), wg_width, gdsii_path=True)
cell.add(sp1)
cell.add(sp2)

lib.write_gds('eulerBend_{}.gds'.format(date))


# %%



# %%



