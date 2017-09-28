# stacking_fault_multi Calculation

- - -

**Lucas M. Hale**, [lucas.hale@nist.gov](mailto:lucas.hale@nist.gov?Subject=ipr-demo), *Materials Science and Engineering Division, NIST*.

**Chandler A. Becker**, [chandler.becker@nist.gov](mailto:chandler.becker@nist.gov?Subject=ipr-demo), *Office of Data and Informatics, NIST*.

**Zachary T. Trautt**, [zachary.trautt@nist.gov](mailto:zachary.trautt@nist.gov?Subject=ipr-demo), *Materials Measurement Science Division, NIST*.

Version: 2017-09-27

[Disclaimers](http://www.nist.gov/public_affairs/disclaimer.cfm) 
 
- - -

## Introduction

The __stacking_fault_multi__ calculation evaluates the full 2D generalized stacking fault map for an array of shifts along a specified crystallographic plane. A regular grid of points is established and the generalized stacking fault energy is evaluated at each.

__Disclaimer #1__: The system's dimension perpendicular to the fault plane should be large to minimize the interaction of the free surface and the stacking fault.

__Disclaimer #2__: Currently, the rotation capabilities of atomman limit this calculation such that only cubic prototypes can be rotated. Properties of non-cubic structures can still be explored, as long as the configuration being loaded has the plane of interest perpendicular to one of the three box vectors.