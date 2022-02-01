#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
foodsheet = pd.read_csv("/Users/IFE/Downloads/Food.csv")
print(foodsheet)


# In[5]:


food_animalfats = foodsheet[foodsheet['Item'] == 'Animal fats']
food_animalfats[['Y2014', 'Y2017']].sum()


# In[12]:


foodsheet[['Y2015']].mean()


# In[9]:


foodsheet[['Y2015']].std()


# In[14]:


foodsheet[['Y2015']].isnull().sum()


# In[17]:


print(foodsheet['Element Code'].corr(foodsheet['Y2014']))
print(foodsheet['Element Code'].corr(foodsheet['Y2015']))
print(foodsheet['Element Code'].corr(foodsheet['Y2016']))
print(foodsheet['Element Code'].corr(foodsheet['Y2017']))


# In[20]:


food_import = foodsheet[foodsheet['Element'] == 'Import Quantity']
food_import[['Y2014', 'Y2015', 'Y2016', 'Y2017']].sum()


# In[23]:


food_import = foodsheet[foodsheet['Element'] == 'Production']
food_import[['Y2014']].sum()


# In[27]:


food_element_2018 = foodsheet[['Element', 'Y2018']]
print(food_element_2018)


# In[31]:


food_element_2018.groupby(['Element']).sum()


# In[35]:


food_algeria = foodsheet[foodsheet['Area'] == 'Algeria']
food_algeria_2018 = food_algeria[['Element', 'Y2018']]
print(food_algeria_2018)
food_algeria_import_quantity =food_algeria_2018[food_algeria_2018['Element'] == 'Import Quantity']
food_algeria_import_quantity[['Y2018']].sum()


# In[41]:


foodsheet['Area'].unique()


# In[ ]:




