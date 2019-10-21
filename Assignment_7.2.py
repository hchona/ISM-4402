#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
status = ['Senior', 'Freshman', 'Sophomore', 'Junior', 'Senior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)
df = pd.DataFrame(data = GradeList, columns = ['Grades','Status'])
get_ipython().run_line_magic('matplotlib','inline')
df.plot(kind = 'bar')


# In[6]:


df2 = df.set_index(df['Status'])
df2.plot(kind="bar")


# In[ ]:




