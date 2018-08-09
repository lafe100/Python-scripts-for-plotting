# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:55:40 2018

@author: s1731217
"""

import matplotlib.pyplot as plt

import cartopy.crs as ccrs



fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# make the map global rather than have it zoom in to
# the extents of any plotted data
ax.set_global()

ax.stock_img()
ax.coastlines()

ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())

plt.show()    

#import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
#
#plt.figure(figsize=(6, 3))
#ax = plt.axes(projection=ccrs.PlateCarree())
#ax.coastlines(resolution='110m')
#ax.gridlines()