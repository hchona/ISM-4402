#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = 'datasets/axisdata.csv'
df = pd.read_csv(Location)
df.head()


# In[3]:


df ['Cars Sold'].mean()


# In[4]:


df ['Cars Sold'].max()


# In[7]:


df ['Cars Sold'].min()


# In[8]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[9]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[12]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[14]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[16]:


import matplotlib.pyplot as plt
import pandas as pd
CarsSold=[2,6,6,3,2]
HoursWorked=[39,46,42,38,33]
Fname=['Jada', 'Nicole', 'Tanya', 'Ronelle', 'Brad']
HoursList=zip(CarsSold, HoursWorked, Fname)
df=pd.DataFrame(data=HoursList,
               columns=['Cars Sold', 'Hours Worked', 'Name'])
df2=df.set_index(df['Name'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')
df2.plot(kind="bar")


# In[17]:


import matplotlib.pyplot as plt
import pandas as pd
CarsSold=[3.57,4.17]
Trained=['No', 'Yes']
Training=zip(CarsSold, Trained)
df=pd.DataFrame(data=Training,
               columns=['Cars Sold', 'Trained'])
df2=df.set_index(df['Trained'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')
df2.plot(kind="bar")


# In[ ]:




