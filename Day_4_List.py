#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#introduction to list data type:

List is a collection of items in a particular order.
List is a mutable data type.


# In[51]:


#how to define a list:------>[]
students=['mansi','dhananjay','vijay','nisha','azeem']


# In[8]:


type(students)


# In[52]:


print(students)


# In[40]:


for i in students:
    print(i.title(), end =" ")


# In[ ]:


#how to access the elements in the list:
By using the concept of indexing !!
Indexing starts from zero.


# In[ ]:


Req:- To print mansi name on the console


# In[15]:


print(students[0].title())


# In[16]:


print(students[2].title())


# In[24]:


message=f"You are doing a good job,{students[2].title()}"


# In[25]:


print(message)


# In[27]:


#Reverse indexing
print(students[-1].title())


# In[ ]:


#changing,adding,removing elements in a list:


# In[ ]:


1. Modify/change elements in a list


# In[29]:


print(students)


# In[ ]:


Req:-changing azeem name to priyanka


# In[53]:


students[4]='priyanka'


# In[54]:


print(students)


# In[55]:


for i in students:
    print(i.title())


# In[ ]:


#Adding elements to the list:


# In[56]:


students.append('kishore')----->append will add the elements at the end of the list.


# In[57]:


print(students)


# In[58]:


for i in students:
    print(i.title(), end=" ")


# In[ ]:


#Req:Adding object to a specific place


# In[59]:


students.insert(2,'chintu')


# In[60]:


print(students)


# In[61]:


for i in students:
    print(i.title())


# In[ ]:


#Removing elements from the list


# In[62]:


print(students)


# In[63]:


del students[0]


# In[64]:


print(students)


# In[66]:


for i in students:
    print(i.title(), end=" ")


# In[ ]:


#Removing elements by using the pop method:-this will not delete permanantly


# In[67]:


print(students)


# In[68]:


students.pop()----->last item will be removed by default


# In[69]:


print(students)


# In[70]:


students.pop(-2)


# In[71]:


print(students)


# In[73]:


students.pop(0)


# In[74]:


print(students)


# In[ ]:




