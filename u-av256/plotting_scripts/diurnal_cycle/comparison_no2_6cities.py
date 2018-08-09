# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:19:23 2018

@author: s1731217
"""

# =============================================================================
# NO2 6 cities Comparison
# =============================================================================
import matplotlib.pyplot as plt
import xlrd
import iris
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from scipy.interpolate import spline  
import sys
import iris.coord_categorisation

filename  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/no2.pp'  # no2
filename2 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/no2.pp'  # no2 (nudging)

# =============================================================================
# no2
# =============================================================================
cube = iris.load(filename)
#cube_unit = cube[0]*29.0*1.0e9/46.0
#air density is not the same 
cube_unit_beijing      = cube[0]*1.185*1.0e9
cube_unit_shijiazhuang = cube[0]*1.181*1.0e9
cube_unit_shanghai     = cube[0]*1.185*1.0e9
cube_unit_nanjing      = cube[0]*1.185*1.0e9
cube_unit_guangzhou    = cube[0]*1.169*1.0e9
cube_unit_hk           = cube[0]*1.169*1.0e9

cube_beijing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_hk, [('latitude', 22.33), ('longitude', 114.19)])

cube2 = iris.load(filename2)

cube_unit_beijing_nudging      = cube2[0]*1.185*1.0e9
cube_unit_shijiazhuang_nudging = cube2[0]*1.181*1.0e9
cube_unit_shanghai_nudging     = cube2[0]*1.185*1.0e9
cube_unit_nanjing_nudging      = cube2[0]*1.185*1.0e9
cube_unit_guangzhou_nudging    = cube2[0]*1.169*1.0e9
cube_unit_hk_nudging           = cube2[0]*1.169*1.0e9

cube_beijing_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_beijing_nudging, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_shijiazhuang_nudging, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_shanghai_nudging, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_nanjing_nudging, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_guangzhou_nudging, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_no2_nudging = iris.analysis.interpolate.extract_nearest_neighbour(cube_unit_hk_nudging, [('latitude', 22.33), ('longitude', 114.19)])

# =============================================================================
# Mean of hour
# =============================================================================
iris.FUTURE.cell_datetime_objects = True
# For 7.5h time difference, e.g. hour1(hour1.5)>> hour9 in China
#hour_24 = iris.Constraint(time=lambda cell: cell.point.hour == 16)
#hour_1 = iris.Constraint(time=lambda cell: cell.point.hour == 17)
#hour_2 = iris.Constraint(time=lambda cell: cell.point.hour == 18)
#hour_3 = iris.Constraint(time=lambda cell: cell.point.hour == 19)
#hour_4 = iris.Constraint(time=lambda cell: cell.point.hour == 20)
#hour_5 = iris.Constraint(time=lambda cell: cell.point.hour == 21)
#hour_6 = iris.Constraint(time=lambda cell: cell.point.hour == 22)
#hour_7 = iris.Constraint(time=lambda cell: cell.point.hour == 23)
#hour_8 = iris.Constraint(time=lambda cell: cell.point.hour == 0)  # here must be 0 instead of 24
#hour_9 = iris.Constraint(time=lambda cell: cell.point.hour == 1)
#hour_10 = iris.Constraint(time=lambda cell: cell.point.hour == 2)
#hour_11 = iris.Constraint(time=lambda cell: cell.point.hour == 3)
#hour_12 = iris.Constraint(time=lambda cell: cell.point.hour == 4)
#hour_13 = iris.Constraint(time=lambda cell: cell.point.hour == 5)
#hour_14 = iris.Constraint(time=lambda cell: cell.point.hour == 6)
#hour_15 = iris.Constraint(time=lambda cell: cell.point.hour == 7)
#hour_16 = iris.Constraint(time=lambda cell: cell.point.hour == 8)
#hour_17 = iris.Constraint(time=lambda cell: cell.point.hour == 9)
#hour_18 = iris.Constraint(time=lambda cell: cell.point.hour == 10)
#hour_19 = iris.Constraint(time=lambda cell: cell.point.hour == 11)
#hour_20 = iris.Constraint(time=lambda cell: cell.point.hour == 12)
#hour_21 = iris.Constraint(time=lambda cell: cell.point.hour == 13)
#hour_22 = iris.Constraint(time=lambda cell: cell.point.hour == 14)
#hour_23 = iris.Constraint(time=lambda cell: cell.point.hour == 15)

# For 8.5h time difference, e.g. hour1(hour1.5)>> hour10 in China
hour_1 = iris.Constraint(time=lambda cell: cell.point.hour == 16)
hour_2 = iris.Constraint(time=lambda cell: cell.point.hour == 17)
hour_3 = iris.Constraint(time=lambda cell: cell.point.hour == 18)
hour_4 = iris.Constraint(time=lambda cell: cell.point.hour == 19)
hour_5 = iris.Constraint(time=lambda cell: cell.point.hour == 20)
hour_6 = iris.Constraint(time=lambda cell: cell.point.hour == 21)
hour_7 = iris.Constraint(time=lambda cell: cell.point.hour == 22)
hour_8 = iris.Constraint(time=lambda cell: cell.point.hour == 23)
hour_9 = iris.Constraint(time=lambda cell: cell.point.hour == 0)  # here must be 0 instead of 24
hour_10 = iris.Constraint(time=lambda cell: cell.point.hour == 1)
hour_11 = iris.Constraint(time=lambda cell: cell.point.hour == 2)
hour_12 = iris.Constraint(time=lambda cell: cell.point.hour == 3)
hour_13 = iris.Constraint(time=lambda cell: cell.point.hour == 4)
hour_14 = iris.Constraint(time=lambda cell: cell.point.hour == 5)
hour_15 = iris.Constraint(time=lambda cell: cell.point.hour == 6)
hour_16 = iris.Constraint(time=lambda cell: cell.point.hour == 7)
hour_17 = iris.Constraint(time=lambda cell: cell.point.hour == 8)
hour_18 = iris.Constraint(time=lambda cell: cell.point.hour == 9)
hour_19 = iris.Constraint(time=lambda cell: cell.point.hour == 10)
hour_20 = iris.Constraint(time=lambda cell: cell.point.hour == 11)
hour_21 = iris.Constraint(time=lambda cell: cell.point.hour == 12)
hour_22 = iris.Constraint(time=lambda cell: cell.point.hour == 13)
hour_23 = iris.Constraint(time=lambda cell: cell.point.hour == 14)
hour_24 = iris.Constraint(time=lambda cell: cell.point.hour == 15)



cube_city_list_no2 = [cube_beijing_no2,  cube_shijiazhuang_no2, cube_shanghai_no2, cube_nanjing_no2, cube_guangzhou_no2, cube_hongkong_no2]
cube_city_list_no2_nudging = [cube_beijing_no2_nudging,  cube_shijiazhuang_no2_nudging, cube_shanghai_no2_nudging, cube_nanjing_no2_nudging, cube_guangzhou_no2_nudging, cube_hongkong_no2_nudging]
# =============================================================================
# PM10 & PM1 hour mean calculating
# =============================================================================
hour = [hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23, hour_24]
def value_get(cube_city_list):
    y_city_list = []
#    for i in np.arange(0,7):
    indice1 = 0
    for i in np.arange(0,6):
        cube_city = cube_city_list[i]  # for each city
        cube_hour_city = []
        indice1 += 1
        print 'indice1:',  indice1
        indice2 = 0
        for i in np.arange(0,24):
            cube_hour_city.append(cube_city.extract(hour[i])) # adding values of each hour to cube_hour_city
#            print cube_city.extract(hour[i])
#            print cube_hour_city[i]
            indice2 += 1
            print 'indice2:', indice2
        hour_mean_city = []
        for i in np.arange(0,24):
            tmp = cube_hour_city[i].collapsed('time', iris.analysis.MEAN)
            hour_mean_city.append(tmp)  # calculating the mean values of each hour
        y_city = []
        for i in np.arange(0,24):
            y_city.append(hour_mean_city[i].data) # adding values into y_city array
        y_city_list.append(y_city) # adding mean values of each city into y_city_list
    return(y_city_list)  # return y_city_list

# =============================================================================
# storing y_city_list values
# =============================================================================

NO2_values = value_get(cube_city_list_no2)
NO2_Beijing = NO2_values[0]
NO2_Shijiazhuang = NO2_values[1]
NO2_Shanghai = NO2_values[2]
NO2_Nanjing = NO2_values[3]
NO2_Guangzhou = NO2_values[4]
NO2_Hongkong = NO2_values[5]

NO2_values_nudging = value_get(cube_city_list_no2_nudging)
NO2_Beijing_nudging = NO2_values_nudging[0]
NO2_Shijiazhuang_nudging = NO2_values_nudging[1]
NO2_Shanghai_nudging = NO2_values_nudging[2]
NO2_Nanjing_nudging = NO2_values_nudging[3]
NO2_Guangzhou_nudging = NO2_values_nudging[4]
NO2_Hongkong_nudging = NO2_values_nudging[5]



#print value_get(cube_city_list_no2)
# =============================================================================
# loading excel data
# =============================================================================
data1 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Beijing/Average_Beijing_NO2.xlsx')
data2 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shijiazhuang/Average_Shijiazhuang_NO2.xlsx')
data3 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shanghai/Average_Shanghai_NO2.xlsx')
data4 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Nanjing/Average_Nanjing_NO2.xlsx')
data5 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Guangzhou/Average_Guangzhou_NO2.xlsx')
data6 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Hongkong/Average_Hongkong_NO2.xlsx')

table1 = data1.sheet_by_name('AVERAGE')
table2 = data2.sheet_by_name('AVERAGE')
table3 = data3.sheet_by_name('AVERAGE')
table4 = data4.sheet_by_name('AVERAGE')
table5 = data5.sheet_by_name('AVERAGE')
table6 = data6.sheet_by_name('AVERAGE')

no2_bei_m = table1.col_values(7)[1:]    # col 1 for old missed time list
no2_shi_m = table2.col_values(6)[1:] 
no2_shang_m = table3.col_values(7)[1:] 
no2_nan_m = table4.col_values(9)[1:] 
no2_guang_m = table5.col_values(10)[1:] 
no2_h_m = table6.col_values(5)[1:] 
# =============================================================================
# 6 sites PM10
# =============================================================================
no2_bei1 = table1.col_values(0)[1:]
no2_bei2 = table1.col_values(1)[1:]
no2_bei3 = table1.col_values(2)[1:]
no2_bei4 = table1.col_values(3)[1:]
no2_bei5 = table1.col_values(4)[1:]
no2_bei6 = table1.col_values(5)[1:]
no2_bei7 = table1.col_values(6)[1:]

no2_shi1 = table2.col_values(0)[1:]
no2_shi2 = table2.col_values(1)[1:]
no2_shi3 = table2.col_values(2)[1:]
no2_shi4 = table2.col_values(3)[1:]
no2_shi5 = table2.col_values(4)[1:]
no2_shi6 = table2.col_values(5)[1:]

no2_shang1 = table3.col_values(0)[1:]
no2_shang2 = table3.col_values(1)[1:]
no2_shang3 = table3.col_values(2)[1:]
no2_shang4 = table3.col_values(3)[1:]
no2_shang5 = table3.col_values(4)[1:]
no2_shang6 = table3.col_values(5)[1:]
no2_shang7 = table3.col_values(6)[1:]

no2_nan1 = table4.col_values(0)[1:]
no2_nan2 = table4.col_values(1)[1:]
no2_nan3 = table4.col_values(2)[1:]
no2_nan4 = table4.col_values(3)[1:]
no2_nan5 = table4.col_values(4)[1:]
no2_nan6 = table4.col_values(5)[1:]
no2_nan7 = table4.col_values(6)[1:]
no2_nan8 = table4.col_values(7)[1:]

no2_guang1 = table5.col_values(0)[1:]
no2_guang2 = table5.col_values(1)[1:]
no2_guang3 = table5.col_values(2)[1:]
no2_guang4 = table5.col_values(3)[1:]
no2_guang5 = table5.col_values(4)[1:]
no2_guang6 = table5.col_values(5)[1:]
no2_guang7 = table5.col_values(6)[1:]
no2_guang8 = table5.col_values(7)[1:]
no2_guang9 = table5.col_values(8)[1:]
no2_guang10 = table5.col_values(9)[1:]


no2_h1 = table6.col_values(0)[1:]
no2_h2 = table6.col_values(1)[1:]
no2_h3 = table6.col_values(2)[1:]
no2_h4 = table6.col_values(3)[1:]
no2_h5 = table6.col_values(4)[1:]


# =============================================================================
# Plotting
# =============================================================================
plt.figure(figsize=(24, 8))

#beijing
pic = plt.subplot(2, 3, 1)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
#beijing = pic.plot(x, value_get(cube_city_list_no2)[0], linewidth=4, label = 'Beijing_NO2', color = 'k')
#beijing2 = pic.plot(x, value_get(cube_city_list_no)[0], linewidth=4, label = 'Beijing_NO', color = 'sienna')
beijing = pic.plot(x, NO2_Beijing, linewidth=4, label = 'Beijing_NO2', color = 'k')
beijing_nudging = pic.plot(x, NO2_Beijing_nudging, linewidth=4, label = 'Beijing_NO2_nudging', color = 'sienna')

obs_bei_no2 = pic.plot(x, no2_bei_m, linewidth=4, label = 'Obs_NO2 (7 sites mean)', color ='r')

lbei1 = pic.plot(x, no2_bei1, linewidth=1,  label = '7 sites NO2', color ='lightcoral')
lbei2 = pic.plot(x, no2_bei2, linewidth=1,  color ='lightcoral')
lbei3 = pic.plot(x, no2_bei3, linewidth=1,  color ='lightcoral')
lbei4 = pic.plot(x, no2_bei4, linewidth=1,  color ='lightcoral')
lbei5 = pic.plot(x, no2_bei5, linewidth=1,  color ='lightcoral')
lbei6 = pic.plot(x, no2_bei6, linewidth=1,  color ='lightcoral')
lbei7 = pic.plot(x, no2_bei7, linewidth=1,  color ='lightcoral')

#shijiazhuang = pic.plot(x, value_get(cube_city_list_pm10)[1], linewidth=2, label = 'Shijiazhuang')
#shanghai = pic.plot(x, value_get(cube_city_list_pm10)[2], linewidth=2, label = 'Shanghai')
#nanjing = pic.plot(x, value_get(cube_city_list_pm10)[3], linewidth=2, label = 'Nanjing')
#guangzhou = pic.plot(x, value_get(cube_city_list_pm10)[4], linewidth=2, label = 'Guangzhou')
#shenzhen = pic.plot(x, value_get(cube_city_list_pm10)[5], linewidth=2, label = 'Shenzhen')
#hongkong = pic.plot(x, value_get(cube_city_list_pm10)[6], linewidth=2, label = 'Hongkong')

ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of NO2 in Beijing (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)

# shijiazhuang
pic = plt.subplot(2, 3, 2)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
shijiazhuang = pic.plot(x, NO2_Shijiazhuang, linewidth=4, label = 'Shijiazhuang_NO2', color = 'k')
shijiazhuang_nudging = pic.plot(x, NO2_Shijiazhuang_nudging, linewidth=4, label = 'Shijiazhuang_NO2_nudging', color = 'sienna')

obs_shi_no2 = pic.plot(x, no2_shi_m, linewidth=4, label = 'Obs_NO2 (7 sites mean)', color ='r')

lshi1 = pic.plot(x, no2_shi1, linewidth=1,  label = '7 sites NO2', color ='lightcoral')
lshi2 = pic.plot(x, no2_shi2, linewidth=1,  color ='lightcoral')
lshi3 = pic.plot(x, no2_shi3, linewidth=1,  color ='lightcoral')
lshi4 = pic.plot(x, no2_shi4, linewidth=1,  color ='lightcoral')
lshi5 = pic.plot(x, no2_shi5, linewidth=1,  color ='lightcoral')
lshi6 = pic.plot(x, no2_shi6, linewidth=1,  color ='lightcoral')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of NO2 in Shijiazhuang (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)
    
 
# shanghai
pic = plt.subplot(2, 3, 3)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
shanghai = pic.plot(x, NO2_Shanghai, linewidth=4, label = 'Shanghai_NO2', color = 'k')
shanghai_nudging = pic.plot(x, NO2_Shanghai_nudging, linewidth=4, label = 'Shanghai_NO2_nudging', color = 'sienna')

obs_shang_no2 = pic.plot(x, no2_shang_m, linewidth=4, label = 'Obs_NO2 (7 sites mean)', color ='r')

lshang1 = pic.plot(x, no2_shang1, linewidth=1,  label = '7 sites NO2', color ='lightcoral')
lshang2 = pic.plot(x, no2_shang2, linewidth=1,  color ='lightcoral')
lshang3 = pic.plot(x, no2_shang3, linewidth=1,  color ='lightcoral')
lshang4 = pic.plot(x, no2_shang4, linewidth=1,  color ='lightcoral')
lshang5 = pic.plot(x, no2_shang5, linewidth=1,  color ='lightcoral')
lshang6 = pic.plot(x, no2_shang6, linewidth=1,  color ='lightcoral')
lshang7 = pic.plot(x, no2_shang7, linewidth=1,  color ='lightcoral')

ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of NO2 in Shanghai (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)
    
# nanjing
pic = plt.subplot(2, 3, 4)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
nanjing = pic.plot(x, NO2_Nanjing, linewidth=4, label = 'Modelled NO2', color = 'k')
nanjing_nudging = pic.plot(x, NO2_Nanjing_nudging, linewidth=4, label = 'Modelled NO2 (nudging)', color = 'sienna')

obs_nan_no2 = pic.plot(x, no2_nan_m, linewidth=4, label = 'Obs_NO2 June', color ='r')

lnan1 = pic.plot(x, no2_nan1, linewidth=1,  label = 'NO2 of a single location', color ='lightcoral')
lnan2 = pic.plot(x, no2_nan2, linewidth=1,  color ='lightcoral')
lnan3 = pic.plot(x, no2_nan3, linewidth=1,  color ='lightcoral')
lnan4 = pic.plot(x, no2_nan4, linewidth=1,  color ='lightcoral')
lnan5 = pic.plot(x, no2_nan5, linewidth=1,  color ='lightcoral')
lnan6 = pic.plot(x, no2_nan6, linewidth=1,  color ='lightcoral')
lnan7 = pic.plot(x, no2_nan7, linewidth=1,  color ='lightcoral')
lnan8 = pic.plot(x, no2_nan8, linewidth=1,  color ='lightcoral')

ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)


plt.title('Comparisons of NO2 in Nanjing (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
plt.legend(bbox_to_anchor=(0.7, -0.09, 2.5, -0.09),  ncol= 4, mode="expand")   # bbox_to_anchor=(x0, y0, x, y)
#ax.ax = gca()
#ax.set_position([0,0,0.8,1]) (left, bottom, width, height)
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
# guangzhou
pic = plt.subplot(2, 3, 5)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
guangzhou = pic.plot(x, NO2_Guangzhou, linewidth=4, label = 'Guangzhou_NO2', color = 'k')
guangzhou_nudging = pic.plot(x, NO2_Guangzhou_nudging, linewidth=4, label = 'Guangzhou_NO2_nudging', color = 'sienna')

obs_guang_no2 = pic.plot(x, no2_guang_m, linewidth=4, label = 'Obs_NO2 (7 sites mean)', color ='r')

lguang1 = pic.plot(x, no2_guang1, linewidth=1,  label = '7 sites NO2', color ='lightcoral')
lguang2 = pic.plot(x, no2_guang2, linewidth=1,  color ='lightcoral')
lguang3 = pic.plot(x, no2_guang3, linewidth=1,  color ='lightcoral')
lguang4 = pic.plot(x, no2_guang4, linewidth=1,  color ='lightcoral')
lguang5 = pic.plot(x, no2_guang5, linewidth=1,  color ='lightcoral')
lguang6 = pic.plot(x, no2_guang6, linewidth=1,  color ='lightcoral')
lguang7 = pic.plot(x, no2_guang7, linewidth=1,  color ='lightcoral')
lguang8 = pic.plot(x, no2_guang8, linewidth=1,  color ='lightcoral')
lguang9 = pic.plot(x, no2_guang9, linewidth=1,  color ='lightcoral')
lguang10 = pic.plot(x, no2_guang10, linewidth=1,  color ='lightcoral')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of NO2 in Guangzhou (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)
    
# hk
pic = plt.subplot(2, 3, 6)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.5 ] 
pic.set_position(pos2)

x = np.arange(1,25)
hk = pic.plot(x, NO2_Hongkong, linewidth=4, label = 'Hong Kong_NO2', color = 'k')
hk_nudging = pic.plot(x, NO2_Hongkong_nudging, linewidth=4, label = 'Hong Kong_NO2_nudging', color = 'sienna')

obs_h_no2 = pic.plot(x, no2_h_m, linewidth=4, label = 'Obs_NO2 (7 sites mean)', color ='r')

lh1 = pic.plot(x, no2_h1, linewidth=1,  label = '7 sites NO2', color ='lightcoral')
lh2 = pic.plot(x, no2_h2, linewidth=1,  color ='lightcoral')
lh3 = pic.plot(x, no2_h3, linewidth=1,  color ='lightcoral')
lh4 = pic.plot(x, no2_h4, linewidth=1,  color ='lightcoral')
lh5 = pic.plot(x, no2_h5, linewidth=1,  color ='lightcoral')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of NO2 in Hong Kong (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' NO2  (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)
    

    
    
plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.15, right=0.9, top=0.9, hspace=0.2, wspace=0.4)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/nudging_test_comparison_no2(34996)_6cities.png', dpi=600, transparent=True)
plt.show()


