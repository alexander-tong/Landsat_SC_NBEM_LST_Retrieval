# Landsat land surface temperature (LST) retrieval
Home of the land surface temperature (LST) retrieval workflow using the single-channel (SC) NDVI-based emissivity method (NBEM) for Landsat 5/7/8 datasets. As time permits, the workflow will be added. Of course, LST is one of the many ecological relavent (environmental) variables being calculated for downstream analysis as part of the [GLUE project](http://www.globalurbanevolution.com/).

LST may be calculated from a single or multiple thermal infrared bands, depending on the method used. Consequently, LST is a non-trivial quantity to calculate. For operational usage, the SC NBEM is one of the more straightforward approaches for LST retrieval and uses a single thermal infrared sensor (TIRS) band (hence its namesake). However, amongst the LST methods, it is also one of the least accurate (worst case scenario ± 2 K). Then, depending on the needs of a study or project, one should choose whether absolute accurate LST retrieval is a necessity or if the margin of error of LST retrieval proposed by a LST retrieval method is acceptable. Nevertheless, this algorithm requires a few quantities:

- thermal band raster
- at-sensor brightness temperature raster
- NDVI raster
- emissivity raster
- atmospheric functions (calculated via water vapor content or RTM) for known atmospheric profile

Instructions for calculating LST will be added at a later date along with the algorithm as reported by Jiménez-Muñoz et al. 2009. 

## Requirements
Workflow tested and developed using the following packages/libraries:
 - arcpy (ArcMap 10.6.1; Esri ArcGIS Spatial Analyst Extension License) 
 - pandas 0.23.0
 
Future implementation will use GDAL in lieu of arcpy for raster calculations


## NDVI 
[Calculate NDVI](https://github.com/alexander-tong/Landsat_SC_NBEM_LST_Retrieval/blob/master/NDVI/landsat_ndvi.py)

## Emissivity 
The NBEM requires the known emissivity of vegetation and soil. Optionally, NBEM can handle for scenes with water, ice and/or snow. If the emissivity values of surface materials are unknown (e.g., not ground-truthed), a global (mean) constant for each material may be used in lieu and can be calculated from an emissivity library. In this case, hemispherical reflectance from the ASTER Spectral Library can be used to derive emissivity via Kirchoff's Law for a TIRS band at a specified effective wavelength.

[Calculate Emissivity](https://github.com/alexander-tong/Landsat_LST_Retrieval/tree/master/Emissivity) 

## Atmospheric Functions
[Calculate Atmospheric Functions](https://atmcorr.gsfc.nasa.gov/) 

## Land Surface Temperature Main
//insert future link to github repo link
<insert link to github repo link>

## References
Jimenez-Munoz, J. C., Cristobal, J., Sobrino, J. A., Sòria, G., Ninyerola, M., & Pons, X. (2009). Revision of the single-channel algorithm for land surface temperature retrieval from landsat thermal-infrared data. IEEE Transactions on Geoscience and Remote Sensing, 47(1), 339-349. doi:10.1109/TGRS.2008.2007125 

Jimenez-Munoz, J. C., Sobrino, J. A., Skokovic, D., Mattar, C., & Cristobal, J. (2014). Land surface temperature retrieval methods from landsat-8 thermal infrared sensor data. IEEE Geoscience and Remote Sensing Letters, 11(10), 1840-1843. doi:10.1109/LGRS.2014.2312032

Sobrino, J. A., Jiménez-Muñoz, J. C., & Paolini, L. (2004). Land surface temperature retrieval from LANDSAT TM 5. Remote Sensing of Environment, 90(4), 434-440. doi:10.1016/j.rse.2004.02.003 

Sobrino, J. A., Jiménez-Muñoz, J. C., Sòria, G., Romaguera, M., Guanter, L., Moreno, J., . . . Martínez, P. (2008). Land surface emissivity retrieval from different VNIR and TIR sensors. IEEE Transactions on Geoscience and Remote Sensing, 46(2), 316-327. doi:10.1109/TGRS.2007.904834
