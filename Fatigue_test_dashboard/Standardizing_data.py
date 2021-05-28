#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import os


# In[16]:



compression_opts = dict(method ='zip', archive_name='out.csv')

col=['Machine_N_cycles', 'Machine_Load', 'Machine_Displacement', 'DIC_index', 'DIC_N_cycles',
     'DIC_exx', 'DIC_eyy', 'DIC_exy', 'DIC_crack_length', 'Th_N_cycles', 'Th_time',
     'Th_specimen_max', 'Th_specimen_mean', 'Th_chamber', 'Th_uppergrips', 'Th_lowergrips']


dat = pd.read_csv('/Volumes/GoogleDrive/.shortcut-targets-by-id/306/FatigueDataPlatform files & data/Use cases/Use case:Vahid_P1/Raw data Vahid/Conf-0.1-47-b-St.txt', sep='\t',header=0, decimal = ",")

df = pd.DataFrame(columns = col)
df.Machine_N_cycles = dat.N
df.Machine_Load = dat.Stress
df.Machine_Displacement = dat.Strain

df.to_csv(path_or_buf='/Users/scottmatthewssalmon/Desktop/github/CCFatigue/Outputs/Vahid_std.csv', index=False)

#print(dat)
#print(df)
#df.to_csv('out.zip', index=False, compression=compression_opts)


# In[17]:



compression_opts = {'method' : 'zip'}

col2=['Machine_N_cycles', 'Machine_Load', 'Machine_Displacement', 'DIC_index', 'DIC_N_cycles',
      'DIC_exx', 'DIC_eyy', 'DIC_exy', 'DIC_crack_length', 'Th_N_cycles', 'Th_time',
      'Th_specimen_max', 'Th_specimen_mean', 'Th_chamber', 'Th_uppergrips', 'Th_lowergrips']
#machine = pd.read_csv('Essai1.steps.trends.csv', sep=';',header=0)



machine = pd.read_csv('/Volumes/GoogleDrive/.shortcut-targets-by-id/306/FatigueDataPlatform files & data/Use cases/Data template - Shayan/Database Platform/Raw Data/DIC_Vic2D/CA_Pl1_S60_R0.1_LR1_1_cycles.txt', sep='\t',header=0, decimal=",")
dic = pd.read_csv('/Volumes/GoogleDrive/.shortcut-targets-by-id/306/FatigueDataPlatform files & data/Use cases/Data template - Shayan/Database Platform/Raw Data/DIC_Vic2D/exx_mean.csv', sep=',',header=1)
thermal = pd.read_csv('/Volumes/GoogleDrive/.shortcut-targets-by-id/306/FatigueDataPlatform files & data/Use cases/Data template - Shayan/Database Platform/Raw Data/Thermal/Temp-Time.dat', sep='\t',header=6, index_col=False)


df2 = pd.DataFrame(columns = col2)

df2.Th_time = thermal.Time
df2.Th_specimen_max = thermal.Specimen_Max
df2.Th_specimen_mean = thermal.Specimen_Mean
df2.Th_chamber = thermal.Chamber
df2.Th_uppergrips = thermal.filter(items = ['Upper Grips'])
df2.Th_lowergrips = thermal.filter(items = ['Lower Grips'])

df2.DIC_index = dic.filter(items = ['Index [1]'])
df2.DIC_exx = dic.filter(items = ['exx [1] - engr.'])
df2.DIC_eyy = dic.filter(items = ['eyy [1] - engr.'])
df2.DIC_exy = dic.filter(items = ['exy [1] - engr.'])

df2.Machine_N_cycles = machine.filter(items = ['Nb of cycle'])
df2.Machine_Load = machine.ai0
df2.Machine_Displacement = machine.ai1

df2 = df2[['Th_N_cycles','Th_time', 'Th_specimen_max', 'Th_specimen_mean',
           'Th_chamber', 'Th_uppergrips', 'Th_lowergrips', 'DIC_index', 'DIC_N_cycles', 'DIC_exx',
           'DIC_eyy', 'DIC_exy', 'Machine_N_cycles', 'Machine_Load', 'Machine_Displacement']]


#print(thermal)


#print(dic)
print(df2)
df2.to_csv(path_or_buf='/Users/scottmatthewssalmon/Desktop/github/CCFatigue/Outputs/Shayan_std.csv', index=False)
#df2.to_csv(r'/Users/scottmatthewssalmon/Desktop/Projet de Master', index = False)


# In[19]:


metadata_col = ['File_Name', 'File_Format', 'File_size', 'TC_Temp', 'TC_RH', 'TC_CM', 'TC_GP',
                'Geo_L', 'Geo_w', 'Geo_T', 'Measuring_equipment', 'CM_FiberMat', 'CM_FiberGeo',
                'CM_AreaDen', 'CM_Adhesive', 'LA_CureTime', 'LA_CureTemp', 'LA_CurePres', 'LA_FiberCont',
                'LA_StackSeq','LT', 'Fat_Type', 'R_Ratio', 'P_maxFat', 'Sig_maxFat',
                'QS_TestType', 'Fracture', 'Fracture_Mode']

meta_df = pd.DataFrame(columns = metadata_col, index = ['value', 'units'])







meta_df.File_Name.value = 'VAH_20210420_FAT_RAW_001'
meta_df.File_Name.units = '[–]'

meta_df.File_Format.value = 'CSV'
meta_df.File_Format.units = '[–]'

meta_df.File_size.value = '1.8'
meta_df.File_size.units = '[MB]'

meta_df.TC_Temp.value = 20
meta_df.TC_Temp.units = '[°C]'

meta_df.TC_RH.value = 'Not specified'
meta_df.TC_RH.units = '[%]'

meta_df.TC_GP.value = 'Not specified'
meta_df.TC_GP.units = '[MPa]'

meta_df.Geo_L.value = 250
meta_df.Geo_L.units = '[mm]'

meta_df.Geo_w.value = 25
meta_df.Geo_w.units = '[mm]'

meta_df.Geo_T.value = 2.25
meta_df.Geo_T.units = '[mm]'

meta_df.Measuring_equipment.value = 'Instron 8800'
meta_df.Measuring_equipment.units = '[–]'

meta_df.CM_FiberMat.value = 'E-glass fiber'
meta_df.CM_FiberMat.units = '[–]'

meta_df.CM_FiberGeo.value = 'Unidirectional'
meta_df.CM_FiberGeo.units = '[–]'

meta_df.CM_AreaDen.value = 425
meta_df.CM_AreaDen.units = '[g/m^2]'

meta_df.LA_CureTime.value = 8
meta_df.LA_CureTime.units = '[hr]'


meta_df.LA_CureTemp.value = 70
meta_df.LA_CureTemp.units = '[°C]'

meta_df.LA_CurePres.value = 'Not specified'
meta_df.LA_CurePres.units = '[Pa]'

meta_df.LA_FiberCont.value = 62
meta_df.LA_FiberCont.units = '[%]'

meta_df.LA_StackSeq.value = '(±45)_2s'
meta_df.LA_StackSeq.units = '[–]'

meta_df.LT.value = 'Fatigue'
meta_df.LT.units = '[–]'

meta_df.Fat_Type.value = 'CA'
meta_df.Fat_Type.units = '[–]'

meta_df.R_Ratio.value = 0.1
meta_df.R_Ratio.units = '[–]'

meta_df.Sig_maxFat.value = 47.4
meta_df.Sig_maxFat.units = '[MPa]'

meta_df.to_csv(path_or_buf='/Users/scottmatthewssalmon/Desktop/github/CCFatigue/Outputs/Vahid_metadata.csv', index=False)


print(meta_df)


# In[ ]:





# In[ ]:



