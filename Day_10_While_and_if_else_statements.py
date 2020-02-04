#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# While Loop:

Having the possibility of the condition


# In[1]:


current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1


# In[8]:


current_number=1
while current_number<=21:
    print(current_number)
    current_number+=2


# In[ ]:


#If Conditions and user input:

Vooting application---->validate---->18 years of age ---->eligible to vote-->if not try next year!!


# In[12]:


age=input("How old are you")
age=int(age)
if age>=18:
    print("\nYou are eligible to vote.")
else:
    print("\nTry next year !!")


# In[ ]:


#Req:Given numby the user in even and odd..
#How to design the application


# In[15]:


num=input("Enter a number and I will tell you its even or odd")
num=int(num)
if num%2==0:
    print("This number is even.")
else:
    print("This number is odd.")


# In[ ]:




