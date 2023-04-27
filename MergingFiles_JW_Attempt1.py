#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing pandas and numpy
import pandas as pd
import numpy as np


# In[2]:


#Reading in patient file
patient = pd.read_csv("patient.csv")
patient


# In[3]:


#Reading in diagnosis file
diagnosis = pd.read_csv("diagnosis.csv")
diagnosis


# In[4]:


#Merge patient file with diagnosis file
ChronicCoughDF1 = pd.merge(patient, diagnosis, how='inner', left_on = 'patient_id', right_on = 'patient_id')
ChronicCoughDF1


# In[6]:


#Dropping unneccesary columns in the ChronicCough file
    #These include "derived_by_TriNetX", "reason_yob_missing", "death_date_source_id", "source_id_x", "source_id_y"
ChronicCoughDF2 = ChronicCoughDF1.drop(columns=["derived_by_TriNetX", "reason_yob_missing", 
                                                "death_date_source_id","source_id_x", "source_id_y"])
ChronicCoughDF2


# In[ ]:


#Creating the new variable documenting the number of cough diagnosis per patient
    #We want to have each unique "patient_id" to have the same count
    #The count should be based on each "encounter_id"
    #The ICD code for chronic cough is 'R05.3' 
ChronicCough = ChronicCoughDF2.assign(cough_dx=)

