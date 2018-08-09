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

#ozone_stash = ['m01s34i001']
#
#filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/apm.pp/*'
#
#stash_constraint = iris.AttributeConstraint(STASH=ozone_stash[0])
#latitude_constraint = iris.Constraint(coord_values={'latitude':lambda cell: 17.5 < cell < 45})
#longitude_constraint = iris.Constraint(coord_values={'longitude':lambda cell: 107.5 < cell < 125})
#cube = iris.load(filename, stash_constraint).extract(latitude_constraint & longitude_constraint)
#cube = iris.load(filename).extract(latitude_constraint & longitude_constraint)

#print cube
#
#print cube[0]
#
#cube_ppb = cube[0]*29.0*1.0e9/48.0
#
#print cube_ppb

fig= plt.figure(figsize=(15, 8), facecolor='white')

plt.subplot(1,1,1)
plt.title('Measurement sites in NCP, YRD, PRD',  fontsize=15)
tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[0], tick_levels, cmap='jet', norm=LogNorm())
m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states_1', drawbounds=True)   # Hong Kong
m.readshapefile('HKG_adm1', 'states_1', drawbounds=True) 
m.readshapefile('bou2_4l', 'states_2', drawbounds=True)  # sea coast line 
m.readshapefile('CHN_adm2', 'city', drawbounds=False) # only read city shapefiles 
#m.fillcontinents(color = 'coral')
m.drawlsmask(land_color = 'whitesmoke', ocean_color='cornflowerblue', lakes=False, resolution='h', grid=1.25)


# =============================================================================
# Measurement sites mapping
import pandas as pd
import xlrd

data = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/measurement_sites_mapping/measurement_sites.xlsx')

table1, table2, table3    = data.sheet_by_name('Beijing'),data.sheet_by_name('Beijing2'),data.sheet_by_name('Beijing3')
table4, table5, table6    = data.sheet_by_name('Shijiazhuang'),data.sheet_by_name('Shijiazhuang2'),data.sheet_by_name('Shijiazhuang3')
table7, table8, table9    = data.sheet_by_name('Shanghai'),data.sheet_by_name('Shanghai2'),data.sheet_by_name('Shanghai3')
table10, table11, table12 = data.sheet_by_name('Nanjing'),data.sheet_by_name('Nanjing2'),data.sheet_by_name('Nanjing3')
table13, table14, table15 = data.sheet_by_name('Guangzhou'),data.sheet_by_name('Guangzhou2'),data.sheet_by_name('Guangzhou3')
table16                   = data.sheet_by_name('Hong Kong')  # measurement in HK, grid are all the same 

# Red dots: measurement sites included 
lon_bj, lat_bj   = table1.col_values(3)[1:], table1.col_values(4)[1:]
lon_sjz, lat_sjz = table4.col_values(3)[1:], table4.col_values(4)[1:]
lon_sh, lat_sh   = table7.col_values(3)[1:], table7.col_values(4)[1:]
lon_nj, lat_nj   = table10.col_values(3)[1:], table10.col_values(4)[1:]
lon_gz, lat_gz   = table13.col_values(3)[1:], table13.col_values(4)[1:]
lon_hk, lat_hk   = table16.col_values(3)[1:], table16.col_values(4)[1:]

# Green '+': measurement sites in the city
lon_bj2, lat_bj2   = table2.col_values(3)[1:], table2.col_values(4)[1:]
lon_sjz2, lat_sjz2 = table5.col_values(3)[1:], table5.col_values(4)[1:]
lon_sh2, lat_sh2   = table8.col_values(3)[1:], table8.col_values(4)[1:]
lon_nj2, lat_nj2   = table11.col_values(3)[1:], table11.col_values(4)[1:]
lon_gz2, lat_gz2   = table14.col_values(3)[1:], table14.col_values(4)[1:]

# Blue dots: measurement sites in the grid
lon_bj3, lat_bj3   = table3.col_values(3)[1:], table3.col_values(4)[1:]
lon_sjz3, lat_sjz3 = table6.col_values(3)[1:], table6.col_values(4)[1:]
lon_sh3, lat_sh3   = table9.col_values(3)[1:], table9.col_values(4)[1:]
lon_nj3, lat_nj3   = table12.col_values(3)[1:], table12.col_values(4)[1:]
lon_gz3, lat_gz3   = table15.col_values(3)[1:], table15.col_values(4)[1:]

lon_red_dots   = np.concatenate((lon_bj, lon_sjz, lon_sh, lon_nj, lon_gz, lon_hk)) 
lat_red_dots   = np.concatenate((lat_bj, lat_sjz, lat_sh, lat_nj, lat_gz, lat_hk)) 
lon_green_plus = np.concatenate((lon_bj2, lon_sjz2, lon_sh2, lon_nj2, lon_gz2, lon_hk)) 
lat_green_plus = np.concatenate((lat_bj2, lat_sjz2, lat_sh2, lat_nj2, lat_gz2, lat_hk)) 
lon_blue_dots  = np.concatenate((lon_bj3, lon_sjz3, lon_sh3, lon_nj3, lon_gz3, lon_hk)) 
lat_blue_dots  = np.concatenate((lat_bj3, lat_sjz3, lat_sh3, lat_nj3, lat_gz3, lat_hk)) 

x_red_dots, y_red_dots     = m(lon_red_dots, lat_red_dots)
x_green_plus, y_green_plus = m(lon_green_plus, lat_green_plus)
x_blue_dots, y_blue_dots   = m(lon_blue_dots, lat_blue_dots)


m.plot(x_green_plus, y_green_plus,  'go', markersize=7, label='Measurement sites only in the city')
m.plot(x_blue_dots, y_blue_dots,  'bo', markersize=7, label='Measurement sites only in the grid')
m.plot(x_red_dots, y_red_dots,  'ro', markersize=7, label='Measurement sites in the both city and grid')
# =============================================================================
# =============================================================================
# Text box: BTH, YRD, PRD
# =============================================================================
# BTH
lon_BTH = 114.5
lat_BTH = 42.7
x, y = m(lon_BTH, lat_BTH)
plt.text(x, y, 'BTH',fontsize=18,fontweight='bold', ha='left',va='bottom',color='orchid',
         bbox=dict(facecolor='b', alpha=0.1))

# YRD
lon_YRD = 116.6
lat_YRD = 35.3
x, y = m(lon_YRD, lat_YRD)
plt.text(x, y, 'YRD',fontsize=18,fontweight='bold', ha='left',va='bottom',color='orchid',
         bbox=dict(facecolor='b', alpha=0.1))

# PRD
lon_PRD = 111.7
lat_PRD = 26
x, y = m(lon_PRD, lat_PRD)
plt.text(x, y, 'PRD',fontsize=18,fontweight='bold', ha='left',va='bottom',color='orchid',
         bbox=dict(facecolor='b', alpha=0.1))
# =============================================================================

# =============================================================================
# Grid box boundary; lat_bbj: boundary_beijing
# =============================================================================
def draw_screen_poly(lats, lons, m):
    x, y = m(lons, lats )
    xy = zip(x,y)
    poly = Polygon( xy, facecolor='red', alpha=0.4 )
    plt.gca().add_patch(poly)
    
lat_bbj = [ 38.75, 40, 40, 38.75 ] # anti-clock wise and start from left bottom
lon_bbj = [ 116.25, 116.25, 118.125, 118.125 ]

lat_bsjz = [ 37.5, 38.75, 38.75, 37.5 ]
lon_bsjz = [ 114.375, 114.375, 116.25, 116.25 ]

lat_bsh = [ 30, 31.25, 31.25, 30 ] 
lon_bsh = [ 120, 120, 121.875, 121.875 ]

lat_bnj = [ 31.25, 32.5, 32.5, 31.25 ] 
lon_bnj = [ 118.125, 118.125, 120, 120 ]

lat_bgz = [ 22.5, 23.75, 23.75, 22.5 ] 
lon_bgz = [ 112.5, 112.5, 114.375, 114.375 ]

lat_bhk = [ 21.25, 22.5, 22.5, 21.25 ] 
lon_bhk = [ 112.5, 112.5, 114.375, 114.375 ]

draw_screen_poly(lat_bbj, lon_bbj, m )
draw_screen_poly(lat_bsjz, lon_bsjz, m )
draw_screen_poly(lat_bsh, lon_bsh, m )
draw_screen_poly(lat_bnj, lon_bnj, m )
draw_screen_poly(lat_bgz, lon_bgz, m )
draw_screen_poly(lat_bhk, lon_bhk, m )
# =============================================================================

#ax = plt.gca()
#for nshape, seg in enumerate(m.states):
#    poly = Polygon(seg, facecolor='r')
#    ax.add_patch(poly)

#for info, shape in zip(m.states_info, m.states):
#    if info['NAME_1'] =='Henan':
#        x, y = zip(*shape)
#        m.plot(x, y, marker = None, color= 'm')
ax = plt.gca()     
patches = []

# =============================================================================
# One way to fill provinces * zorder = 2 (this patch cannot be overlaid), should be 1
# =============================================================================
for info, shape in zip(m.states_info, m.states):
     if info['NAME_1'] =='Beijing':
         patches.append(Polygon(np.array(shape), True))
     if info['NAME_1'] =='Tianjin':
         patches.append(Polygon(np.array(shape), True))  
     if info['NAME_1'] =='Hebei':
         patches.append(Polygon(np.array(shape), True))
     if info['NAME_1'] =='Shanghai':
         patches.append(Polygon(np.array(shape), True))
     if info['NAME_1'] =='Jiangsu':
         patches.append(Polygon(np.array(shape), True))
     if info['NAME_1'] =='Zhejiang':
         patches.append(Polygon(np.array(shape), True))
     if info['NAME_1'] =='Guangdong':
         patches.append(Polygon(np.array(shape), True))


         
ax.add_collection(PatchCollection(patches, facecolor = 'gold', edgecolor = 'k', linewidths = 1, zorder = 1))
# =============================================================================

# =============================================================================
# Another way to fill provinces
# =============================================================================
# for info, shp in zip(m.states_info, m.states):
#     proid = info['NAME_1'] 
#     if proid == 'Hebei':
#        poly = Polygon(shp,facecolor='gold',edgecolor='k', lw = 1) 
#        ax.add_patch(poly)
# =============================================================================

# =============================================================================
# Draw city boundaries and filling them in the province (6 cities)
# =============================================================================
#patches_city = []
#for info, shape in zip(m.city_info, m.city):
#    if info['NAME_1'] == 'Hebei':
#        x, y = zip(*shape) 
#        m.plot(x, y, marker=None,color='m')
#    if info['NAME_1'] == 'Jiangsu':
#        x, y = zip(*shape) 
#        m.plot(x, y, marker=None,color='m')
#    if info['NAME_1'] == 'Guangdong':
#        x, y = zip(*shape) 
#        m.plot(x, y, marker=None,color='m')
#    if info['NAME_2'] =='Nanjing':
#        patches_city.append(Polygon(np.array(shape), True))
#        
#ax.add_collection(PatchCollection(patches_city, facecolor = 'orchid', edgecolor = 'k', linewidths = 1, zorder = 1))
# =============================================================================

# =============================================================================
# Draw city boundaries and filling them in the province (6 cities)
# =============================================================================
ax = plt.gca() 
patches_city = []
for info, shape in zip(m.city_info, m.city):
    if info['NAME_1'] == 'Hebei':
        x, y = zip(*shape) 
        m.plot(x, y, marker=None,color='m')
    if info['NAME_1'] == 'Jiangsu':
        x, y = zip(*shape) 
        m.plot(x, y, marker=None,color='m')
    if info['NAME_1'] == 'Guangdong':
        x, y = zip(*shape) 
        m.plot(x, y, marker=None,color='m')
    if info['NAME_1'] == 'Zhejiang':
        x, y = zip(*shape)
        m.plot(x, y, marker=None,color='m')
    if info['NAME_2'] =='Beijing':
        patches_city.append(Polygon(np.array(shape), True))
    if info['NAME_2'] =='Shijiazhuang':
        patches_city.append(Polygon(np.array(shape), True))
    if info['NAME_2'] =='Shanghai':
        patches_city.append(Polygon(np.array(shape), True))  
    if info['NAME_2'] =='Nanjing':
        patches_city.append(Polygon(np.array(shape), True))
    if info['NAME_2'] =='Guangzhou':
        patches_city.append(Polygon(np.array(shape), True))
    
for info, shape in zip(m.states_1_info, m.states_1):
     if info['NAME_0'] =='Hong Kong':
         patches_city.append(Polygon(np.array(shape), True))
        
ax.add_collection(PatchCollection(patches_city, facecolor = 'deepskyblue', edgecolor = 'k', linewidths = 1, zorder = 1))
# =============================================================================

# =============================================================================
# Annotation arrows to point out 6 cities
# =============================================================================
# Example: x, y 
#x2, y2 = (-90, 10)
#x3, y3 = (30, 10) # for Shanghai 
#x4, y4 = (-150, 20) # for Guangzhou and Hong K
    
lat_abj, lon_abj   = m(116.41, 39.9)
lat_asjz, lon_asjz = m(114.51, 38.04)
lat_ash, lon_ash   = m(121.47, 31.23)
lat_anj, lon_anj   = m(118.80, 32.06)
lat_agz, lon_agz   = m(113.26, 23.13)
lat_ahk, lon_ahk   = m(114.19, 22.33)

plt.annotate('Beijing', xy=(lat_abj, lon_abj),  xycoords='data',
                xytext=(-130, 20), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Shijiazhuang', xy=(lat_asjz, lon_asjz),  xycoords='data',
                xytext=(-120, 10), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Shanghai', xy=(lat_ash, lon_ash),  xycoords='data',
                xytext=(40, 10), textcoords='offset points',
                color='darkorange',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Nanjing', xy=(lat_anj, lon_anj),  xycoords='data',
                xytext=(-90, 10), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Guangzhou', xy=(lat_agz, lon_agz),  xycoords='data',
                xytext=(-150, 20), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )

plt.annotate('Hong Kong', xy=(lat_ahk, lon_ahk),  xycoords='data',
                xytext=(-180, 20), textcoords='offset points',
                color='cornflowerblue',
                arrowprops=dict(arrowstyle="fancy", color='darkorange')
                )
    

# =============================================================================
#plt.legend(bbox_to_anchor=(0.03, -0.09, 0.9, -0.09),  ncol= 4, mode="expand") 
#plt.legend(['sites'], loc='best')
plt.legend(loc = 4)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')

#plt.subplot(3,4,2)
#plt.title('O3 Feb 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[1], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,3)
#plt.title('O3 Mar 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[2], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,4)
#plt.title('O3 Apr 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[3], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,5)
#plt.title('O3 May 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[4], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,6)
#plt.title('O3 Jun 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[5], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,7)
#plt.title('O3 Jul 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[6], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,8)
#plt.title('O3 Aug 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[7], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,9)
#plt.title('O3 Sep 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[8], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,10)
#plt.title('O3 Oct 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[9], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,11)
#plt.title('O3 Nov 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[10], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')
#
#plt.subplot(3,4,12)
#plt.title('O3 Dec 2014',  fontsize=5)
#tick_levels = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80]
#iplt.contourf(cube_ppb[11], tick_levels, cmap='jet', norm=LogNorm())
#m = Basemap(llcrnrlon = 108, llcrnrlat = 18.2, urcrnrlon = 124.5, urcrnrlat = 44.3)
#m.readshapefile('CHN_adm1', 'states', drawbounds=True)
#m.readshapefile('bou2_4p', 'states', drawbounds=True)   
#m.readshapefile('bou2_4l', 'states', drawbounds=True)
#cb1=plt.colorbar(orientation='vertical', extend='both')
#cb1.ax.set_yticklabels([1, 10, 20, 30, 40, 60, 80], fontsize=8)
#cb1.set_label('ppb')


plt.tight_layout()
#plt.subplots_adjust(left=0.1, bottom=0.1, right=0.87, top=0.9, hspace=0.2, wspace=0.01)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/measurement_sites_mapping/measurement_sites_mapping.png', dpi=600, transparent=True)

plt.show()

