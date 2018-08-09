# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:14:25 2018

@author: s1731217
"""

# =============================================================================
# dumped pp file for no2, o3, pm2.5 & pm10
# =============================================================================
import iris 
s34001 = ['m01s34i001'] #o3
s34996 = ['m01s34i996'] #no2 

filename = ['/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/apb.pp/av256a.pb201406*.pp']

cube = iris.load(filename)

cube34001 = cube.extract(iris.AttributeConstraint(STASH=s34001[0]))
cube34996 = cube.extract(iris.AttributeConstraint(STASH=s34996[0]))

#surface34001 = cube34001.extract(iris.Constraint(model_level_number=1))
#surface34996 = cube34996.extract(iris.Constraint(model_level_number=1))

iris.save(cube34001, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/o3.pp')
iris.save(cube34996, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/no2.pp')

print 'done'



