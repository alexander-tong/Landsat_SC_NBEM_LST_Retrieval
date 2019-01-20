# Landsat land surface temperature (LST) retrieval
Home of the land surface temperature (LST) retrieval workflow using the single-channel NDVI-based emissivity method (NBEM) for Landsat 5/7/8 datasets. As time permits, the workflow will be added and updated. Of course, LST is one of the many ecological relavent (environmental) variables being calculated for downstream analysis as part of the [GLUE project](http://www.globalurbanevolution.com/).

LST may be calculated from a single or multiple thermal infrared bands, depending on the method used. Consequently, LST is a non-trivial quantity to calculate. For operational usage, the single-channel NBEM method is one of the more straightforward approaches for LST retrieval and uses a single thermal infrared (TIRS) thermal band (hence its namesake). However, amongst the LST methods, it is also one of the least accurate (worst case scenario ± 3 K). Then, depending on the needs of a study or project, one should choose whether absolute accurate LST retrieval is a necessity or if the margin of error of LST retrieval proposed by a LST retrieval method is acceptable. Nevertheless, this algorithm requires a few quantities:

- thermal band raster
- at-sensor brightness temperature raster
- NDVI raster
- emissivity raster
- atmospheric functions or water vapor content of the atmospheric profile

Instructions for calculating LST will be added at a later date along with the algorithm as reported by Jiménez-Muñoz et al. 2009. 

# Requirements


# References
Jimenez-Munoz, J. C., Cristobal, J., Sobrino, J. A., Sòria, G., Ninyerola, M., & Pons, X. (2009). Revision of the single-channel algorithm for land surface temperature retrieval from landsat thermal-infrared data. IEEE Transactions on Geoscience and Remote Sensing, 47(1), 339-349. doi:10.1109/TGRS.2008.2007125 

Jimenez-Munoz, J. C., Sobrino, J. A., Skokovic, D., Mattar, C., & Cristobal, J. (2014). Land surface temperature retrieval methods from landsat-8 thermal infrared sensor data. IEEE Geoscience and Remote Sensing Letters, 11(10), 1840-1843. doi:10.1109/LGRS.2014.2312032

Sobrino, J. A., Jiménez-Muñoz, J. C., & Paolini, L. (2004). Land surface temperature retrieval from LANDSAT TM 5. Remote Sensing of Environment, 90(4), 434-440. doi:10.1016/j.rse.2004.02.003 

Sobrino, J. A., Jiménez-Muñoz, J. C., Sòria, G., Romaguera, M., Guanter, L., Moreno, J., . . . Martínez, P. (2008). Land surface emissivity retrieval from different VNIR and TIR sensors. IEEE Transactions on Geoscience and Remote Sensing, 46(2), 316-327. doi:10.1109/TGRS.2007.904834
