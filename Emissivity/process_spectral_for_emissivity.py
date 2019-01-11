# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:58:24 2018

@author: Alex
"""

def main():
#    directory = r'D:\GLUE Datasets\Spectra\manmade'
    directory = r'D:\GLUE Datasets\Spectra\ecospeclib-1541789735754'
#    material = 'manmade'
    material = 'soil'
    landsat_sensor = 8
    process_emissivity(directory,material,landsat_sensor)

def process_emissivity(directory,material,landsat_sensor):
    '''
    Description: 
        computes the average emissivity for materials from ASTER spectral response \n\
        curves from the ASTER Spectral Library. Emissivity values are used in the \n\
        calculation of land surface temperature.
    
    WARNING: only tested with manmade and soil spectra files; modify effective wavelength \n\
             values in try/except statements as necessary
    
    Args: 
        directory (str): specify directory of .txt files from ASTER Spectral Library 
        material (str): specify material type as given by the file from ASTER Spectral Library 
                       (e.g., if manmade.concrete.constructionconcrete.solid.all.0598uuucnc.jhu.becknic.spectrum, then 'manmade')
        landsat_sensor (int): specify landsat sensor; currently only accepts 5, 7, or 8
        
    Returns:
        no returns or exchanges
    '''
    import os
    import pandas as pd 
    
    material_type = []
    df_list = []
    
    headers_mean = ['Material', 'wavelength', '% reflectance','reflectance','emissivity'] 
    df_select_mean = pd.DataFrame(columns=headers_mean)
    
    for root, dirnames, filenames in os.walk(directory):
        for file in range(len(filenames)):
            if filenames[file].endswith('spectrum.txt'):
    #            if 'tir' in filenames[file]:    #only for non-photosythethic or vegetation; not applicable for man-made
                if material in filenames[file]:  
                    count = 0
                    title = []
                    spectra_raw = []
                    spectra_cleaned = []
                    df_combine = pd.DataFrame()
                    
                    with open(os.path.join(root,filenames[file]) ,'r') as infile:
        
                        for line in infile:
                            if count == 0:
                                title.append(line.rstrip('\n')) 
                                material_type.append(title[0][6:])  
                                
                            elif count > 20:
                                spectra_raw.append('NaN' + '\t' + line)
                            count += 1
                          
                        headers = ['Material','wavelength','% reflectance']  
                        
                        
        #                print material_type
                            
        #                count = 0
                        #remove '\n' and convert '\t' to ','
                        for i in range(len(spectra_raw)):
                            #clean and separate
                            strip_n = spectra_raw[i].rstrip('\n')
                            replace_tab = strip_n.split('\t')
                            
                            # convert values and re-combine
                            title = replace_tab[0]
                            wavelength = float(replace_tab[1])
                            reflectance = float(replace_tab[2])
                            combined = [title, wavelength, reflectance]
                            
                            # make multiple lists 
                            spectra_cleaned.append(combined)
                            
        #                    print spectra_cleaned
                            #empty list for re-population
                            combined = []
                            
        #                print spectra_cleaned[-1]
                        
        #bob = zip(spectra_cleaned, spectra_cleaned,spectra_cleaned,spectra_cleaned)
        #
        #for i in range(len(bob)):
        #    bob[i].strip('(','')
        #
        #ls_of_ls = [[i,j] for i,j in zip(spectra_cleaned,spectra_cleaned)]
        #df = pd.DataFrame(ls_of_ls)
        
        #                df_count = 0 
                        
                        # while len of all lists not 0, continue 
                        df = pd.DataFrame(spectra_cleaned, columns=headers)
                        
                        #calculate emissivity: create new columns 
                        df['reflectance'] = df['% reflectance']/100
                        df['emissivity'] = 1 - df['reflectance']
                        
                        # find effective wavelength; will be different, so factor for all cases
                        try:
                            if landsat_sensor == 8: # 10.895 um
                                df_select = df[(df['wavelength'] >= 10.89) & (df['wavelength'] <= 10.9)]
#                                print df_select
                                
                            # fix such that it takes the average value from 10.2 and 10.3; not necessary for this wavelength
                            elif landsat_sensor == 7: # 11.269 um (Revision of the Single-Channel Algorithm for Land Surface Temperature Retrieval From Landsat Thermal-Infrared Data)
                                # only works for soil spectra
                                df_select = df[(df['wavelength'] >= 11.26) & (df['wavelength'] <= 11.28)]
#                                print df_select
                                
                            # fix such that it takes the average value from 10.4 and 10.5 
                            # WARNING BELOW RANGE IS SET BASED ON SOIL TXT WAVELENGTH SAMPLING INTERVALS; WILL CHANGE WITH OTHER ASTER SPECTRAL CURVE TXT DATASETS
                            elif landsat_sensor == 5: # 11.457 um (Revision of the Single-Channel Algorithm for Land Surface Temperature Retrieval From Landsat Thermal-Infrared Data)
                                # get average value between 2 values; saves as series and all rows become float; not as a dataframe 
                                df_select = df[(df['wavelength'] >= 11.44) & (df['wavelength'] <= 11.47)].mean(axis = 0) 
                                # need to re-add name to series in order to be able to append to dataframe 
                                df_select = df_select.rename(index = df[(df['wavelength'] >= 11.44) & (df['wavelength'] <= 11.47)].index[0])
                                # append new row to list 
                                df_select_mean = df_select_mean.append(df_select)   
                                # at first column, convert row from float to string to allow for material name to added 
                                df_select_mean[['Material']] = df_select_mean[['Material']].astype(str)

#                                print df_select
                                # grab index of first of two items that were averaged in previous step 
#                                df_select_mean.index = df[(df['wavelength'] >= 11.44) & (df['wavelength'] <= 11.47)].head(1)
     
                        except:
                            pass
                        
                        # set material name from previous list 
                        if (landsat_sensor == 8 or landsat_sensor == 7): 
                            # get value at index, and replace with material type name (index, col_name)
                            df_select.at[df_select.index[0], 'Material'] = material_type[0]
                            print df_select
                            
                            # convert values to list for processing
                            df_select_val_process = df_select.values.tolist()
                            
                        elif landsat_sensor == 5:
                            # get name at index                         
                            df_select_mean.at[df_select_mean.index[0], 'Material'] = material_type[0]
                            print df_select_mean
                            
                            # convert values to list for processing
                            df_select_val_process = df_select_mean.values.tolist()
                            
                        # remove each material name from end of list as it cycles through all txt files;
                        # such that each txt gets its original material name before processing end
                        material_type.pop(-1)
                        
                        df_list.append(df_select_val_process)
                    
                
                        # empty container for next val to be put into dataframe
                        df_select_mean = pd.DataFrame(columns=headers_mean)
                    
                    # once all txt have cycled, append to new list for final output                    
                    df_list_cleaned = []
                    for i in range(len(df_list)):
                        df_list_cleaned.append(df_list[i][0])
                        
                    headers_final = ['Material','wavelength','% reflectance','reflectance','emissivity']  
                    df_analysis = pd.DataFrame(df_list_cleaned, columns=headers_final)
                    
                    # get mean value of emissivity for x material
                    df_analysis['emissivity'].mean()
                    
                    df_analysis['emissivity']
                    df_analysis[['Material','emissivity']]
                    df_analysis.head()  
    
    
    print (df_analysis[['Material','emissivity']])        
    print ('\n' + 'Average emissivity of all {0} materials is {1}'.format(material,round(df_analysis['emissivity'].mean(),4)))
 
    
main() 
