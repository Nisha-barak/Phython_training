#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name="nisha"
last_name="barak"
full_name=f"{first_name} {last_name}"
print(full_name)


# In[2]:


print(full_name.title())


# In[7]:


#Enhancement of the Code:
print(f"Welcome,great to see you again !, {full_name.title()}")


# In[10]:


#Adding white spaces:
print("Python")
print("\tphython")----->delimited--->print---->on tab


# In[11]:


print("Java\nSwift")---->\n to print in a new line.


# In[13]:


print("Languages:\nPython\nC\nJavaScript")


# In[14]:


print("Languages:\n\tPhython\n\tC\n\tJavaScript")


# In[15]:


#stripping of white spaces!
Fav_lang=" Python"
print(Fav_lang)


# In[ ]:


#Methods for stripping:
1. Lstrip
2. Rstrip
3. Strip


# In[26]:


Fav_lang.lstrip()


# In[28]:


Fav_lang="Python "
print(Fav_lang)
Fav_lang.rstrip()


# In[31]:


Name_1=" My name is Nisha Barak "
print(Name_1)
Name_1.strip()


# In[34]:


Name_2="and My name is Nisha Barak"
print(Name_2)
Name_2.strip("and ")


# In[40]:


Name_3="and My name is Nisha Barak."
print(Name_3)
Name_3.strip("and .")


# In[57]:


Name_4="and My name is nisha barak.\ni want to learn followng languages:\n\tphython\n\tc\n\tjavascript"
print(Name_4.title())


# In[63]:


print(Name_4.lstrip("and ").title())


# In[ ]:




