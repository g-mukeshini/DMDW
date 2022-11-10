#!/usr/bin/env python
# coding: utf-8

# DMDW LAB 5TH SEM 

# BY G. MUKESHINI ROLLNO-20CSE108  SEC-'C'

# DATASET: STUDENT PERFORMANCE 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv(r'C:\Users\91824\Downloads\archive (10)\exams.csv')
dataset.head()


# In[3]:


dataset.shape


# In[4]:


dataset.info()


# In[5]:


#check if any null values
dataset.isnull().sum()


# In[6]:


dataset.describe()


# In[7]:


#using statstical methods 

#median
dataset['math score']=dataset['math score'].fillna(dataset['math score'].median())
dataset['math score']

#mean

dataset['reading score']=dataset['reading score'].fillna(dataset['reading score'].mean())
dataset['reading score']


#mode

dataset['writing score']=dataset['writing score'].fillna(dataset['writing score'].mode())
dataset['writing score']


# In[9]:


#box plot representation

fig = plt.figure(figsize=(10,10))
plt.boxplot(dataset['math score'])
plt.show()


# In[10]:


fig = plt.figure(figsize=(10,10))
plt.boxplot(dataset['reading score'])
plt.show()


# In[13]:


fig = plt.figure(figsize=(10,10))
plt.boxplot(dataset['writing score'])
plt.show()


# In[15]:


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


# In[ ]:





# In[16]:


cut_points= [75,90]
labels=["BEST","OUTSTANDING","EXTRA-ORDINARY"]
dataset["GRADES "]=binning(dataset['math score'],cut_points,labels)
dataset


# In[29]:


# min -max normalization

# first copy the data from main dataset into another dataset

norml_dataset = dataset.copy()

for score in norml_dataset.iloc[:,5:8]:
    norml_dataset[score]=(norml_dataset[score] - norml_dataset[score].min()) / (norml_dataset[score].max() - norml_dataset[score].min())

norml_dataset.head()


# In[ ]:




