# LST-Retrieval

Home of the land surface temperature (LST) retrieval workflow using the single-channel NDVI-based emissivity method (NBEM) for Landsat 5/7/8 datasets. As time permits, the workflow will be added and updated. Of course, LST is one of the many ecological relavent (environmental) variables being calculated for downstream analysis as part of the [GLUE project](http://www.globalurbanevolution.com/).

LST may be calculated from a single or multiple thermal infrared bands, depending on the method used. Consequently, LST is a non-trival quantity to calculate. For operational usage, the single-channel NBEM method is one of the more straightforward approaches for LST retrieval, but amongst the LST methods, is also one of the least accurate (worst case scenario ± 3 K). Nevertheless, this algorithm requires a few quantities:

- thermal band raster
- at-sensor brightness temperature raster
- NDVI raster
- emissivity raster
- atmospheric functions or water vapor content of the atmospheric profile


