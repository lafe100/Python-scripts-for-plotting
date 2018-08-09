# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:14:25 2018

@author: s1731217
"""

# =============================================================================
# dumped pp file for Met fields
# =============================================================================
import iris 
s00002 = ['m01s00i002'] # u
s00003 = ['m01s00i003'] # v
s00010 = ['m01s00i010'] # specific humidty
s00024 = ['m01s00i024'] # T
s00025 = ['m01s00i025'] # BL
s00409 = ['m01s00i409'] # P

filename = ['/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/apa.pp/av257a.pa201406*.pp']

cube = iris.load(filename)

cube00002 = cube.extract(iris.AttributeConstraint(STASH=s00002[0]))
cube00003 = cube.extract(iris.AttributeConstraint(STASH=s00003[0]))
cube00010 = cube.extract(iris.AttributeConstraint(STASH=s00010[0]))
cube00024 = cube.extract(iris.AttributeConstraint(STASH=s00024[0]))
cube00025 = cube.extract(iris.AttributeConstraint(STASH=s00025[0]))
cube00409 = cube.extract(iris.AttributeConstraint(STASH=s00409[0]))

#surface34001 = cube34001.extract(iris.Constraint(model_level_number=1))
#surface34996 = cube34996.extract(iris.Constraint(model_level_number=1))

iris.save(cube00002, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/u.pp')
iris.save(cube00003, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/v.pp')
iris.save(cube00010, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/specific_humidty.pp')
iris.save(cube00024, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/T.pp')
iris.save(cube00025, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/BL.pp')
iris.save(cube00409, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/dumped_pp_files/June/Met/P.pp')

print 'done'



