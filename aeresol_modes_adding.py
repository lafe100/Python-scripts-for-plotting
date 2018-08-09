# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:32:59 2018

@author: afe
"""

# =============================================================================
# adding aerosol
# =============================================================================
import iris
#s38485 = ['m01s38i485'] #nucleation soluble h2so4
#s38486 = ['m01s38i486'] #aitken soluble h2so4
#s38487 = ['m01s38i487'] #accumulation soluble h2so4
#s38488 = ['m01s38i488'] #coarse soluble h2so4
#s38489 = ['m01s38i489'] #aitken soluble bc
#s38490 = ['m01s38i490'] #accumulation soluble BC
#s38491 = ['m01s38i491'] #coarse soluble BC 
#s38492 = ['m01s38i492'] #aitken insoluble BC
#s38493 = ['m01s38i493'] #uncleation soluble om
#s38494 = ['m01s38i494'] #aitken soluble om
#s38495 = ['m01s38i495'] #accumulation soluble om
#s38496 = ['m01s38i496'] #coarse soluble om
#s38497 = ['m01s38i497'] #aitken insoluble om 
#s38498 = ['m01s38i498'] #accumulation soluble sea salt 
#s38499 = ['m01s38i499'] #coarse soluble sea salt

# =============================================================================
# apc (kg/m3)
# =============================================================================
#filename1 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38485.pp'
#filename2 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38486.pp'
#filename3 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38487.pp'
#filename4 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38488.pp'
#filename5 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38489.pp'
#filename6 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38490.pp'
#filename7 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38491.pp'
#filename8 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38492.pp'
#filename9 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38493.pp'
#filename10 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38494.pp'
#filename11 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38495.pp'
#filename12 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38496.pp'
#filename13 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38497.pp'
#filename14 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38498.pp'
#filename15 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38499.pp'

# =============================================================================
# apk (kg/kg)
# =============================================================================
filename1 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34102.pp'
filename2 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34104.pp'
filename3 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34105.pp'
filename4 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34106.pp'
filename5 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34108.pp'
filename6 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34109.pp'
filename7 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34110.pp'
filename8 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34111.pp'
filename9 =  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34114.pp'
filename10 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34115.pp'
filename11 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34116.pp'
filename12 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34117.pp'
filename13 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34120.pp'
filename14 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34121.pp'
filename15 = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34126.pp'


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

aerosol_total_pm2p5 = cube1[0]+cube2[0]+cube3[0]+cube5[0]+cube6[0]+cube8[0]+cube9[0]+cube10[0]+cube11[0]+cube13[0]+cube14[0]
aerosol_total_pm10 = cube1[0]+cube2[0]+cube3[0]+cube4[0]+cube5[0]+cube6[0]+cube7[0]+cube8[0]+cube9[0]+cube10[0]+cube11[0]+cube12[0]+cube13[0]+cube14[0]+cube15[0]

#print aerosol_total_pm2p5
#print aerosol_total_pm2p5[0]             
#print aerosol_total_pm10
#print aerosol_total_pm10[0]             
             
iris.save(aerosol_total_pm2p5,  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/pm2.5_monthly.pp')
iris.save(aerosol_total_pm10,  '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/pm10_monthly.pp')

print('Done')