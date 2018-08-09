# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:55:23 2018

@author: s1731217
"""

# =============================================================================
# Plotting
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import openpyxl
import xlrd
from matplotlib.dates import DateFormatter, MonthLocator, WeekdayLocator, DayLocator, MONDAY, YEARLY
import matplotlib.dates as dates
from pylab import *
import numpy as np
import iris

# =============================================================================
# loading data (excel)
# =============================================================================
data = xlrd.open_workbook('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/model_evaluation/2014_06_total.xlsx')

#data = xlrd.open_workbook('Z:/output_ukca/observation/beijing/test.xlsx')
table1 = data.sheet_by_name('PM2.5')
table2 = data.sheet_by_name('O3')
table3 = data.sheet_by_name('NO2')

y_pm_beijing  = table1.col_values(0)[1:] 
y_o3_beijing  = table2.col_values(0)[1:] 
y_no2_beijing = table3.col_values(0)[1:] 

#y_no2_shijiazhuang = table1.col_values(1)[1:] 
#y_no2_shanghai = table1.col_values(2)[1:] 
#y_no2_nanjing = table1.col_values(3)[1:] 
#y_no2_guangzhou = table1.col_values(4)[1:] 
#y_no2_hongkong = table1.col_values(5)[1:]  

#x_cn = range(1, 745), for 31d; if for June (30d), it is range(1,721)
#x_utc = range (10, 754)
#example: UTC time: 00:30, China time: 08:30
x_cn = np.arange(1.5, 721.5)
x_utc = np.arange(9.5, 729.5)
# =============================================================================
# loading data (cube); u-av256: nudged; u-av257: non-nudged
# =============================================================================
# Met field
filename_u    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/u.pp' 
filename_u_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/u.pp' # n=nudged 
filename_v    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/v.pp' 
filename_v_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/v.pp' # n=nudged 
filename_h    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/specific_humidity.pp' 
filename_h_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/specific_humidity.pp' # n=nudged 
filename_t    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/T.pp' 
filename_t_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/T.pp' # n=nudged 
filename_bl    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/BL.pp' 
filename_bl_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/BL.pp' # n=nudged 
filename_p    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/P.pp' 
filename_p_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/Met/P.pp' # n=nudged 

# Chem
filename_pm    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/pm2.5.pp' 
filename_pm_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/pm2.5.pp' 
filename_o3    = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/o3.pp' 
filename_o3_n  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/o3.pp' 
filename_no2   = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/no2.pp' 
filename_no2_n = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/no2.pp'

cube_u     = iris.load(filename_u) 
cube_u_n   = iris.load(filename_u_n) 
cube_v     = iris.load(filename_v) 
cube_v_n   = iris.load(filename_v_n) 
cube_h     = iris.load(filename_h) 
cube_h_n   = iris.load(filename_h_n) 
cube_t     = iris.load(filename_t) 
cube_t_n   = iris.load(filename_t_n) 
cube_bl    = iris.load(filename_bl) 
cube_bl_n  = iris.load(filename_bl_n) 
cube_p     = iris.load(filename_p) 
cube_p_n   = iris.load(filename_p_n) 
cube_pm    = iris.load(filename_pm) 
cube_pm_n  = iris.load(filename_pm_n) 
cube_o3    = iris.load(filename_o3) 
cube_o3_n  = iris.load(filename_o3_n) 
cube_no2   = iris.load(filename_no2) 
cube_no2_n = iris.load(filename_no2_n) #cube2: nudging

cube_u_unit_beijing       = cube_u[0]
cube_u_unit2_beijing      = cube_u_n[0]
cube_v_unit_beijing       = cube_v[0]
cube_v_unit2_beijing      = cube_v_n[0]
cube_h_unit_beijing       = cube_h[0]
cube_h_unit2_beijing      = cube_h_n[0]
cube_t_unit_beijing       = cube_t[0]
cube_t_unit2_beijing      = cube_t_n[0]
cube_bl_unit_beijing      = cube_bl[0]
cube_bl_unit2_beijing     = cube_bl_n[0]
cube_p_unit_beijing       = cube_p[0]
cube_p_unit2_beijing      = cube_p_n[0]

cube_pm_unit_beijing        = cube_pm[0]*1.185*1.0e9
cube_pm_unit2_beijing       = cube_pm_n[0]*1.185*1.0e9
cube_o3_unit_beijing        = cube_o3[0]*1.185*1.0e9
cube_o3_unit2_beijing       = cube_o3_n[0]*1.185*1.0e9
cube_no2_unit_beijing       = cube_no2[0]*1.185*1.0e9
cube_no2_unit2_beijing      = cube_no2_n[0]*1.185*1.0e9

## unit: ug/m3
#cube_no2_unit_beijing      = cube_no2[0]*1.185*1.0e9
#cube_no2_unit_shijiazhuang = cube_no2[0]*1.181*1.0e9
#cube_no2_unit_shanghai     = cube_no2[0]*1.185*1.0e9
#cube_no2_unit_nanjing      = cube_no2[0]*1.185*1.0e9
#cube_no2_unit_guangzhou    = cube_no2[0]*1.169*1.0e9
#cube_no2_unit_hk           = cube_no2[0]*1.169*1.0e9
#
##nudged data : unit2
#cube_no2_unit2_beijing     = cube2_no2[0]*1.185*1.0e9
#cube_no2_unit2_shijiazhuang= cube2_no2[0]*1.181*1.0e9
#cube_no2_unit2_shanghai    = cube2_no2[0]*1.185*1.0e9
#cube_no2_unit2_nanjing     = cube2_no2[0]*1.185*1.0e9
#cube_no2_unit2_guangzhou   = cube2_no2[0]*1.169*1.0e9
#cube_no2_unit2_hk          = cube2_no2[0]*1.169*1.0e9

cube_beijing_u       = iris.analysis.interpolate.extract_nearest_neighbour(cube_u_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_u_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_u_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_v       = iris.analysis.interpolate.extract_nearest_neighbour(cube_v_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_v_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_v_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_h       = iris.analysis.interpolate.extract_nearest_neighbour(cube_h_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_h_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_h_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_t       = iris.analysis.interpolate.extract_nearest_neighbour(cube_t_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_t_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_t_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_bl       = iris.analysis.interpolate.extract_nearest_neighbour(cube_bl_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_bl_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_bl_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_p       = iris.analysis.interpolate.extract_nearest_neighbour(cube_p_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_p_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_p_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_pm       = iris.analysis.interpolate.extract_nearest_neighbour(cube_pm_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_pm_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_pm_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_o3       = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_no2       = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_beijing_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
#cube_beijing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
#cube_shijiazhuang_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
#cube_shanghai_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
#cube_nanjing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
#cube_guangzhou_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
#cube_hongkong_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_hk, [('latitude', 22.33), ('longitude', 114.19)])
#
#cube_beijing_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
#cube_shijiazhuang_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
#cube_shanghai_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
#cube_nanjing_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
#cube_guangzhou_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
#cube_hongkong_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_hk, [('latitude', 22.33), ('longitude', 114.19)])

# =============================================================================
# PM1 (model) & PM2.5 (obs) plotting
# =============================================================================
#beijing
plt.figure(figsize=(24, 15), facecolor='white')
pic = plt.subplot(6,2,1)
beijing_u = pic.plot(x_utc, cube_beijing_u.data, linewidth=4, color = 'k')
beijing_u_nudging = pic.plot(x_utc, cube_beijing_u_nudge.data, linewidth=4, color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_beijing, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in Beijing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' U Beijing')
#plt.legend(loc = 1)
#red_patch1 = mpatches.Patch(color='red', label='Beijing')
#plt.legend(handles=[red_patch1])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#shijiazhuang   
pic = plt.subplot(6,2,3)
beijing_v = pic.plot(x_utc, cube_beijing_v.data, linewidth=4, color = 'k')
beijing_v_nudging = pic.plot(x_utc, cube_beijing_v_nudge.data, linewidth=4, color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_shijiazhuang, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in shijiazhuang (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' V Beijing')
#plt.legend(loc = 1)

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)
#red_patch2 = mpatches.Patch(color='red', label='Shijiazhuang')
#plt.legend(handles=[red_patch2])

for label in pic.get_xticklabels():
    label.set_rotation(45)

#shanghai    
pic = plt.subplot(6,2,5)
beijing_h = pic.plot(x_utc, cube_beijing_h.data, linewidth=4, color = 'k')
beijing_h_nudging = pic.plot(x_utc, cube_beijing_h_nudge.data, linewidth=4, color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_shanghai, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in shanghai (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' Sepcific Humidity Beijing')
#plt.legend(loc = 1)
#red_patch3 = mpatches.Patch(color='red', label='Shanghai')
#plt.legend(handles=[red_patch3])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#nanjing    
pic = plt.subplot(6,2,7)
beijing_t = pic.plot(x_utc, cube_beijing_t.data, linewidth=4, color = 'k')
beijing_t_nudging = pic.plot(x_utc, cube_beijing_t_nudge.data, linewidth=4, color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_nanjing, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in nanjing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' Temperature Beijing')
#plt.legend(loc = 1)
#red_patch4 = mpatches.Patch(color='red', label='Nanjing')
#plt.legend(handles=[red_patch4])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#guangzhou
pic = plt.subplot(6,2,9)
beijing_bl = pic.plot(x_utc, cube_beijing_bl.data, linewidth=4, color = 'k')
beijing_bl_nudging = pic.plot(x_utc, cube_beijing_bl_nudge.data, linewidth=4, color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_guangzhou, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in guangzhou (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' Boundary Layer Beijing')
#plt.legend(loc = 1)
#red_patch5 = mpatches.Patch(color='red', label='Guangzhou')
#plt.legend(handles=[red_patch5])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#hongkong
pic = plt.subplot(6,2,11)
beijing_p = pic.plot(x_utc, cube_beijing_p.data, linewidth=4, label = 'Model: u, v, humidity, T, BL, P', color = 'k')
beijing_p_nudging = pic.plot(x_utc, cube_beijing_p_nudge.data, linewidth=4, label = 'Nudged Model', color = 'sienna')
#obs_no2 = pic.plot(x_cn, y_no2_hongkong, linewidth = 4, label = 'Obs PM2.5 (ug/m3) in June', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' Pressure Beijing')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='red', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)    
    
#label
#plt.legend(bbox_to_anchor=(0.03, -0.09, 0.9, -0.09),  ncol= 4, mode="expand")    # bbox_to_anchor=(x0, y0, x, y)  
plt.legend(bbox_to_anchor=(0.1, -0.09, 0.8, -0.09),  ncol= 4, mode="expand")    # bbox_to_anchor=(x0, y0, x, y)  

#Chem
pic = plt.subplot(6,2,2)
beijing_pm = pic.plot(x_utc, cube_beijing_pm.data, linewidth=4, label = 'Model', color = 'k')
beijing_pm_nudging = pic.plot(x_utc, cube_beijing_pm_nudge.data, linewidth=4, label = 'Nudged Model', color = 'sienna')
obs_pm = pic.plot(x_cn, y_pm_beijing, linewidth = 4, label = 'Obs PM2.5 (ug/m3) in June', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' PM Beijing')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='red', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)   
    
pic = plt.subplot(6,2,4)
beijing_o3 = pic.plot(x_utc, cube_beijing_o3.data, linewidth=4, label = 'Model', color = 'k')
beijing_o3_nudging = pic.plot(x_utc, cube_beijing_o3_nudge.data, linewidth=4, label = 'Nudged Model', color = 'sienna')
obs_o3 = pic.plot(x_cn, y_o3_beijing, linewidth = 4, label = 'Obs PM2.5 (ug/m3) in June', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Beijing')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='red', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)   
    
pic = plt.subplot(6,2,6)
beijing_pm = pic.plot(x_utc, cube_beijing_pm.data, linewidth=4, label = 'Model: PM1, O3, NO2', color = 'k')
beijing_pm_nudging = pic.plot(x_utc, cube_beijing_pm_nudge.data, linewidth=4, label = 'Nudged Model', color = 'sienna')
obs_pm = pic.plot(x_cn, y_pm_beijing, linewidth = 4, label = 'Obs: PM2.5, O3, NO2in June', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Beijing')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='red', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)   
    
plt.legend(bbox_to_anchor=(0.1, -0.09, 0.8, -0.09),  ncol= 4, mode="expand")    # bbox_to_anchor=(x0, y0, x, y)  

#plt.tight_layout()
plt.subplots_adjust(left=0.06, bottom=0.1, right=0.94, top=0.95, hspace=0.2, wspace=0.2)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/model_evaluation/model_evaluation_Met.png', dpi=600, transparent=True)
plt.show()
