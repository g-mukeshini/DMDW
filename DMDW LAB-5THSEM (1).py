#!/usr/bin/env python
# coding: utf-8

# DMDW LAB - 5TH SEM

# BY CHANDAN MOHANTY
# ROLL NO: 20CSE012
# SEC: 'C'
# 

# Dataset : Virat Kholi's 71 Century 

# Lib importing

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset= pd.read_csv(r'C:\Users\91824\Downloads\71 Centuries of Virat Kohli.csv')
dataset.head()


# In[3]:


dataset.head(10)


# In[4]:


#viewing the statstical description of the dataset
dataset.describe()


# In[5]:


#dropping the features that dont require 
dataset.drop(['Unnamed: 14'],inplace=True, axis=1)
dataset.head()


# In[6]:


dataset.describe()


# In[7]:


# checking the information of the dataset
dataset.info()


# In[8]:


dataset.isnull().sum()


# Replacing the missing values using Statstical methods:
# Mean
# Mode
# Median

# In[9]:


dataset['Strike Rate']=dataset['Strike Rate'].fillna(dataset['Strike Rate'].mean())
dataset['Strike Rate']


# In[10]:


dataset['Strike Rate'].isnull().sum()   # this indicates there is no more missing values in the column 'Strike Rate'


# In[11]:


dataset['Strike Rate'].mean()


# In[12]:


dataset['Strike Rate'].max()


# In[13]:


dataset['Strike Rate'].min()


# In[14]:


dataset['Strike Rate']=dataset['Strike Rate'].fillna(dataset['Strike Rate'].median())
dataset['Strike Rate']


# In[15]:


dataset['Strike Rate']=dataset['Strike Rate'].fillna(dataset['Strike Rate'].mode())
dataset['Strike Rate']


# In[16]:


dataset.head()


# In[17]:


#representation in boxplot

f, axes = plt.subplots(1,2,figsize = (14,10))

sns.boxplot(dataset['Score'], ax=axes[0])
sns.boxplot(dataset['Strike Rate'],ax=axes[1])


# In[18]:


#Binning 
def binning(col, cut_points, lables=None):
    minval=col.min()
    maxval=col.max()
    break_points=[minval]+cut_points+[maxval]
    print(break_points)
    if not lables:
        lables = range(len(cut_points)+1)
    colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
    return colBin


# In[19]:


cut_points= [130,180]
labels=["Best","OUTSTANDING","EXTRA-ORDINARY"]
dataset["SCORE_TYPE"]=binning(dataset['Score'],cut_points,labels)
dataset


# In[21]:


# min -max normalization

# first copy the data from main dataset into another dataset

norml_dataset = dataset.copy()

for score in norml_dataset.iloc[:,0:1]:
    norml_dataset[score]=(norml_dataset[score] - norml_dataset[score].min()) / (norml_dataset[score].max() - norml_dataset[score].min())

norml_dataset.head()


# In[ ]:




