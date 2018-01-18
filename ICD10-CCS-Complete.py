# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:02:00 2018

@author: BUNCHKDL
"""
import time
import random
import pandas as pd
then = time.time() #Time before the operations start

ICD10_CCSdef=pd.read_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/ICD10CM_Clean.csv", usecols=['ICD10 CLASSIFICATION 1', 'CCS Diagnosis Definition', 'ICD10 ID'])
ICD10_CCSdef.head()

CCS_code_def=pd.read_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/CCS-code-definition-list.csv",usecols=['CCS Diagnosis Code', 'CCS Diagnosis Definition'])
CCS_code_def.head()

for index3, row3 in ICD10_CCSdef.iterrows():
    for index2, row2 in CCS_code_def.iterrows():
        if  CCS_code_def.loc[index2, 'CCS Diagnosis Definition'] == ICD10_CCSdef.loc[index3, 'CCS Diagnosis Definition']:
            ICD10_CCSdef.loc[index3, 'CCS Diagnosis Code']=CCS_code_def.loc[index2, 'CCS Diagnosis Code']
            break
        
ICD10_CCSdef.to_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/ICD10CM_CCS_complete.csv")

now = time.time() #Time after it finished
print("It took: ", now-then, " sec")