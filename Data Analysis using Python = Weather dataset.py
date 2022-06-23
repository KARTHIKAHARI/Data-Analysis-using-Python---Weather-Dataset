#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


data = pd.read_csv(r"C:\Users\karth\Downloads\1. Weather Data.csv")


# In[6]:


data


# In[7]:


data.head()


# In[8]:





# In[9]:


data.shape


# In[10]:


data.index


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[14]:


data['Weather'].unique()


# In[15]:


data.nunique()


# In[16]:


data.count()


# In[17]:


data['Weather'].value_counts()


# In[18]:


data.info()


# In[19]:


### WindSpeed Values in the data


# In[20]:


data.nunique()


# In[22]:


data['Wind Speed_km/h'].nunique()


# In[23]:


data['Wind Speed_km/h'].unique()     


# In[24]:


data[data.Weather == 'Clear']


# In[27]:


#groupby() 
data.groupby('Weather').get_group('Clear')


# In[28]:


#No of times the Windspeed was exactly 4 km/hr
data[data['Wind Speed_km/h']== 4]


# In[29]:


#Null Values in Data
data.isnull().sum()


# In[34]:


#Rename COLUMN Weather as Weather Condition
data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True )


# In[35]:


data.head()


# In[36]:


#Mean Visibility
data.Visibility_km.mean()


# In[38]:


#Std Deviation of Pressure Column
data.Press_kPa.std()


# In[39]:


#Variance of Relative Humidity
data['Rel Hum_%'].var()


# In[40]:


#Instances where SNOW was recorded
data[data['Weather Condition']== 'Snow']


# In[41]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[43]:


data[(data['Wind Speed_km/h']> 24) & (data['Visibility_km'] == 25)]


# In[44]:


#Mean Value of each Column against each Weather Condition

data.groupby('Weather Condition').mean()


# In[45]:


#Min and Max value of each column against Weather Condition

data.groupby('Weather Condition').min()


# In[46]:


#Max

data.groupby('Weather Condition').max()


# In[47]:


data.head()


# In[56]:


#Weather is fog
data[data['Weather Condition'] == 'Fog']


# In[57]:


#Weather is clear and visibility>40
data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[60]:


#Weather is clear and humidity>50 or visibility >40 
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km']>40)]


# In[ ]:




