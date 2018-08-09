import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

import iris
import iris.plot as iplt
import iris.quickplot as qplt

ozone_stash = ['m01s34i002']


'''
filename = ['/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014jan.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014feb.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014mar.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014apr.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014may.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014jun.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014jul.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014aug.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014sep.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014oct.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014nov.pp',
            '/exports/csce/datastore/geos/users/s1731217/u-av257_20140101_12m/av257a.pm2014dec.pp']
'''

filename = '/exports/csce/datastore/geos/users/s1731217/u-av256_20130901_16m/*'

stash_constraint = iris.AttributeConstraint(STASH=ozone_stash[0])
latitude_constraint = iris.Constraint(coord_values={'latitude':lambda cell: 17.5 < cell < 45})
longitude_constraint = iris.Constraint(coord_values={'longitude':lambda cell: 107.5 < cell < 125})
cube = iris.load(filename, stash_constraint).extract(latitude_constraint & longitude_constraint)


print cube

print cube[0]

cube_ppb = cube[0]*29.0*1.0e9/48.0

print cube_ppb

fig= plt.figure(figsize=(24, 8))

plt.subplot(3,4,1)
plt.title('NO Jan 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[0][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   #Taiwan
m.readshapefile('bou2_4l', 'states', drawbounds=True)   #South sea boundary
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,2)
plt.title('NO Feb 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[1][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,3)
plt.title('NO Mar 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[2][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,4)
plt.title('NO Apr 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[3][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,5)
plt.title('NO May 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[4][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,6)
plt.title('NO Jun 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[5][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,7)
plt.title('NO Jul 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[6][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,8)
plt.title('NO Aug 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[7][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,9)
plt.title('NO Sep 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[8][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,10)
plt.title('NO Oct 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[9][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,11)
plt.title('NO Nov 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[10][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,12)
plt.title('NO Dec 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 200]
iplt.contourf(cube_ppb[11][0], tick_levels, cmap='cubehelix_r', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 200], fontsize=8)
cb1.set_label('ppb')


plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.87, top=0.9, hspace=0.2, wspace=0.2)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_plotting/no_monthly_2014_spin_up.png', dpi=600, transparent=True)

plt.show()
