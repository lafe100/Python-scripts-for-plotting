# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:14:25 2018

@author: s1731217
"""

# =============================================================================
# dumped pp file for aerosol 
# =============================================================================
import iris 
# =============================================================================
# apc (kg/m3)
# =============================================================================
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
# apk (kg/kg)
# =============================================================================
s34102 = ['m01s34i102'] #nucleation soluble h2so4
s34104 = ['m01s34i104'] #aitken soluble h2so4 
s34105 = ['m01s34i105'] #aitken soluble bc
s34106 = ['m01s34i106'] #aitken soluble om
s34108 = ['m01s34i108'] #accumulation soluble h2so4
s34109 = ['m01s34i109'] #accumulation soluble BC
s34110 = ['m01s34i110'] #accumulation soluble om
s34111 = ['m01s34i111'] #accumulation soluble sea salt
s34114 = ['m01s34i114'] #coarse soluble h2so4
s34115 = ['m01s34i115'] #coarse soluble BC 
s34116 = ['m01s34i116'] #coarse soluble om
s34117 = ['m01s34i117'] #coarse soluble sea salt
s34120 = ['m01s34i120'] #aitken insoluble BC
s34121 = ['m01s34i121'] #aitken insoluble om
s34126 = ['m01s34i126'] #uncleation soluble om

#filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/apk.pp/av256a.pk201406*.pp'
filename = '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av257/apm.pp/*' # monthly dump files

cube = iris.load(filename)

# =============================================================================
# apc (kg/m3)
# =============================================================================
#cube38485 = cube.extract(iris.AttributeConstraint(STASH=s38485[0]))
#cube38486 = cube.extract(iris.AttributeConstraint(STASH=s38486[0]))
#cube38487 = cube.extract(iris.AttributeConstraint(STASH=s38487[0]))
#cube38488 = cube.extract(iris.AttributeConstraint(STASH=s38488[0]))
#cube38489 = cube.extract(iris.AttributeConstraint(STASH=s38489[0]))
#cube38490 = cube.extract(iris.AttributeConstraint(STASH=s38490[0]))
#cube38491 = cube.extract(iris.AttributeConstraint(STASH=s38491[0]))
#cube38492 = cube.extract(iris.AttributeConstraint(STASH=s38492[0]))
#cube38493 = cube.extract(iris.AttributeConstraint(STASH=s38493[0]))
#cube38494 = cube.extract(iris.AttributeConstraint(STASH=s38494[0]))
#cube38495 = cube.extract(iris.AttributeConstraint(STASH=s38495[0]))
#cube38496 = cube.extract(iris.AttributeConstraint(STASH=s38496[0]))
#cube38497 = cube.extract(iris.AttributeConstraint(STASH=s38497[0]))
#cube38498 = cube.extract(iris.AttributeConstraint(STASH=s38498[0]))
#cube38499 = cube.extract(iris.AttributeConstraint(STASH=s38499[0]))

# =============================================================================
# apk (kg/kg)
# =============================================================================

cube34102 = cube.extract(iris.AttributeConstraint(STASH=s34102[0]))
cube34104 = cube.extract(iris.AttributeConstraint(STASH=s34104[0]))
cube34105 = cube.extract(iris.AttributeConstraint(STASH=s34105[0]))
cube34106 = cube.extract(iris.AttributeConstraint(STASH=s34106[0]))
cube34108 = cube.extract(iris.AttributeConstraint(STASH=s34108[0]))
cube34109 = cube.extract(iris.AttributeConstraint(STASH=s34109[0]))
cube34110 = cube.extract(iris.AttributeConstraint(STASH=s34110[0]))
cube34111 = cube.extract(iris.AttributeConstraint(STASH=s34111[0]))
cube34114 = cube.extract(iris.AttributeConstraint(STASH=s34114[0]))
cube34115 = cube.extract(iris.AttributeConstraint(STASH=s34115[0]))
cube34116 = cube.extract(iris.AttributeConstraint(STASH=s34116[0]))
cube34117 = cube.extract(iris.AttributeConstraint(STASH=s34117[0]))
cube34120 = cube.extract(iris.AttributeConstraint(STASH=s34120[0]))
cube34121 = cube.extract(iris.AttributeConstraint(STASH=s34121[0]))
cube34126 = cube.extract(iris.AttributeConstraint(STASH=s34126[0]))
  
  
#surface34001 = cube34001.extract(iris.Constraint(model_level_number=1))
#surface34996 = cube34996.extract(iris.Constraint(model_level_number=1))

# =============================================================================
# apc (kg/m3)
# =============================================================================
#iris.save(cube38485, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38485.pp')
#iris.save(cube38486, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38486.pp')
#iris.save(cube38487, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38487.pp')
#iris.save(cube38488, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38488.pp')
#iris.save(cube38489, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38489.pp')
#iris.save(cube38490, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38490.pp')
#iris.save(cube38491, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38491.pp')
#iris.save(cube38492, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38492.pp')
#iris.save(cube38493, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38493.pp')
#iris.save(cube38494, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38494.pp')
#iris.save(cube38495, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38495.pp')
#iris.save(cube38496, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38496.pp')
#iris.save(cube38497, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38497.pp')
#iris.save(cube38498, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38498.pp')
#iris.save(cube38499, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/plotting_scripts/diurnal_cycle/apc pm (kg m-3)/s38499.pp')

# =============================================================================
# apk (kg/kg)
# =============================================================================
iris.save(cube34102, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34102.pp')
iris.save(cube34104, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34104.pp')
iris.save(cube34105, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34105.pp')
iris.save(cube34106, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34106.pp')
iris.save(cube34108, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34108.pp')
iris.save(cube34109, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34109.pp')
iris.save(cube34110, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34110.pp')
iris.save(cube34111, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34111.pp')
iris.save(cube34114, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34114.pp')
iris.save(cube34115, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34115.pp')
iris.save(cube34116, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34116.pp')
iris.save(cube34117, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34117.pp')
iris.save(cube34120, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34120.pp')
iris.save(cube34121, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34121.pp')
iris.save(cube34126, '/exports/csce/datastore/geos/users/s1731217/output_ukca/u-av256/dumped_pp_files/June/monthly/s34126.pp')
print('done')



