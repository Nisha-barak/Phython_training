#!/usr/bin/env python
# coding: utf-8

# In[1]:


cars=['bmw','audi','toyata','benz']


# In[ ]:


#Req: Organise the list in a alphabactical order:
Methods:
    1. Sort() ---->Change permanantly
    2.Sorted()----->change temporarily


# In[ ]:


#Sorted Implementation:-


# In[3]:


print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))


# In[4]:


print(cars)


# In[ ]:


#For Loops:
----Temp variable creation
----maintaining the indentation:
----maintaining the spaces


# In[5]:


students=['vijay','azeem','priyanka','ashok','sri']


# In[ ]:


#Req:-keep up the good job.


# In[6]:


for student in students:
    print(student)


# In[9]:


for student in students:
    print(f" {student.title()},keep up the good job")


# In[10]:


for student in students:
    print(f" {student.title()},keep up the good job")
    
print("\n Thank you all for showing interest in learning python")


# In[ ]:


#Range Function:


# In[ ]:


#Req:-Print the num from 1-20


# In[11]:


for value in range(1,21):
    print(value)


# In[ ]:


#Range declaration--->last num is always exclusive


# In[ ]:


#Req:-Create a list by using the range function:


# In[12]:


numbers=list(range(1,51))
print(numbers)


# In[ ]:


#Req:-Print even numbers 1-50
#Range (Start value, stop value, step count)


# In[14]:


Even_num=list(range(2,51,2))
print(Even_num)


# In[ ]:


#Req:-Print Odd numbers 1-50


# In[20]:


Odd_num=list(range(1,51,2))
print(Odd_num)


# In[ ]:




