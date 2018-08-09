import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

import iris
import iris.plot as iplt
import iris.quickplot as qplt

no2_stash = ['m01s34i996']

filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/apm.pp/*'
            
stash_constraint = iris.AttributeConstraint(STASH=no2_stash[0])
latitude_constraint = iris.Constraint(coord_values={'latitude':lambda cell: 17.5 < cell < 45})
longitude_constraint = iris.Constraint(coord_values={'longitude':lambda cell: 107.5 < cell < 125})
cube = iris.load(filename, stash_constraint).extract(latitude_constraint & longitude_constraint)

no2_ppb = cube[0]*29.0*1.0e9/46.0

fig= plt.figure(figsize=(15, 8))

plt.subplot(3,4,1)
plt.title('NO2 Jan 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[0], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,2)
plt.title('NO2 Feb 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[1], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,3)
plt.title('NO2 Mar 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[2], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,4)
plt.title('NO2 Apr 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[3], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,5)
plt.title('NO2 May 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[4], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,6)
plt.title('NO2 Jun 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[5], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,7)
plt.title('NO2 Jul 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[6], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,8)
plt.title('NO2 Aug 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[7], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,9)
plt.title('NO2 Sep 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[8], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,10)
plt.title('NO2 Oct 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[9], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,11)
plt.title('NO2 Nov 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[10], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')

plt.subplot(3,4,12)
plt.title('NO2 Dec 2014',  fontsize=5)
tick_levels = [0.1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
iplt.contourf(no2_ppb[11], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
m.readshapefile('bou2_4p', 'states', drawbounds=True)   
m.readshapefile('bou2_4l', 'states', drawbounds=True)
cb1=plt.colorbar(orientation='vertical', extend='both')
cb1.ax.set_yticklabels([0.1, 10, 20, 30, 40, 50, 60, 70], fontsize=8)
cb1.set_label('ppb')


plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.87, top=0.9, hspace=0.2, wspace=0.01)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/map/no2_monthly_2014.png', dpi=600, transparent=True)

plt.show()
