# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:19:23 2018

@author: s1731217
"""

# =============================================================================
# Comparisons of aerosol concentrations in NCP, YRD & PRD 
# =============================================================================
import matplotlib.pyplot as plt
import xlrd
import iris
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
#from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from scipy.interpolate import spline  
import sys
import iris.coord_categorisation

#filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/pm10.pp'  # PM10
#filename2 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/pm2.5.pp'   # PM1

filename = 'Z:/output_ukca/u-av256/dumped_pp_files/pm10.pp'
filename2 = 'Z:/output_ukca/u-av256/dumped_pp_files/pm2.5.pp'
# =============================================================================
# unit: ug/m3 PM10
# =============================================================================

cube = iris.load(filename)
#cube_unit = cube[0]*29.0*1.0e9/46.0
#air density is not the same 
#cube_unit_beijing = cube[0]*1.284*1.0e9
#cube_unit_shijiazhuang = cube[0]*1.275*1.0e9
#cube_unit_shanghai = cube[0]*1.248*1.0e9
#cube_unit_nanjing = cube[0]*1.252*1.0e9
#cube_unit_guangzhou = cube[0]*1.213*1.0e9
#cube_unit_hk = cube[0]*1.209*1.0e9

cube_beijing_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_pm10 = iris.analysis.interpolate.extract_nearest_neighbour(cube[0], [('latitude', 22.33), ('longitude', 114.19)])

# =============================================================================
# unit: ug/m3 PM1
# =============================================================================
cube2 = iris.load(filename2)

#cube_unit_beijing2 = cube2[0]*1.284*1.0e9
#cube_unit_shijiazhuang2 = cube2[0]*1.275*1.0e9
#cube_unit_shanghai2 = cube2[0]*1.248*1.0e9
#cube_unit_nanjing2 = cube2[0]*1.252*1.0e9
#cube_unit_guangzhou2 = cube2[0]*1.213*1.0e9
#cube_unit_hk2 = cube2[0]*1.209*1.0e9

cube_beijing_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_pm1 = iris.analysis.interpolate.extract_nearest_neighbour(cube2[0], [('latitude', 22.33), ('longitude', 114.19)])
# =============================================================================
# Mean of hour
# =============================================================================
iris.FUTURE.cell_datetime_objects = True
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

cube_city_list_pm10 = [cube_beijing_pm10,  cube_shijiazhuang_pm10, cube_shanghai_pm10, cube_nanjing_pm10, cube_guangzhou_pm10, cube_hongkong_pm10]
cube_city_list_pm1 = [cube_beijing_pm1, cube_shijiazhuang_pm1, cube_shanghai_pm1, cube_nanjing_pm1, cube_guangzhou_pm1, cube_hongkong_pm1]
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
        print('indice1:'),  indice1
        indice2 = 0
        for i in np.arange(0,24):
            cube_hour_city.append(cube_city.extract(hour[i])) # adding values of each hour to cube_hour_city
#            print cube_city.extract(hour[i])
#            print cube_hour_city[i]
            indice2 += 1
            print('indice2:'), indice2
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

PM10_values = value_get(cube_city_list_pm10)
PM10_Beijing = PM10_values[0]
PM10_Shijiazhuang = PM10_values[1]
PM10_Shanghai = PM10_values[2]
PM10_Nanjing = PM10_values[3]
PM10_Guangzhou = PM10_values[4]
PM10_Hongkong = PM10_values[5]

PM1_values = value_get(cube_city_list_pm1)
PM1_Beijing = PM1_values[0]
PM1_Shijiazhuang = PM1_values[1]
PM1_Shanghai = PM1_values[2]
PM1_Nanjing = PM1_values[3]
PM1_Guangzhou = PM1_values[4]
PM1_Hongkong = PM1_values[5]

# =============================================================================
# loading Excel data PM10
# =============================================================================
#data1_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Beijing/Average_Beijing_PM10.xlsx')
#data2_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shijiazhuang/Average_Shijiazhuang_PM10.xlsx')
#data3_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shanghai/Average_Shanghai_PM10.xlsx')
#data4_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Nanjing/Average_Nanjing_PM10.xlsx')
#data5_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Guangzhou/Average_Guangzhou_PM10.xlsx')
#data6_PM10 = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Hongkong/Average_Hongkong_PM10.xlsx')

data1_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Beijing/Average_Beijing_PM10.xlsx')
data2_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Shijiazhuang/Average_Shijiazhuang_PM10.xlsx')
data3_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Shanghai/Average_Shanghai_PM10.xlsx')
data4_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Nanjing/Average_Nanjing_PM10.xlsx')
data5_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Guangzhou/Average_Guangzhou_PM10.xlsx')
data6_PM10 = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Hongkong/Average_Hongkong_PM10.xlsx')

table1_PM10 = data1_PM10.sheet_by_name('AVERAGE')
table2_PM10 = data2_PM10.sheet_by_name('AVERAGE')
table3_PM10 = data3_PM10.sheet_by_name('AVERAGE')
table4_PM10 = data4_PM10.sheet_by_name('AVERAGE')
table5_PM10 = data5_PM10.sheet_by_name('AVERAGE')
table6_PM10 = data6_PM10.sheet_by_name('AVERAGE')

PM10_bei_m = table1_PM10.col_values(7)[1:]    # col 1 for old missed time list
PM10_shi_m = table2_PM10.col_values(6)[1:] 
PM10_shang_m = table3_PM10.col_values(7)[1:] 
PM10_nan_m = table4_PM10.col_values(9)[1:] 
PM10_guang_m = table5_PM10.col_values(10)[1:] 
PM10_h_m = table6_PM10.col_values(5)[1:] 
# =============================================================================
# 6 sites PM10
# =============================================================================
PM10_bei1 = table1_PM10.col_values(0)[1:]
PM10_bei2 = table1_PM10.col_values(1)[1:]
PM10_bei3 = table1_PM10.col_values(2)[1:]
PM10_bei4 = table1_PM10.col_values(3)[1:]
PM10_bei5 = table1_PM10.col_values(4)[1:]
PM10_bei6 = table1_PM10.col_values(5)[1:]
PM10_bei7 = table1_PM10.col_values(6)[1:]

PM10_shi1 = table2_PM10.col_values(0)[1:]
PM10_shi2 = table2_PM10.col_values(1)[1:]
PM10_shi3 = table2_PM10.col_values(2)[1:]
PM10_shi4 = table2_PM10.col_values(3)[1:]
PM10_shi5 = table2_PM10.col_values(4)[1:]
PM10_shi6 = table2_PM10.col_values(5)[1:]

PM10_shang1 = table3_PM10.col_values(0)[1:]
PM10_shang2 = table3_PM10.col_values(1)[1:]
PM10_shang3 = table3_PM10.col_values(2)[1:]
PM10_shang4 = table3_PM10.col_values(3)[1:]
PM10_shang5 = table3_PM10.col_values(4)[1:]
PM10_shang6 = table3_PM10.col_values(5)[1:]
PM10_shang7 = table3_PM10.col_values(6)[1:]

PM10_nan1 = table4_PM10.col_values(0)[1:]
PM10_nan2 = table4_PM10.col_values(1)[1:]
PM10_nan3 = table4_PM10.col_values(2)[1:]
PM10_nan4 = table4_PM10.col_values(3)[1:]
PM10_nan5 = table4_PM10.col_values(4)[1:]
PM10_nan6 = table4_PM10.col_values(5)[1:]
PM10_nan7 = table4_PM10.col_values(6)[1:]
PM10_nan8 = table4_PM10.col_values(7)[1:]

PM10_guang1 = table5_PM10.col_values(0)[1:]
PM10_guang2 = table5_PM10.col_values(1)[1:]
PM10_guang3 = table5_PM10.col_values(2)[1:]
PM10_guang4 = table5_PM10.col_values(3)[1:]
PM10_guang5 = table5_PM10.col_values(4)[1:]
PM10_guang6 = table5_PM10.col_values(5)[1:]
PM10_guang7 = table5_PM10.col_values(6)[1:]
PM10_guang8 = table5_PM10.col_values(7)[1:]
PM10_guang9 = table5_PM10.col_values(8)[1:]
PM10_guang10 = table5_PM10.col_values(9)[1:]


PM10_h1 = table6_PM10.col_values(0)[1:]
PM10_h2 = table6_PM10.col_values(1)[1:]
PM10_h3 = table6_PM10.col_values(2)[1:]
PM10_h4 = table6_PM10.col_values(3)[1:]
PM10_h5 = table6_PM10.col_values(4)[1:]

# =============================================================================
# loading Excel data PM2.5
# =============================================================================
#data1_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Beijing/Average_Beijing_PM2.5.xlsx')
#data2_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shijiazhuang/Average_Shijiazhuang_PM2.5.xlsx')
#data3_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Shanghai/Average_Shanghai_PM2.5.xlsx')
#data4_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Nanjing/Average_Nanjing_PM2.5.xlsx')
#data5_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Guangzhou/Average_Guangzhou_PM2.5.xlsx')
#data6_PM = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/obs_data/Hongkong/Average_Hongkong_PM2.5.xlsx')

data1_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Beijing/Average_Beijing_PM2.5.xlsx')
data2_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Shijiazhuang/Average_Shijiazhuang_PM2.5.xlsx')
data3_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Shanghai/Average_Shanghai_PM2.5.xlsx')
data4_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Nanjing/Average_Nanjing_PM2.5.xlsx')
data5_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Guangzhou/Average_Guangzhou_PM2.5.xlsx')
data6_PM = xlrd.open_workbook('Z:/output_ukca/u-av256/obs_data/Hongkong/Average_Hongkong_PM2.5.xlsx')

table1_PM = data1_PM.sheet_by_name('AVERAGE')
table2_PM = data2_PM.sheet_by_name('AVERAGE')
table3_PM = data3_PM.sheet_by_name('AVERAGE')
table4_PM = data4_PM.sheet_by_name('AVERAGE')
table5_PM = data5_PM.sheet_by_name('AVERAGE')
table6_PM = data6_PM.sheet_by_name('AVERAGE')

PM_bei_m = table1_PM.col_values(7)[1:]    # col 1 for old missed time list
PM_shi_m = table2_PM.col_values(6)[1:] 
PM_shang_m = table3_PM.col_values(7)[1:] 
PM_nan_m = table4_PM.col_values(9)[1:] 
PM_guang_m = table5_PM.col_values(10)[1:] 
PM_h_m = table6_PM.col_values(5)[1:] 
# =============================================================================
# 6 sites PM2.5
# =============================================================================
PM_bei1 = table1_PM.col_values(0)[1:]
PM_bei2 = table1_PM.col_values(1)[1:]
PM_bei3 = table1_PM.col_values(2)[1:]
PM_bei4 = table1_PM.col_values(3)[1:]
PM_bei5 = table1_PM.col_values(4)[1:]
PM_bei6 = table1_PM.col_values(5)[1:]
PM_bei7 = table1_PM.col_values(6)[1:]

PM_shi1 = table2_PM.col_values(0)[1:]
PM_shi2 = table2_PM.col_values(1)[1:]
PM_shi3 = table2_PM.col_values(2)[1:]
PM_shi4 = table2_PM.col_values(3)[1:]
PM_shi5 = table2_PM.col_values(4)[1:]
PM_shi6 = table2_PM.col_values(5)[1:]

PM_shang1 = table3_PM.col_values(0)[1:]
PM_shang2 = table3_PM.col_values(1)[1:]
PM_shang3 = table3_PM.col_values(2)[1:]
PM_shang4 = table3_PM.col_values(3)[1:]
PM_shang5 = table3_PM.col_values(4)[1:]
PM_shang6 = table3_PM.col_values(5)[1:]
PM_shang7 = table3_PM.col_values(6)[1:]

PM_nan1 = table4_PM.col_values(0)[1:]
PM_nan2 = table4_PM.col_values(1)[1:]
PM_nan3 = table4_PM.col_values(2)[1:]
PM_nan4 = table4_PM.col_values(3)[1:]
PM_nan5 = table4_PM.col_values(4)[1:]
PM_nan6 = table4_PM.col_values(5)[1:]
PM_nan7 = table4_PM.col_values(6)[1:]
PM_nan8 = table4_PM.col_values(7)[1:]

PM_guang1 = table5_PM.col_values(0)[1:]
PM_guang2 = table5_PM.col_values(1)[1:]
PM_guang3 = table5_PM.col_values(2)[1:]
PM_guang4 = table5_PM.col_values(3)[1:]
PM_guang5 = table5_PM.col_values(4)[1:]
PM_guang6 = table5_PM.col_values(5)[1:]
PM_guang7 = table5_PM.col_values(6)[1:]
PM_guang8 = table5_PM.col_values(7)[1:]
PM_guang9 = table5_PM.col_values(8)[1:]
PM_guang10 = table5_PM.col_values(9)[1:]


PM_h1 = table6_PM.col_values(0)[1:]
PM_h2 = table6_PM.col_values(1)[1:]
PM_h3 = table6_PM.col_values(2)[1:]
PM_h4 = table6_PM.col_values(3)[1:]
PM_h5 = table6_PM.col_values(4)[1:]


# =============================================================================
# Plotting
# =============================================================================
plt.figure(figsize=(24, 8))

#beijing
pic = plt.subplot(2, 3, 1)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
beijing = pic.plot(x, PM10_Beijing, linewidth=4, label = 'Beijing_PM10', color = 'darkblue')
beijing2 = pic.plot(x, PM1_Beijing, linewidth=4, label = 'Beijing_PM1', color = 'green')

obs_bei_pm10 = pic.plot(x, PM10_bei_m, linewidth=4, label = 'Obs_pm10 (7 sites mean)', color ='r')
obs_bei_pm = pic.plot(x, PM_bei_m, linewidth=4, label = 'Obs_pm2.5 (7 sites mean)', color ='darkorange')

lbei1_pm10 = pic.plot(x, PM10_bei1, linewidth=1,  label = '7 sites PM10', color ='coral')
lbei2_pm10 = pic.plot(x, PM10_bei2, linewidth=1,  color ='coral')
lbei3_pm10 = pic.plot(x, PM10_bei3, linewidth=1,  color ='coral')
lbei4_pm10 = pic.plot(x, PM10_bei4, linewidth=1,  color ='coral')
lbei5_pm10 = pic.plot(x, PM10_bei5, linewidth=1,  color ='coral')
lbei6_pm10 = pic.plot(x, PM10_bei6, linewidth=1,  color ='coral')
lbei7_pm10 = pic.plot(x, PM10_bei7, linewidth=1,  color ='coral')

lbei1_pm = pic.plot(x, PM_bei1, linewidth=1,  label = '7 sites PM2.5', color ='gold')
lbei2_pm = pic.plot(x, PM_bei2, linewidth=1,  color ='gold')
lbei3_pm = pic.plot(x, PM_bei3, linewidth=1,  color ='gold')
lbei4_pm = pic.plot(x, PM_bei4, linewidth=1,  color ='gold')
lbei5_pm = pic.plot(x, PM_bei5, linewidth=1,  color ='gold')
lbei6_pm = pic.plot(x, PM_bei6, linewidth=1,  color ='gold')
lbei7_pm = pic.plot(x, PM_bei7, linewidth=1,  color ='gold')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of PM in Beijing (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' PM (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

# shijiazhuang
pic = plt.subplot(2, 3, 2)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
shijiazhuang = pic.plot(x, PM10_Shijiazhuang, linewidth=4, label = 'Shijiazhuang_PM10', color = 'darkblue')
shijiazhuang2 = pic.plot(x, PM1_Shijiazhuang, linewidth=4, label = 'Shijiazhuang_PM1', color = 'green')

obs_shi_pm10 = pic.plot(x, PM10_shi_m, linewidth=4, label = 'Obs_pm10 (7 sites mean)', color ='r')
obs_shi_pm = pic.plot(x, PM_shi_m, linewidth=4, label = 'Obs_pm2.5 (7 sites mean)', color ='darkorange')

lshi1_pm10 = pic.plot(x, PM10_shi1, linewidth=1,  label = '7 sites PM10', color ='coral')
lshi2_pm10 = pic.plot(x, PM10_shi2, linewidth=1,  color ='coral')
lshi3_pm10 = pic.plot(x, PM10_shi3, linewidth=1,  color ='coral')
lshi4_pm10 = pic.plot(x, PM10_shi4, linewidth=1,  color ='coral')
lshi5_pm10 = pic.plot(x, PM10_shi5, linewidth=1,  color ='coral')
lshi6_pm10 = pic.plot(x, PM10_shi6, linewidth=1,  color ='coral')


lshi1_pm = pic.plot(x, PM_shi1, linewidth=1,  label = '7 sites PM2.5', color ='gold')
lshi2_pm = pic.plot(x, PM_shi2, linewidth=1,  color ='gold')
lshi3_pm = pic.plot(x, PM_shi3, linewidth=1,  color ='gold')
lshi4_pm = pic.plot(x, PM_shi4, linewidth=1,  color ='gold')
lshi5_pm = pic.plot(x, PM_shi5, linewidth=1,  color ='gold')
lshi6_pm = pic.plot(x, PM_shi6, linewidth=1,  color ='gold')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of PM in Shijiazhuang (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' PM (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)
    
    
 
# shanghai
pic = plt.subplot(2, 3, 3)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
shanghai = pic.plot(x, PM10_Shanghai, linewidth=4, label = 'Shanghai_PM10', color = 'darkblue')
shanghai2 = pic.plot(x, PM1_Shanghai, linewidth=4, label = 'Shanghai_PM1', color = 'green')

obs_shang_pm10 = pic.plot(x, PM10_shang_m, linewidth=4, label = 'Obs_pm10 (7 sites mean)', color ='r')
obs_shang_pm = pic.plot(x, PM_shang_m, linewidth=4, label = 'Obs_pm2.5 (7 sites mean)', color ='darkorange')

lshang1_pm10 = pic.plot(x, PM10_shang1, linewidth=1,  label = '7 sites PM10', color ='coral')
lshang2_pm10 = pic.plot(x, PM10_shang2, linewidth=1,  color ='coral')
lshang3_pm10 = pic.plot(x, PM10_shang3, linewidth=1,  color ='coral')
lshang4_pm10 = pic.plot(x, PM10_shang4, linewidth=1,  color ='coral')
lshang5_pm10 = pic.plot(x, PM10_shang5, linewidth=1,  color ='coral')
lshang6_pm10 = pic.plot(x, PM10_shang6, linewidth=1,  color ='coral')
lshang7_pm10 = pic.plot(x, PM10_shang7, linewidth=1,  color ='coral')

lshang1_pm = pic.plot(x, PM_shang1, linewidth=1,  label = '7 sites PM2.5', color ='gold')
lshang2_pm = pic.plot(x, PM_shang2, linewidth=1,  color ='gold')
lshang3_pm = pic.plot(x, PM_shang3, linewidth=1,  color ='gold')
lshang4_pm = pic.plot(x, PM_shang4, linewidth=1,  color ='gold')
lshang5_pm = pic.plot(x, PM_shang5, linewidth=1,  color ='gold')
lshang6_pm = pic.plot(x, PM_shang6, linewidth=1,  color ='gold')
lshang7_pm = pic.plot(x, PM_shang7, linewidth=1,  color ='gold')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of PM in Shanghai (June 2014)')
#plt.xlabel('hour per day')
plt.ylabel(' PM (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')


for label in pic.get_xticklabels():
    label.set_rotation(45)
    
    
# nanjing
pic = plt.subplot(2, 3, 4)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
nanjing = pic.plot(x, PM10_Nanjing, linewidth=4, label = 'Modelled PM10', color = 'darkblue')
nanjing2 = pic.plot(x, PM1_Nanjing, linewidth=4, label = 'Modelled PM1', color = 'green')

obs_nan_pm10 = pic.plot(x, PM10_nan_m, linewidth=4, label = 'Obs PM10', color ='r')
obs_nan_pm = pic.plot(x, PM_nan_m, linewidth=4, label = 'Obs PM2.5', color ='darkorange')

lnan1_pm10 = pic.plot(x, PM10_nan1, linewidth=1,  label = 'PM10 of a single location', color ='coral')
lnan2_pm10 = pic.plot(x, PM10_nan2, linewidth=1,  color ='coral')
lnan3_pm10 = pic.plot(x, PM10_nan3, linewidth=1,  color ='coral')
lnan4_pm10 = pic.plot(x, PM10_nan4, linewidth=1,  color ='coral')
lnan5_pm10 = pic.plot(x, PM10_nan5, linewidth=1,  color ='coral')
lnan6_pm10 = pic.plot(x, PM10_nan6, linewidth=1,  color ='coral')
lnan7_pm10 = pic.plot(x, PM10_nan7, linewidth=1,  color ='coral')
lnan8_pm10 = pic.plot(x, PM10_nan8, linewidth=1,  color ='coral')

lnan1_pm = pic.plot(x, PM_nan1, linewidth=1,  label = 'PM2.5 of a single location', color ='gold')
lnan2_pm = pic.plot(x, PM_nan2, linewidth=1,  color ='gold')
lnan3_pm = pic.plot(x, PM_nan3, linewidth=1,  color ='gold')
lnan4_pm = pic.plot(x, PM_nan4, linewidth=1,  color ='gold')
lnan5_pm = pic.plot(x, PM_nan5, linewidth=1,  color ='gold')
lnan6_pm = pic.plot(x, PM_nan6, linewidth=1,  color ='gold')
lnan7_pm = pic.plot(x, PM_nan7, linewidth=1,  color ='gold')
lnan8_pm = pic.plot(x, PM_nan8, linewidth=1,  color ='gold')


ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)



plt.title('Comparisons of NOx in Nanjing (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' PM  (ug/m3)')
plt.legend(bbox_to_anchor=(0.4, -0.09, 3.0, -0.09),  ncol= 6, mode="expand")   # bbox_to_anchor=(x, y)
#ax.ax = gca()
#ax.set_position([0,0,0.8,1]) (left, bottom, width, height)
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
# guangzhou
pic = plt.subplot(2, 3, 5)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
guangzhou = pic.plot(x, PM10_Guangzhou, linewidth=4, label = 'Guangzhou_PM10', color = 'darkblue')
guangzhou2 = pic.plot(x, PM1_Guangzhou, linewidth=4, label = 'Guangzhou_PM1', color = 'green')

obs_guang_pm10 = pic.plot(x, PM10_guang_m, linewidth=4, label = 'Obs_pm10 (7 sites mean)', color ='r')
obs_guang_pm = pic.plot(x, PM_guang_m, linewidth=4, label = 'Obs_pm2.5 (7 sites mean)', color ='darkorange')

lguang1_pm10 = pic.plot(x, PM10_guang1, linewidth=1,  label = '7 sites PM10', color ='coral')
lguang2_pm10 = pic.plot(x, PM10_guang2, linewidth=1,  color ='coral')
lguang3_pm10 = pic.plot(x, PM10_guang3, linewidth=1,  color ='coral')
lguang4_pm10 = pic.plot(x, PM10_guang4, linewidth=1,  color ='coral')
lguang5_pm10 = pic.plot(x, PM10_guang5, linewidth=1,  color ='coral')
lguang6_pm10 = pic.plot(x, PM10_guang6, linewidth=1,  color ='coral')
lguang7_pm10 = pic.plot(x, PM10_guang7, linewidth=1,  color ='coral')
lguang8_pm10 = pic.plot(x, PM10_guang8, linewidth=1,  color ='coral')
lguang9_pm10 = pic.plot(x, PM10_guang9, linewidth=1,  color ='coral')
lguang10_pm10 = pic.plot(x, PM10_guang10, linewidth=1,  color ='coral')

lguang1_pm = pic.plot(x, PM_guang1, linewidth=1,  label = '7 sites PM2.5', color ='gold')
lguang2_pm = pic.plot(x, PM_guang2, linewidth=1,  color ='gold')
lguang3_pm = pic.plot(x, PM_guang3, linewidth=1,  color ='gold')
lguang4_pm = pic.plot(x, PM_guang4, linewidth=1,  color ='gold')
lguang5_pm = pic.plot(x, PM_guang5, linewidth=1,  color ='gold')
lguang6_pm = pic.plot(x, PM_guang6, linewidth=1,  color ='gold')
lguang7_pm = pic.plot(x, PM_guang7, linewidth=1,  color ='gold')
lguang8_pm = pic.plot(x, PM_guang8, linewidth=1,  color ='gold')
lguang9_pm = pic.plot(x, PM_guang9, linewidth=1,  color ='gold')
lguang10_pm = pic.plot(x, PM_guang10, linewidth=1,  color ='gold')

ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of PM in Guangzhou (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' PM (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

    
# hk
pic = plt.subplot(2, 3, 6)

pos1 = pic.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height*0.9 ] 
pic.set_position(pos2)

x = np.arange(1,25)
Hongkong = pic.plot(x, PM10_Hongkong, linewidth=4, label = 'Hongkong_PM10', color = 'darkblue')
Hongkong2 = pic.plot(x, PM1_Hongkong, linewidth=4, label = 'Hongkong_PM1', color = 'green')

obs_h_pm10 = pic.plot(x, PM10_h_m, linewidth=4, label = 'Obs_pm10 (7 sites mean)', color ='r')
obs_h_pm = pic.plot(x, PM_h_m, linewidth=4, label = 'Obs_pm2.5 (7 sites mean)', color ='darkorange')

lh1_pm10 = pic.plot(x, PM10_h1, linewidth=1,  label = '7 sites PM10', color ='coral')
lh2_pm10 = pic.plot(x, PM10_h2, linewidth=1,  color ='coral')
lh3_pm10 = pic.plot(x, PM10_h3, linewidth=1,  color ='coral')
lh4_pm10 = pic.plot(x, PM10_h4, linewidth=1,  color ='coral')
lh5_pm10 = pic.plot(x, PM10_h5, linewidth=1,  color ='coral')


lh1_pm = pic.plot(x, PM_h1, linewidth=1,  label = '7 sites PM2.5', color ='gold')
lh2_pm = pic.plot(x, PM_h2, linewidth=1,  color ='gold')
lh3_pm = pic.plot(x, PM_h3, linewidth=1,  color ='gold')
lh4_pm = pic.plot(x, PM_h4, linewidth=1,  color ='gold')
lh5_pm = pic.plot(x, PM_h5, linewidth=1,  color ='gold')



ticks = np.arange(1, 25) 
labels = range (1, 25)
pic.set_xticks(x)
pic.set_xticklabels(labels)
pic.set_xlim(1, 24)
#pic.set_ylim(0, 700)

plt.title('Comparisons of PM in Hong Kong (June 2014)')
plt.xlabel('hour per day')
plt.ylabel(' PM (ug/m3)')
#plt.legend(loc = 'best')
plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)


for label in pic.get_xticklabels():
    label.set_rotation(45)

    

    
    
plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.15, right=0.9, top=0.9, hspace=0.2, wspace=0.4)
#plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/Comparison_PM_6cities_test.png', dpi=600, transparent=True)
plt.savefig('Z:/output_ukca/u-av256/plotting_scripts/diurnal_cycle/Comparison_PM_6cities_test.png', dpi=600, transparent=True)
plt.show()

