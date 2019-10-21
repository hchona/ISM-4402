#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame (data = GradeList, columns = ['Names', 'Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[3]:


df.plot()
displayText = "Wow!"
xloc = .5
yloc = 76
xtext = 10
ytext = 0
plt.annotate(displayText,
             xy = (xloc,yloc),
             xytext = (xtext,ytext),
             xycoords = ('axes fraction','data'),
             textcoords = 'offset points')


# In[ ]:




