
# coding: utf-8

# # Introduction
# 
# FIFA, also known as FIFA Football or FIFA Soccer, is a series of association football video games or football simulator, released annually by Electronic Arts under the EA Sports label.

# In[1]:


import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


directory = os.getcwd()


# In[3]:


os.chdir(directory + '//data')


# In[4]:


attribute = pd.read_csv('PlayerAttributeData.csv', low_memory=False)
personal = pd.read_csv('PlayerPersonalData.csv', low_memory=False)
position = pd.read_csv('PlayerPlayingPositionData.csv', low_memory=False)
complete_data = pd.read_csv("CompleteDataset.csv", low_memory=False)


# **Make a copy of the data frame**

# In[5]:


attribute_df = attribute.copy()
personal_df = personal.copy()
position_df = position.copy()
complete_data_df = complete_data.copy()


# ### Assess

# In[6]:


attribute_df.head()


# In[7]:


personal_df.head()


# In[8]:


position_df.head()


# In[9]:


complete_data_df.head()


# **Quality**
# 
# ##### `attribute_df` table
# - Remove unmaned column
# - Numeric data types are string
# - ID should be sting not integer
# - Values have an additon numbers with them too. e.g. For `ID` `213661` has acceleration as `70+9`
# 
# ##### `personal_df` table
# - Remove unmaned column
# - Numeric data type are string
# - ID should be sting not integer
# 
# ##### `position_df` table
# - Remove unmaned column
# - Numeric data type are string
# - ID should be sting not integer
# 
# ##### `complete_data_df` table
# - Remove unmaned column
# - Numeric data type are string
# - ID should be sting not integer
# 
# **Tidiness**

# In[10]:


attribute_df.info()


# In[11]:


personal_df.info()


# In[12]:


position_df.info()


# In[13]:


complete_data_df.info()


# ### Cleaning

# ##### `attribute_df` , `personal_df`, `position_df` : **Remove columns**
# 
# **Define:**
# 
# The unwanted columns should be removed
# 
# **Code:**

# In[14]:


attribute_df = attribute_df.drop(['Unnamed: 0'], axis=1)
personal_df = personal_df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
position_df = position_df.drop(['Unnamed: 0'], axis=1)
complete_data_df = complete_data_df.drop(['Unnamed: 0'], axis=1)


# **Test**

# In[15]:


attribute_df.head(2)


# In[16]:


personal_df.head(2)


# In[17]:


position_df.head(2)


# In[18]:


complete_data_df.head(2)


# In[19]:


attribute_df[attribute_df.ID==213661]


# In[20]:


attribute_df.iloc[309]

