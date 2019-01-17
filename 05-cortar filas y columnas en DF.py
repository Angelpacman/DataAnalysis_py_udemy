
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ufo = pd.read_csv('http://bit.ly/uforeports')


# In[3]:


ufo.head()


# In[4]:


ufo.shape


# In[5]:


ufo.drop('Colors Reported', axis=1, inplace=True)


# In[6]:


ufo.head()


# In[7]:


ufo.drop(['City','State'], axis=1, inplace=True)


# In[8]:


ufo.head()


# In[9]:


ufo.drop([1,3], axis = 0, inplace=True)


# In[10]:


ufo.head()

