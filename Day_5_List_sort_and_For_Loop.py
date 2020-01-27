#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Organishng a list:


# In[5]:


cars=['benz','audi','toyota','bmw']
print(cars)
for i in cars:
    print(i.title())


# In[7]:


for i in cars:
    print(i.title(),end=" ")


# In[10]:


print(cars)
for i in cars:
    print(i.upper())


# In[11]:


type(cars)


# In[ ]:


#Req:Print the list in a alphabatical order:


# In[16]:


cars.sort()------->It will make the changes permanantly
print(cars)
for i in cars:
    print(i.title(),end=" ")


# In[ ]:


#Req: Print the list in reverse order:


# In[22]:


cars.sort(reverse=True)
print(cars)
for i in cars:
    print(i.title(),end=" ")


# In[ ]:


#Sorting a list temporarily with a sorted function:


# In[23]:


cars.sorted()


# In[ ]:


#how to find the length of the list:
#No. of elements in a list


# In[25]:


list(cars)
len(cars)


# In[ ]:


#Working with looping conditions:
1.For loop
2.While loop


# In[30]:


my_students=['venkat','sumanth','rama','pujitha','kamesh']
for i in my_students:
    print(i.title(),end=" ")


# In[32]:


for student in my_students:
    print(student.title())


# In[63]:


my_students=['venkat','sumanth','rama','pujitha','kamesh']
print(f"{my_students[1].title()},Keep up the good work,maintain tha same")


# In[71]:


my_students=['venkat','sumanth','rama','pujitha','kamesh']
for student in my_students:
    print(f"{student.title()},Keep up the good work,maintain the same")


# In[ ]:





# In[ ]:





# In[ ]:




