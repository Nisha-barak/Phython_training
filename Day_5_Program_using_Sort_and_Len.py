#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=['venkat','rama','sumanth','pujitha','ramesh']
print(list)


# In[ ]:


#Req: Sort a list according to the length of the elements:-


# In[2]:


list=['venkat','rama','sumanth','pujitha','ramesh']
for i in list:
    print(len(i))


# In[3]:


list.sort(key=len)
print(list)


# In[4]:


for i in list:
    print(i.title())


# In[5]:


for i in list:
    print(i.title(),end=" ")


# In[ ]:




