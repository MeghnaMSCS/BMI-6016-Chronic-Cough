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


#Merge patient file with the diagnosis file
ChronicCoughDF1 = pd.merge(patient, diagnosis, how='inner', left_on = 'patient_id', right_on = 'patient_id')
ChronicCoughDF1


# In[5]:


#Dropping unneccesary columns in the ChronicCoughDF1 dataframe and saving as ChronicCoughDF2
    #These include "derived_by_TriNetX", "reason_yob_missing", "death_date_source_id", "source_id_x", "source_id_y"
ChronicCoughDF2 = ChronicCoughDF1.drop(columns=["derived_by_TriNetX", "reason_yob_missing", 
                                                "death_date_source_id","source_id_x", "source_id_y"])
ChronicCoughDF2


# In[6]:


# Create a list of conditions that identifies if the ICD code relates to chronic cough
conditions = [
    (ChronicCoughDF2['code'] == 'R05.3' ) | (ChronicCoughDF2['code'] == '786.2' ),
    (ChronicCoughDF2['code'] != 'R05.3' ) & (ChronicCoughDF2['code'] != '786.2' )
    ]

# Create values Yes is '1' and No is '0'
values = ['1', '0']

# Create a new column 'c_cough_yn' and use np.select to assign values to it using our lists as arguments
ChronicCoughDF2['c_cough_yn'] = np.select(conditions, values)

# display updated DataFrame
ChronicCoughDF2.head()


# In[7]:


# Count the number of chronic cough codes in the dataframe
print(ChronicCoughDF2['c_cough_yn'].value_counts()['1'])


# In[8]:


#Create a new data frame that counts the number of chronic cough diagnoses each patient has
df_count = ChronicCoughDF2.groupby('patient_id')['c_cough_yn'].apply(lambda x: (x=='1').sum()).reset_index(name='count')
df_count


# In[9]:


# Merge the df_count data frame with the ChronicCoughDF2 dataframe to create the new data set 
FINALDF = pd.merge(ChronicCoughDF2, df_count, how='inner', left_on = 'patient_id', right_on = 'patient_id')
FINALDF


# In[10]:


FINALDF.to_csv('chronic_cough.csv')


# The FINALDF dataset is ready for a quality assessment to confirm that everything was merged correctly.
