#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Dog:
    """A simple attempt to model a dog"""
    
    def __init__(self,name,age):
        """Initialising name and age attributes"""
        self.name = name
        self.age = age
        print('This Worked')
    def sit(self):
        """Simulate a dog in respose to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
              """Simulate a dog in response to a rollover command"""
              print(f"{self.name} is now rolling over")


# In[22]:


xobj = Dog('Bruno',3)


# In[23]:


xobj.sit()


# In[24]:


xobj.roll_over()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




