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


# %%

lib = gdspy.GdsLibrary()
date = datetime.datetime.now()
cell = lib.new_cell('eulerBend_{}'.format(date))


# %%
x, y = eulerBend(10, np.pi/2, 100)
c = lambda x, y: [c for c in zip(x,y)]
wg_width = 1 #um


# %%

sp1 = gdspy.FlexPath(c(x,y), wg_width, gdsii_path=True)
cell.add(sp1)

lib.write_gds('eulerBend_{}.gds'.format(date))


