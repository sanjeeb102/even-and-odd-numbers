#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for x in numbers:
    if not x%2 == 0:
        count_even +=1
    else:
        count_odd +=1
print("Numbers of even numbers is:",count_even)
print("Numbers of odd numbers is:",count_odd)

