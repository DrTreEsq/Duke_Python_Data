#!/usr/bin/env python
# coding: utf-8

# # Updating DataFrame Data
# 1. Run the cell below to setup a DataFrame of client data

# In[43]:


import pandas as pd
data = {'first': ['Carl', 'Francis', 'Sam'],
        'last':  ['Po',   'Nyguen',  'Smith'],
        'age':   ['32',   '45',      '22'],
        'CH_count':[12,  14, 39]}
clients = pd.DataFrame(data)
clients


# 2. Run the cell below to create a DataFrame with additional clients

# In[44]:


new_data = {'first':['Sue', 'Boya'],
            'last':['Rankler', 'Maple'],
            'age':[93, 12],
            'CH_count':[22, 1]}
new_clients = pd.DataFrame(new_data)
new_clients


# 3. Use the DataFrame `.append()` method to add the new clients.

# In[45]:


clients.append(new_clients)


# 4. Set the age of the first client to 33 by using `.loc[]` to select row 0, column 'age'.

# In[46]:


clients.loc[0]         = 33
clients


# 5. Set the value of all rows in the column 'CH_count' to -1

# In[47]:


clients.loc['CH_count'] = -1
clients


# 6. Use `+=` to add 1 to all rows of 'CH_count'

# In[48]:


clients.loc['CH_count'] += 1
clients


# 7. Use the DataFrame `.replace()` method with the arguments `0, 99` to replace all 0 values in the DataFrame with 99.

# In[50]:


clients.replace(0, 99)
clients

