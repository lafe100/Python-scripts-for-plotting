import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

import iris
import iris.plot as iplt
import iris.quickplot as qplt

co_stash = ['m01s34i010']

'''
filename = ['/exports/csce/datastore/geos/users/s1731217/u-av256_20130901_16m/*jan*',
            '/exports/csce/datastore/geos/users/s1731217/u-av256_20130901_16m/*feb*']
'''

filename = '/exports/csce/datastore/geos/users/s1731217/u-av256_20130901_16m/*'
            

stash_constraint = iris.AttributeConstraint(STASH=co_stash[0])
latitude_constraint = iris.Constraint(coord_values={'latitude':lambda cell: 17.5 < cell < 45})
longitude_constraint = iris.Constraint(coord_values={'longitude':lambda cell: 107.5 < cell < 125})
cube = iris.load(filename, stash_constraint).extract(latitude_constraint & longitude_constraint)

co_ppb = cube[0]*29.0*1.0e9/48.0

fig= plt.figure(figsize=(24, 8))

plt.subplot(3,4,1)
plt.title('CO Jan 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[0][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,2)
plt.title('CO Feb 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[1][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,3)
plt.title('CO Mar 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[2][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,4)
plt.title('CO Apr 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[3][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,5)
plt.title('CO May 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[4][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,6)
plt.title('CO Jun 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[5][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,7)
plt.title('CO Jul 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[6][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,8)
plt.title('CO Aug 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[7][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,9)
plt.title('CO Sep 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[8][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,10)
plt.title('CO Oct 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[9][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,11)
plt.title('CO Nov 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[10][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,12)
plt.title('CO Dec 2014',  fontsize=5)
tick_levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 2000, 3000, 4500]
iplt.contourf(co_ppb[11][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([100, 300, 500, 700, 900, 1200, 2000, 4500], fontsize=8)
cb1.set_label('ppb')


plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.87, top=0.9, hspace=0.2, wspace=0.2)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_plotting/co_monthly_2014_spin_up.png', dpi=600, transparent=True)

plt.show()

