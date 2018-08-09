# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:22:28 2018

@author: s1731217
"""

import numpy as np
import matplotlib.pyplot as plt
import iris

filename1 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34102.pp'
filename2 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34104.pp'
filename3 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34105.pp'
filename4 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34106.pp'
filename5 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34108.pp'
filename6 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34109.pp'
filename7 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34110.pp'
filename8 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34111.pp'
filename9 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34114.pp'
filename10 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34115.pp'
filename11 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34116.pp'
filename12 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34117.pp'
filename13 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34120.pp'
filename14 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34121.pp'
filename15 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apk pm (kg kg-1)/s34126.pp'

cube1 = iris.load(filename1)
cube2 = iris.load(filename2)
cube3 = iris.load(filename3)
cube4 = iris.load(filename4)
cube5 = iris.load(filename5)
cube6 = iris.load(filename6)
cube7 = iris.load(filename7)
cube8 = iris.load(filename8)
cube9 = iris.load(filename9)
cube10 = iris.load(filename10)
cube11 = iris.load(filename11)
cube12 = iris.load(filename12)
cube13 = iris.load(filename13)
cube14 = iris.load(filename14)
cube15 = iris.load(filename15)

cube1_unit = cube1[0]*1.284*1.0e9
cube2_unit = cube2[0]*1.284*1.0e9
cube3_unit = cube3[0]*1.284*1.0e9
cube4_unit = cube4[0]*1.284*1.0e9
cube5_unit = cube5[0]*1.284*1.0e9
cube6_unit = cube6[0]*1.284*1.0e9
cube7_unit = cube7[0]*1.284*1.0e9
cube8_unit = cube8[0]*1.284*1.0e9
cube9_unit = cube9[0]*1.284*1.0e9
cube10_unit = cube10[0]*1.284*1.0e9
cube11_unit = cube11[0]*1.284*1.0e9
cube12_unit = cube12[0]*1.284*1.0e9
cube13_unit = cube13[0]*1.284*1.0e9
cube14_unit = cube14[0]*1.284*1.0e9
cube15_unit = cube15[0]*1.284*1.0e9

cube1_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube1_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube2_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube2_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube3_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube3_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube4_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube4_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube5_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube5_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube6_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube6_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube7_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube7_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube8_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube8_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube9_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube9_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube10_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube10_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube11_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube11_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube12_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube12_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube13_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube13_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube14_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube14_unit, [('latitude', 39.90), ('longitude', 116.41)])
cube15_beijing = iris.analysis.interpolate.extract_nearest_neighbour(cube15_unit, [('latitude', 39.90), ('longitude', 116.41)])


#x = [1, 2, 3, 4, 5]
#y1 = [1, 1, 2, 3, 5]
#y2 = [0, 4, 2, 6, 8]
#y3 = [1, 3, 5, 7, 9]
#
#y = np.vstack([y1, y2, y3])

#labels = ["Fibonacci ", "Evens", "Odds"]
x_utc = np.arange(9.5, 706.5)

fig, ax = plt.subplots()
ax.stackplot(x_utc,\
             cube1_beijing.data, cube2_beijing.data, cube3_beijing.data, cube4_beijing.data, cube5_beijing.data,\
             cube6_beijing.data, cube7_beijing.data, cube8_beijing.data, cube9_beijing.data, cube10_beijing.data,\
             cube11_beijing.data, cube12_beijing.data, cube13_beijing.data, cube14_beijing.data, cube15_beijing.data)

#ax.legend(loc=2)
plt.show()

#fig, ax = plt.subplots()
#ax.stackplot(x, y)
#plt.show()