#!/usr/bin/env python
# coding: utf-8

# # DataFrame Apply
# 1. Run the cell below to setup this lab.

# In[36]:


import pandas as pd
data = { 'even': range(20,0,-2),
         'odd':  range(1,21,2)
       }
df = pd.DataFrame(data)
df


# 2. The Python Standard Library includes a built-in funciton `max()`, which returns the maximun value of an iterable input. Use the DataFrame `.apply()` method to get the maximum value of each column.

# In[37]:


df.apply(max)


# 3. Now use the `axis=1` argument with apply to get the maximum value of each row.

# In[38]:


df.apply(max, axis=1)


# 4. Complete the function below so that it will return `True` if the odd value is greater than the even one.

# In[39]:


def odd_bigger(row):
    if row['odd'] > row['even']:
        return True
    return False


# 5. Apply this function to `df` with the axis argument set to 1 to run it on each row.

# In[40]:


g = df.apply(odd_bigger, axis=1)


# 6. Now use the output values to create a new column, 'Odd Bigger' and view `df` to confirm that the values are correct.

# In[41]:


df['Odd Bigger'] = g
df

