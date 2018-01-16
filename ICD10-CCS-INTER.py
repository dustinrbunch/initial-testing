# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:14:56 2018

@author: BUNCHKDL
"""

import pandas as pd

ICD10_CCSdef=pd.read_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/ICD10_CCS_testfile.csv")
ICD10_CCSdef.head()

CCS_code_def=pd.read_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/CCS-code-definition-list.csv")
CCS_code_def.head()

d=[]

for index, row in ICD10_CCSdef.iterrows():
    
    if "ICD10CM" in ICD10_CCSdef.iloc[index,4]:
        
        d.append(row)
        
df=pd.DataFrame(d)
df
df.to_csv("C:/Users/bunchkdl/Documents/GitHub/initial-testing/ICD10CM_Clean.csv")