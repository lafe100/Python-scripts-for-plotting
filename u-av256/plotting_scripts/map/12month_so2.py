import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

import iris
import iris.plot as iplt
import iris.quickplot as qplt

ozone_stash = ['m01s34i092']

filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/apm.pp/*'

stash_constraint = iris.AttributeConstraint(STASH=ozone_stash[0])
latitude_constraint = iris.Constraint(coord_values={'latitude':lambda cell: 17.5 < cell < 45})
longitude_constraint = iris.Constraint(coord_values={'longitude':lambda cell: 107.5 < cell < 125})
cube = iris.load(filename, stash_constraint).extract(latitude_constraint & longitude_constraint)
#cube = iris.load(filename).extract(latitude_constraint & longitude_constraint)


print cube

print cube[0]

cube_ppb = cube[0]*29.0*1.0e9/48.0

print cube_ppb

fig= plt.figure(figsize=(15, 8))

plt.subplot(3,4,1)
plt.title('O3 Jan 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[0], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,2)
plt.title('O3 Feb 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[1], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,3)
plt.title('O3 Mar 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[2], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,4)
plt.title('O3 Apr 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[3], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,5)
plt.title('O3 May 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[4], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,6)
plt.title('O3 Jun 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[5], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,7)
plt.title('O3 Jul 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[6], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,8)
plt.title('O3 Aug 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[7], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,9)
plt.title('O3 Sep 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[8], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,10)
plt.title('O3 Oct 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[9], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,11)
plt.title('O3 Nov 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[10], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,12)
plt.title('O3 Dec 2014',  fontsize=5)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
iplt.contourf(cube_ppb[11], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
cb1.set_label('ppb')


plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.87, top=0.9, hspace=0.2, wspace=0.01)
#plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/map/o3_monthly_2014.png', dpi=600, transparent=True)

plt.show()

