#!/usr/bin/env python
# coding: utf-8

# This notebook includes the code related to assessing the new data file and the subsequent corrections to the data file.

# In[1]:


#Importing pandas and numpy
import pandas as pd
import numpy as np


# In[2]:


#Reading in chronic cough
ccdf = pd.read_csv('chronic_cough.csv')
ccdf


# In[3]:


#reading in the diagnosis file for reference
dgdf = pd.read_csv('diagnosis.csv')
dgdf


# In[4]:


#reading in the patient file for reference
ptdf = pd.read_csv('patient.csv')
ptdf


# In[5]:


##1
#The patient file had 354,772 unique patient IDs. 
#Check the new file to ensure all were transferred over
print(len(ccdf['patient_id'].unique()))


# In[6]:


##7
#The diagnosis file had 10,878,455 unique encounter ids
#Check the new file to ensure all encounters were transferred
print(len(ccdf['encounter_id'].unique()))


# In[7]:


##2
#Comparing the unique values in each column to the original files
# The total counts in the patient file
print('\nTotal counts for sex:', len(ptdf['sex'].unique()))
print('\nTotal counts for race:', len(ptdf['race'].unique()))
print('\nTotal counts for ethnicity:', len(ptdf['ethnicity'].unique()))
print('\nTotal counts for marital_status:', len(ptdf['marital_status'].unique()))
print('\nTotal counts for year_of_birth:', len(ptdf['year_of_birth'].unique()))
print('\nTotal counts for month_year_death:', len(ptdf['month_year_death'].unique()))
print('\nTotal counts for patient_regional_location:', len(ptdf['patient_regional_location'].unique()))


# In[8]:


#The total counts in the diagnosis file
print('\nTotal counts for code system:', len(dgdf['code_system'].unique()))
print('\nTotal counts for code:', len(dgdf['code'].unique()))
print('\nTotal counts for principal diagnosis indicator :', len(dgdf['principal_diagnosis_indicator'].unique()))
print('\nTotal counts for admitting diagnosis:', len(dgdf['admitting_diagnosis'].unique()))
print('\nTotal counts for reason for visit:', len(dgdf['reason_for_visit'].unique()))
print('\nTotal counts for diagnosis date:', len(dgdf['date'].unique()))


# In[9]:


# The total counts in the new file
print('\nTotal counts for sex:', len(ccdf['sex'].unique()))
print('\nTotal counts for race:', len(ccdf['race'].unique()))
print('\nTotal counts for ethnicity:', len(ccdf['ethnicity'].unique()))
print('\nTotal counts for marital_status:', len(ccdf['marital_status'].unique()))
print('\nTotal counts for year_of_birth:', len(ccdf['year_of_birth'].unique()))
print('\nTotal counts for month_year_death:', len(ccdf['month_year_death'].unique()))
print('\nTotal counts for patient_regional_location:', len(ccdf['patient_regional_location'].unique()))
print('\nTotal counts for code system:', len(ccdf['code_system'].unique()))
print('\nTotal counts for code:', len(ccdf['code'].unique()))
print('\nTotal counts for principal diagnosis indicator :', len(ccdf['principal_diagnosis_indicator'].unique()))
print('\nTotal counts for admitting diagnosis:', len(ccdf['admitting_diagnosis'].unique()))
print('\nTotal counts for reason for visit:', len(ccdf['reason_for_visit'].unique()))
print('\nTotal counts for diagnosis date:', len(ccdf['date'].unique()))


# In[10]:


##3 & 10
#The patient file had 345,928 missing values for month_year_death
#The diagnosis file had 8,619 missing values for encounter id 
    #and 1,498 missing values for code_system
#Check missing values in chronic cough file
ccdf.isna().sum()


# In[11]:


##4
#The birth range in the patient file is 1942-2005
#Check the birth range in the chronic cough file
min_date = ccdf['year_of_birth'].min()
max_date = ccdf['year_of_birth'].max()
print(min_date)
print()
print(max_date)


# In[12]:


##5
#The death date range in the patient file is 10/1961 to 02/2023
#Check the birth range in the chronic cough file
min_d_date = ccdf['month_year_death'].min()
max_d_date = ccdf['month_year_death'].max()
print(min_d_date)
print()
print(max_d_date)


# In[13]:


##6
#Compare year of death with year of birth
#start with converting month_year_death to year_of_death
ccdf['year_of_death'] = ccdf['month_year_death'].fillna(3000).astype(int).astype(str).str[:4].astype(int)


# In[14]:


# compare year_of_birth with year_of_death to see if there is any year of death before year of birth
ccdf['birth_vs_death'] = ccdf['year_of_birth'] > ccdf['year_of_death']
count_true = (ccdf['birth_vs_death'] == True).sum()
print(count_true)


# In[15]:


# compare year_of_birth with year_of_death to see if there is any year of death before or same with year of birth
ccdf['birth_vs_death'] = ccdf['year_of_birth'] >= ccdf['year_of_death']
count_true = (ccdf['birth_vs_death'] == True).sum()
print(count_true)


# In[16]:


# the number of patient that born and die in the same year
selected_rows = ccdf[ccdf['birth_vs_death'] == True]
print(len(selected_rows['patient_id'].unique())) 


# ##7 Has been moved below #1

# In[17]:


##8 & 9
#Compare the data types between patient, diagnosis & chronic cough file
ptdf.dtypes


# In[18]:


dgdf.dtypes


# In[19]:


ccdf.dtypes


# ##10 is associated with 3

# In[20]:


##11
#Are there the same number of icd codes for chronic cough in the new file?
#Identifying the number of icd-9 Chronic cough codes in the diagnosis file
dgdf['code'] = dgdf['code'].astype(str)
rslt786_df = dgdf[dgdf['code'] == '786.2']
rslt786_df


# In[21]:


#Identifying the number of icd-9 Chronic cough codes in the new file
ccdf['code'] = ccdf['code'].astype(str)
rslt786_new = ccdf[ccdf['code'] == '786.2']
rslt786_new


# In[22]:


#Identifying the number of icd-10 Chronic cough codes in the diagnosis file
dgdf['code'] = dgdf['code'].astype(str)
rsltR05_df = dgdf[dgdf['code'] == 'R05.3']
rsltR05_df


# In[23]:


#Identifying the number of icd-10 Chronic cough codes in the new file
ccdf['code'] = ccdf['code'].astype(str)
rsltR05_new = ccdf[ccdf['code'] == 'R05.3']
rsltR05_new


# In[24]:


##12
#Check to make sure that R05.3 is only associated with ICD-10
ccdf[(ccdf['code'] == 'R05.3') & (ccdf['code_system'] == 'ICD-10-CM')].shape[0]


# In[25]:


#Check to make sure that R05.3 is not associated with ICD-9
ccdf[(ccdf['code'] == 'R05.3') & (ccdf['code_system'] == 'ICD-9-CM')].shape[0]


# In[26]:


##13
#Check to make sure that 786.2 is only associated with ICD-9
ccdf[(ccdf['code'] == '786.2') & (ccdf['code_system'] == 'ICD-9-CM')].shape[0]


# In[27]:


#Check to make sure that 786.2 is not associated with ICD-10
ccdf[(ccdf['code'] == '786.2') & (ccdf['code_system'] == 'ICD-10-CM')].shape[0]


# In[28]:


##14
#What is the diagnosis date range?
min_date = ccdf['date'].min()
max_date = ccdf['date'].max()
print(min_date)
print()
print(max_date)


# In[29]:


##15
#Are there any diagnosis dates before a person is born?
#First step is to convert encounter/diagnosis date to year of diagnosis
ccdf['year_of_diagnosis'] = ccdf['date'].astype(int).astype(str).str[:4].astype(int)


# In[30]:


# compare year_of_birth with year_of_diagnosis to see if there is any year of date before year of birth
ccdf['birth_vs_diagnosis'] = ccdf['year_of_birth'] > ccdf['year_of_diagnosis']
count_true_1 = (ccdf['birth_vs_diagnosis'] == True).sum()
print(count_true_1)


# In[31]:


##16
#Are there any diagnosis dates after a person dies?
# compare year_of_death with year_of_diagnosis to see if there is any year of death before year of diagnosis
ccdf['death_vs_diagnosis'] = ccdf['year_of_death'] < ccdf['year_of_diagnosis']
count_true_2 = (ccdf['death_vs_diagnosis'] == True).sum()
print(count_true_2)


# In[32]:


# show all the rows that year of death before year of diagnosis(only these 3 columns: 'year_of_birth', 'year_of_diagnosis','year_of_death')
ccdf[ccdf['death_vs_diagnosis'] == True][['year_of_birth', 'year_of_diagnosis','year_of_death']]


# In[33]:


#Are duplicates present?
# Drop the column 'Unnamed: 0' because this is unneccesary and will aide in removing the duplicates latter
ccdf.drop('Unnamed: 0', axis=1, inplace=True)
#Checking for duplicates
duplicated_rows = ccdf[ccdf.duplicated()]
duplicated_rows


# CORRECTIONS BELOW
# 1)Dropping the missing rows with missing data for encounter_id and code system
# 2)Drop rows with diagnosis after death
# 3)Drop all duplicates

# In[34]:


#drop the rows that encounter_id or code_system are missing
ccdf.dropna(subset=['encounter_id', 'code_system'], inplace=True)


# In[35]:


#Checking to make sure they were removed
ccdf.isna().sum()


# In[36]:


# drop all rows that year of death before year of diagnosis
ccdf = ccdf[ccdf['death_vs_diagnosis'] != True]


# In[37]:


# show all the rows that year of death before year of diagnosis(only these 3 columns: 'year_of_birth', 'year_of_diagnosis','year_of_death')
ccdf[ccdf['death_vs_diagnosis'] == True][['year_of_birth', 'year_of_diagnosis','year_of_death']]


# In[38]:


#dropping duplicates from the table
ccdf = ccdf.drop_duplicates(keep='first')


# In[39]:


#checking to see if any additional duplicates exist
duplicated_rows1 = ccdf[ccdf.duplicated()]
duplicated_rows1


# In[40]:


#Look at dimensions of file
ccdf


# In[41]:


#Remove unneccesary columns created for the data quality assessment
ccdf_final = ccdf.drop(['birth_vs_death','birth_vs_diagnosis','death_vs_diagnosis'], axis=1)


# In[42]:


#Looking at dimensions of final data file.
ccdf_final


# In[ ]:


#Converting assessed and corrected data frame to csv
ccdf_final.to_csv('chroniccough_final.csv',index=False)


# END
