# -*- coding: utf-8 -*-
"""
@author: Alexander Tong

Developed and tested with Python 2.7.15
"""
import os, sys

if sys.version_info[0] != 2:
    print("This script requires Python version 2.xx")
    sys.exit(1)
    
try:
    import arcpy
    
except ImportError as IE:
    print (IE)
    print ("This script requires arcpy to run")
    sys.exit(1)


def NDVI(directory, outpath):  
    '''
   **WARNING** logic is dependent on default Landsat naming convention and must be strictly adhered to.
   
    Description: 
        This function will recursively go into a directory and compute a <spectral index> product\n\
        from composited surface reflectance Landsat datasets. 
    
    arcpy is forcing creation of temporary layers in memory to process. 
    
            Normalized Difference Vegetation Index
            NDVI = NIR - Red / NIR + Red
 
            Landsat 5/7:(Band 4 - Band 3)/(Band 4 + Band 3)
            Landsat 8: (Band 5 - Band 4)/(Band 5 + Band 4) 
            
            Normalized Difference Snow Index
            NDSI = green - SWIR / green + SWIR

            Landsat 5/7:(Band 2 - Band 5/(Band 2 + Band 5) 
            Landsat 8: (Band 3 - Band 6/(Band 3 + Band 6) 

    
    Args:
        directory (str): input directory to be parsed. e.g., 'C:\\inpath'
        outpath (str): specify outpath. e.g., 'C:\\outpath' 
        
    Returns:
        Output derived NDVI from composited Landsat raster 
    
    $ to be implemented: optimize code; reduce amount of lines    
    $ to be implemented: if outpath does not exist, create folder, else nothing
    
    '''
    import os, arcpy 
    from arcpy.sa import *

    arcpy.CheckOutExtension("spatial")
    arcpy.env.overwriteOutput = True
    
    for root, dirnames, filenames in os.walk(directory):
        for file in range(len(filenames)):
            if filenames[file].endswith('sr_composite.tif'):
                
                if os.path.isfile(os.path.join(outpath, filenames[file][:41] + '_NDVI' + '.tif')):
                    print filenames[file][:41] + '_NDVI' + '.tif' + ' already exists!'

                else: 
                    # Landsat 5 and 7
                    if 'LE07' in filenames[file] or 'LT05' in filenames[file]:
                        print filenames[file]

                        arcpy.env.workspace = root 
                        print filenames[file]
                        Band_3 = arcpy.Raster(filenames[file] + '\Band_3')*0.0001  # apply scale factor
                        Band_4 = arcpy.Raster(filenames[file] + '\Band_4')*0.0001  # apply scale facto

                        arcpy.MakeRasterLayer_management(Band_3,'Red_out')
                        arcpy.MakeRasterLayer_management(Band_4,'NIR_out') 

                    # Landsat 8
                    elif 'LC08' in filenames[file]:

                        arcpy.env.workspace = root 
                        print filenames[file]
                        Band_4 = arcpy.Raster(filenames[file] + '\Band_4')*0.0001  # apply scale factor
                        Band_5 = arcpy.Raster(filenames[file] + '\Band_5')*0.0001  # apply scale factor

                        arcpy.MakeRasterLayer_management(Band_4,'Red_out')
                        arcpy.MakeRasterLayer_management(Band_5,'NIR_out') 


                    Num = arcpy.sa.Float(Raster('NIR_out') - Raster('Red_out'))
                    Denom = arcpy.sa.Float(Raster('NIR_out') + Raster('Red_out'))
                    arcpy.MakeRasterLayer_management(Num,'Num_out')
                    arcpy.MakeRasterLayer_management(Denom,'Denom_out') 

                    NDVI = arcpy.sa.Divide('Num_out', 'Denom_out')
                    arcpy.MakeRasterLayer_management(NDVI,'NDVI_out')                         

                    # constrained -1 to 1 
                    NDVI_rescaled = SetNull('NDVI_out', 'NDVI_out','VALUE < -1 OR VALUE > 1' )

                    # fill artifacts with NoData; only true for isolated areas; else large NoData areas are likely cloud, ice/snow/water, edge of water
                    neighborhood = NbrRectangle(3, 3, "CELL")
                    infill_ndvi = arcpy.sa.Con(IsNull(NDVI_rescaled), FocalStatistics(NDVI_rescaled, neighborhood, "MEAN"), NDVI_rescaled)

                    OUTPUT_NDVI = os.path.join(outpath, filenames[file][:41] + '_NDVI' + '.tif')

                    arcpy.CopyRaster_management(infill_ndvi, OUTPUT_NDVI)

                    arcpy.Delete_management('NIR_out')
                    arcpy.Delete_management('Red_out')
                    arcpy.Delete_management('Num_out')    
                    arcpy.Delete_management('Denom_out')
