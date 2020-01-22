#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.Understanding Variables of Phython
2.Introduction to String
3.Declaration of String
4.String built-in Methods


# In[ ]:


#Understanding Variables of Phython:
    1.No spaces between variable names
    2.No number should be used in starting of variable declaraion
    3.No special characters should be used in begining of variable name


# In[4]:


1. No spaces between variable names

Example: First name = "Nisha" ---Invalid due to space inbetween
        print(First name)


# In[5]:


firstname="Nisha"
print(firstname)


# In[6]:


First_name="Nisha"
print(First_name)


# In[7]:


2. No number should be used in starting of variable declaraion
Example:1name="Nisha" ----invalid due to number in begining
    print(1name)


# In[9]:


name1="Nisha"
print(name1)


# In[18]:


3.No special characters should be used in begining of variable name
Example : $x=23
    print($x)


# In[ ]:


#Data types in Phython:
1.String  ---->str
2.List  ------>List
3. Tuples  ---> Tuples
4. Dictionary-->Dict


# In[ ]:


#Introduction to String
String is a series of characters.
String is a imutable data type.


# In[ ]:


#Declaration of String
Possible ways to declare a string:-


# In[27]:


x='This is a string'
type(x)


# In[28]:


y="This is also a string"
type(y)


# In[29]:


z="""This is also considered as a string"""
type(z)


# In[30]:


#String built-in Methods
name="nisha barak"
print(name)


# In[31]:


print(name.title())


# In[32]:


print(name.upper())


# In[33]:


print(name.lower())


# In[36]:


#Concept of "f string"
first_name="nisha"
middle_name=" "
last_name="barak"
full_name=f"{first_name}{middle_name}{last_name}"
print(full_name.title())

