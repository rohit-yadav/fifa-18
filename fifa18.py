
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
# 
# 
# ##### `personal_df` table
# - Remove unmaned column
# 
# 
# ##### `position_df` table
# - Remove unmaned column
# 
# 
# ##### `complete_data_df` table
# - Remove unmaned column
# 
# **Tidiness**
