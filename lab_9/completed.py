#!/usr/bin/env python
# coding: utf-8

# # Comprehensions and Generators

# 1. Write a list comprehension which returns the square of each number from 0 to 15

# In[1]:


[x**2 for x in range(16)]


#  2. The expression `x%4==0` will return `True` if 4 is a factor of `x`. Write a list comprehension which will return numbers from 0 to 20 which have 4 as a factor. 

# In[3]:


[x%4==0 for x in range (21)]


# 3. Write a generator function which will return the string 'foo' every fifth call, and 'moo' otherwise.

# In[ ]:


def foo_moo():
    i = 0
    while True:
        if i%5==0:
            print('foo')      
        else:
            i += 1
            print('moo')
            
fm = foo_moo()

for _ in range(11):
    print(next(fm))


# 4. A comprehension using curly brackets will produce a dictionary. Set the variable 'name' to your name and use it to create a dictionary 

# In[13]:


name = 'EMS'
items = zip(list(name), list(range(len(name))))

{x:y for x,y in items}

