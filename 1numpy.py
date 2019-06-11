#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


one=[2,3,4]
one


# In[5]:


arrays=np.array(one)
arrays


# In[6]:


ok=([1,2,3],[2,4,5], [4,3,5])
print(ok)


# In[7]:


ok=np.array(ok)
ok


# In[8]:


n=[[1,2,3],[2,34,5]]
n


# In[9]:


n=np.array(n)
n


# In[16]:


np.arange(0,11)


# In[19]:


np.arange(0,11,2)


# In[20]:


np.zeros(3)


# In[23]:



np.zeros((3,2))


# In[24]:


np.ones(4)


# In[26]:


np.ones((2,2))


# In[27]:


np.linspace(0,5,100)


# In[28]:


np.eye(4)


# In[30]:


np.random.rand(5)


# In[31]:


np.random.randn(2)


# In[32]:


np.random.randn(4,4)


# In[34]:


np.random.randint(1,100)


# In[ ]:




