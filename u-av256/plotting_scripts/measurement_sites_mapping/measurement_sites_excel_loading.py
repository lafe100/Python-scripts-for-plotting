# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:39:34 2018

@author: s1731217
"""

# =============================================================================
# Measurement sites excel loading -- test 
# =============================================================================
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np

import iris
import iris.plot as iplt
import iris.quickplot as qplt

fig= plt.figure(figsize=(15, 8), facecolor='white')

plt.subplot(1,1,1)
plt.title('Measurement sites in NCP, YRD, PRD',  fontsize=15)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[0], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)

x, y = map(116, 40)
x2, y2 = (-90,10)
plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='r',
                arrowprops=dict(arrowstyle="fancy", color='g')
                )

plt.show()
# =============================================================================
