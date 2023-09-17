#!/usr/bin/env python
# coding: utf-8

# # Manipulating DataFrames
# 1. Run the cell below to setup this lab.

# In[11]:


import pandas as pd
data = {'first': ['Carl', 'Francis', 'Sam'],
        'last':  ['Po',   'Nyguen',  'Smith'],
        'age':   ['32',   '45',      '22']}
clients = pd.DataFrame(data)
clients


# 2. Rename the columns from 'first' to 'First', 'last' to 'Last', and 'age' to 'Age'. Provide the 'columns' argument with a dictionary mapping current column names to the new names.

# In[12]:


clients.rename(columns= {'first':'First', 'last':'Last','age':'Age'}, inplace=True)
clients


# 3. Create a new column 'Name' by combining the values from the columns 'First' and 'Last'. You can use addtion between the columns: `clients.First + ' ' + clients.Last` to create the values.

# In[13]:


clients['Name'] = clients.First + ' ' + clients.Last
clients


# 4. Drop the columns 'First' and 'Last' using the `.drop()` method. The columns parameter takes a list of column names to drop.

# In[14]:


clients.drop(columns= ['First','Last'], inplace=True)
clients

