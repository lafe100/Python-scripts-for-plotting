# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:45:24 2018

@author: s1731217
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


#map = Basemap( 
#              lat_0=0, lon_0=0)
map = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
map.readshapefile('CHN_adm1', 'states', drawbounds=True)



x, y = map(116, 40) # lon, lat
x2, y2 = (-90, 10)
x3, y3 = (30, 10)
x4, y4 = (-150, 20)

plt.annotate('Barcelona', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='r',
                arrowprops=dict(arrowstyle="fancy", color='g')
                )

  
lat_abj, lon_abj   = map(116.41, 39.9)
lat_asjz, lon_asjz = map(114.51, 38.04)
lat_ash, lon_ash   = map(121.47, 31.23)
lat_anj, lon_anj   = map(118.80, 32.06)
lat_agz, lon_agz   = map(113.26, 23.13)
lat_ahk, lon_ahk   = map(114.19, 22.33)

plt.annotate('Beijing', xy=(lat_abj, lon_abj),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Shijiazhuang', xy=(lat_asjz, lon_asjz),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Shanghai', xy=(lat_ash, lon_ash),  xycoords='data',
                xytext=(x3, y3), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Nanjing', xy=(lat_anj, lon_anj),  xycoords='data',
                xytext=(x2, y2), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Guangzhou', xy=(lat_agz, lon_agz),  xycoords='data',
                xytext=(x4, y4), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Hong Kong', xy=(lat_ahk, lon_ahk),  xycoords='data',
                xytext=(x4, y4), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )
plt.show()