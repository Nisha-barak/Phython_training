#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionary of similar objects:-


# In[3]:


fav_language={'swetha':'Python','Prashant':'Java','Nisha' :'Swift', 'Narasima' :'C'}


# In[5]:


Language=fav_language['Narasima'.title()]


# In[8]:


print(f"Narasima's favourite language is {Language}")


# In[9]:


{'user_name':'Faiyaz_94',
 'email_ID' :'Codetraining01',
 'First_name' : 'Faiyaz',
 'Last_name' : 'Shaik',}


# In[ ]:


# Looping through dictionaries:-


# In[10]:


user_0={'user_name':'Faiyaz_94',
 'email_ID' :'Codetraining01',
 'First_name' : 'Faiyaz',
 'Last_name' : 'Shaik',}


# In[12]:


for key,value in user_0.items():
    print(f"\nkey:{key}")
    print(f"\nvalue:{value}")


# In[13]:


for a,b in user_0.items():
    print(f"\nkey:{a}")
    print(f"\nvalue:{b}")


# In[ ]:


# Req:-Only to get keys


# In[14]:


for x in user_0.keys():
    print(x)


# In[ ]:


# Req:-Only to get value    


# In[16]:


for y in user_0.values():
    print(y)


# In[ ]:





# In[ ]:





# In[ ]:




