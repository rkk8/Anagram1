#!/usr/bin/env python
# coding: utf-8

# Anagram ex: atom : moat, arc : car, rat : tar, etc
# 
# first I will be to to convert the name(string) to list. 
# Then I will sort both lists.
# If the sorted lists are equal they are an anagram..
# 

# In[12]:


def ana_gram(s1,s2):
    l1=list(s1).sort()
    l2=list(s2).sort()
    
    if len(s1)==len(s2) and l1 == l2:
        statement1='These two words are anagrams!'
        return print(statement1)
    else:
        statement2='These two words are not anagrams'
        return print(statement2)


# In[13]:


ana_gram('rat','tar')


# In[14]:


ana_gram('spat','taps')


# In[15]:


ana_gram('desert','dessert')


# In[ ]:




