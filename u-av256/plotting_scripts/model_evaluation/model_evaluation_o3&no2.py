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
table1 = data.sheet_by_name('NO2')
table2 = data.sheet_by_name('O3')

y_no2_beijing = table1.col_values(0)[1:] 
y_no2_shijiazhuang = table1.col_values(1)[1:] 
y_no2_shanghai = table1.col_values(2)[1:] 
y_no2_nanjing = table1.col_values(3)[1:] 
y_no2_guangzhou = table1.col_values(4)[1:] 
y_no2_hongkong = table1.col_values(5)[1:] 
y_o3_beijing = table2.col_values(0)[1:] 
y_o3_shijiazhuang = table2.col_values(1)[1:] 
y_o3_shanghai = table2.col_values(2)[1:] 
y_o3_nanjing = table2.col_values(3)[1:] 
y_o3_guangzhou = table2.col_values(4)[1:] 
y_o3_hongkong = table2.col_values(5)[1:]  

#x_cn = range(1, 745), for 31d; if for June (30d), it is range(1,721)
#x_utc = range (10, 754)
#example: UTC time: 00:30, China time: 08:30
x_cn = np.arange(1.5, 721.5)
x_utc = np.arange(9.5, 729.5)
# =============================================================================
# loading data (cube); u-av256: nudged; u-av257: non-nudged
# =============================================================================
filename_no2  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/no2.pp' # no2
filename2_no2 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/no2.pp' # no2 (nudging)
filename_o3   = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/o3.pp'  # o3
filename2_o3  = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/o3.pp'  # o3 (nudging)

cube_no2  = iris.load(filename_no2) 
cube2_no2 = iris.load(filename2_no2) #cube2: nudging
cube_o3   = iris.load(filename_o3)
cube2_o3  = iris.load(filename2_o3)
# unit: ug/m3
cube_no2_unit_beijing      = cube_no2[0]*1.185*1.0e9
cube_no2_unit_shijiazhuang = cube_no2[0]*1.181*1.0e9
cube_no2_unit_shanghai     = cube_no2[0]*1.185*1.0e9
cube_no2_unit_nanjing      = cube_no2[0]*1.185*1.0e9
cube_no2_unit_guangzhou    = cube_no2[0]*1.169*1.0e9
cube_no2_unit_hk           = cube_no2[0]*1.169*1.0e9

cube_o3_unit_beijing       = cube_o3[0]*1.185*1.0e9
cube_o3_unit_shijiazhuang  = cube_o3[0]*1.181*1.0e9
cube_o3_unit_shanghai      = cube_o3[0]*1.185*1.0e9
cube_o3_unit_nanjing       = cube_o3[0]*1.185*1.0e9
cube_o3_unit_guangzhou     = cube_o3[0]*1.169*1.0e9
cube_o3_unit_hk            = cube_o3[0]*1.169*1.0e9

#nudged data : unit2
cube_no2_unit2_beijing     = cube2_no2[0]*1.185*1.0e9
cube_no2_unit2_shijiazhuang= cube2_no2[0]*1.181*1.0e9
cube_no2_unit2_shanghai    = cube2_no2[0]*1.185*1.0e9
cube_no2_unit2_nanjing     = cube2_no2[0]*1.185*1.0e9
cube_no2_unit2_guangzhou   = cube2_no2[0]*1.169*1.0e9
cube_no2_unit2_hk          = cube2_no2[0]*1.169*1.0e9

cube_o3_unit2_beijing      = cube2_o3[0]*1.185*1.0e9
cube_o3_unit2_shijiazhuang = cube2_o3[0]*1.181*1.0e9
cube_o3_unit2_shanghai     = cube2_o3[0]*1.185*1.0e9
cube_o3_unit2_nanjing      = cube2_o3[0]*1.185*1.0e9
cube_o3_unit2_guangzhou    = cube2_o3[0]*1.169*1.0e9
cube_o3_unit2_hk           = cube2_o3[0]*1.169*1.0e9

cube_beijing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_no2 = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit_hk, [('latitude', 22.33), ('longitude', 114.19)])

cube_beijing_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_no2_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_no2_unit2_hk, [('latitude', 22.33), ('longitude', 114.19)])

cube_beijing_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_o3 = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit_hk, [('latitude', 22.33), ('longitude', 114.19)])

cube_beijing_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_beijing, [('latitude', 39.90), ('longitude', 116.41)])
cube_shijiazhuang_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_shijiazhuang, [('latitude', 38.04), ('longitude', 114.51)])
cube_shanghai_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_shanghai, [('latitude', 31.23), ('longitude', 121.47)])
cube_nanjing_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_nanjing, [('latitude', 32.06), ('longitude', 118.80)])
cube_guangzhou_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_guangzhou, [('latitude', 23.13), ('longitude', 113.26)])
cube_hongkong_o3_nudge = iris.analysis.interpolate.extract_nearest_neighbour(cube_o3_unit2_hk, [('latitude', 22.33), ('longitude', 114.19)])
# =============================================================================
# NO2 plotting
# =============================================================================
#beijing
plt.figure(figsize=(24, 15), facecolor='white')
pic = plt.subplot(6,2,1)
beijing_no2 = pic.plot(x_utc, cube_beijing_no2.data, linewidth=4, color = 'k')
beijing_no2_nudging = pic.plot(x_utc, cube_beijing_no2_nudge.data, linewidth=4, color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_beijing, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in Beijing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Beijing')
#plt.legend(loc = 1)
#red_patch1 = mpatches.Patch(color='red', label='Beijing')
#plt.legend(handles=[red_patch1])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#shijiazhuang   
pic = plt.subplot(6,2,3)
shijiazhuang_no2 = pic.plot(x_utc, cube_shijiazhuang_no2.data, linewidth=4, color = 'k')
shijiazhuang_no2_nudging = pic.plot(x_utc, cube_shijiazhuang_no2_nudge.data, linewidth=4, color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_shijiazhuang, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in shijiazhuang (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Shijiazhuang')
#plt.legend(loc = 1)

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)
#red_patch2 = mpatches.Patch(color='red', label='Shijiazhuang')
#plt.legend(handles=[red_patch2])

for label in pic.get_xticklabels():
    label.set_rotation(45)

#shanghai    
pic = plt.subplot(6,2,5)
shanghai_no2 = pic.plot(x_utc, cube_shanghai_no2.data, linewidth=4, color = 'k')
shanghai_no2_nudging = pic.plot(x_utc, cube_shanghai_no2_nudge.data, linewidth=4, color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_shanghai, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in shanghai (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Shanghai')
#plt.legend(loc = 1)
#red_patch3 = mpatches.Patch(color='red', label='Shanghai')
#plt.legend(handles=[red_patch3])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#nanjing    
pic = plt.subplot(6,2,7)
nanjing_no2 = pic.plot(x_utc, cube_nanjing_no2.data, linewidth=4, color = 'k')
nanjing_no2_nudging = pic.plot(x_utc, cube_nanjing_no2_nudge.data, linewidth=4, color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_nanjing, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in nanjing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Nanjing')
#plt.legend(loc = 1)
#red_patch4 = mpatches.Patch(color='red', label='Nanjing')
#plt.legend(handles=[red_patch4])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#guangzhou
pic = plt.subplot(6,2,9)
guangzhou_no2 = pic.plot(x_utc, cube_guangzhou_no2.data, linewidth=4, color = 'k')
guangzhou_no2_nudging = pic.plot(x_utc, cube_guangzhou_no2_nudge.data, linewidth=4, color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_guangzhou, linewidth = 4, label = 'OBS', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 in guangzhou (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Guangzhou')
#plt.legend(loc = 1)
#red_patch5 = mpatches.Patch(color='red', label='Guangzhou')
#plt.legend(handles=[red_patch5])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#hongkong
pic = plt.subplot(6,2,11)
hongkong_no2 = pic.plot(x_utc, cube_hongkong_no2.data, linewidth=4, label = 'Model: NO2 (ug/m3)', color = 'k')
hongkong_no2_nudging = pic.plot(x_utc, cube_hongkong_no2_nudge.data, linewidth=4, label = 'Model: NO2 (nudged) ', color = 'sienna')
obs_no2 = pic.plot(x_cn, y_no2_hongkong, linewidth = 4, label = 'Obs (ug/m3) June', color = 'red')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('NO2 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' NO2 Hong Kong')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='red', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)    
    
#label
plt.legend(bbox_to_anchor=(0.03, -0.09, 0.9, -0.09),  ncol= 4, mode="expand")    # bbox_to_anchor=(x0, y0, x, y)  
# =============================================================================
# O3 plotting
# =============================================================================
#beijing
pic = plt.subplot(6,2,2)
beijing_o3 = pic.plot(x_utc, cube_beijing_o3.data, linewidth=4, color = 'limegreen')
beijing_o3_nudging = pic.plot(x_utc, cube_beijing_o3_nudge.data, linewidth=4, color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_beijing, linewidth = 4, label = 'OBS', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 in Beijing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Beijing')
#plt.legend(loc = 1)
#red_patch6 = mpatches.Patch(color='gold', label='Beijing')
#plt.legend(handles=[red_patch6])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)


#shijiazhuang
pic = plt.subplot(6,2,4)
shijiazhuang_o3 = pic.plot(x_utc, cube_shijiazhuang_o3.data, linewidth=4, color = 'limegreen')
shijiazhuang_o3_nudging = pic.plot(x_utc, cube_shijiazhuang_o3_nudge.data, linewidth=4, color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_shijiazhuang, linewidth = 4, label = 'OBS', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 in shijiazhuang (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Shijiazhuang')
#plt.legend(loc = 1)
#red_patch7 = mpatches.Patch(color='gold', label='Shijiazhuang')
#plt.legend(handles=[red_patch7])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#shanghai 
pic = plt.subplot(6,2,6)
shanghai_o3 = pic.plot(x_utc, cube_shanghai_o3.data, linewidth=4, color = 'limegreen')
shanghai_o3_nudging = pic.plot(x_utc, cube_shanghai_o3_nudge.data, linewidth=4, color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_shanghai, linewidth = 4, label = 'OBS', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 in shanghai (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Shanghai')
#plt.legend(loc = 1)
#red_patch8 = mpatches.Patch(color='gold', label='Shanghai')
#plt.legend(handles=[red_patch8])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#nanjing
pic = plt.subplot(6,2,8)
nanjing_o3 = pic.plot(x_utc, cube_nanjing_o3.data, linewidth=4, color = 'limegreen')
nanjing_o3_nudging = pic.plot(x_utc, cube_nanjing_o3_nudge.data, linewidth=4, color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_nanjing, linewidth = 4, label = 'OBS', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 in nanjing (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Nanjing')
#plt.legend(loc = 1)
#red_patch9 = mpatches.Patch(color='gold', label='Nanjing')
#plt.legend(handles=[red_patch9])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#guangzhou
pic = plt.subplot(6,2,10)
guangzhou_o3 = pic.plot(x_utc, cube_guangzhou_o3.data, linewidth=4, color = 'limegreen')
guangzhou_o3_nudging = pic.plot(x_utc, cube_guangzhou_o3_nudge.data, linewidth=4, color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_guangzhou, linewidth = 4, label = 'OBS', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 in guangzhou (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Guangzhou')
#plt.legend(loc = 1)
#red_patch10 = mpatches.Patch(color='gold', label='Guangzhou')
#plt.legend(handles=[red_patch10])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)

#hongkong
pic = plt.subplot(6,2,12)
hongkong_o3 = pic.plot(x_utc, cube_hongkong_o3.data, linewidth=4, label = 'Model: O3 (ug/m3)', color = 'limegreen')
hongkong_o3_nudging = pic.plot(x_utc, cube_hongkong_o3_nudge.data, linewidth=4, label = 'Model O3: (nudged)', color = 'darkblue')
obs_o3 = pic.plot(x_cn, y_o3_hongkong, linewidth = 4, label = 'Obs (ug/m3) June', color = 'gold')

ticks = np.arange(1, 721, 24) 
labels = range (1, 31)
pic.set_xticks(ticks)
pic.set_xticklabels(labels)
#plt.title('O3 (10/11-10/12) 2014')
#plt.xlabel('Day')
plt.ylabel(' O3 Hong Kong')
#plt.legend(loc = 1)
#red_patch = mpatches.Patch(color='gold', label='HongKong')
#plt.legend(handles=[red_patch])

plt.grid(linestyle = '--')
# pic.set_xticklabels(day_list)

for label in pic.get_xticklabels():
    label.set_rotation(45)
    
#label
plt.legend(bbox_to_anchor=(0.03, -0.09, 0.9, -0.09),  ncol= 4, mode="expand")    # bbox_to_anchor=(x0, y0, x, y)

#plt.tight_layout()
plt.subplots_adjust(left=0.06, bottom=0.1, right=0.94, top=0.95, hspace=0.2, wspace=0.2)
plt.savefig('/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/model_evaluation/model_evaluation_no2_o3.png', dpi=600, transparent=True)
plt.show()
