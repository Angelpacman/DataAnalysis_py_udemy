
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


movies = pd.read_csv('http://bit.ly/imdbratings')


# In[4]:


movies.head()


# In[5]:


movies.describe()


# In[7]:


movies.dtypes


# In[13]:


type(movies)


# In[14]:


movies.describe(include=['object'])

