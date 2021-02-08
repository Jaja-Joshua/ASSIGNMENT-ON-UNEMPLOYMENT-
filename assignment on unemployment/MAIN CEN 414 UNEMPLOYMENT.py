#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


unemployment_2017 = pd.read_csv(r"C:\Users\JAJA\Documents\unemployment_2017.csv")
unemployment_2017.head()


# In[3]:


unemployment_2017.drop(index = 0,axis = 0,inplace = True)


# In[4]:


unemployment_2017 = unemployment_2017.sort_values(by = "UNEMPLOYMENT RATE", ascending = False)


# In[5]:


unemployment_2017.head()


# In[6]:


unemployment_2017.dtypes


# In[7]:


import plotly

import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio


# In[8]:


fig = px.bar(unemployment_2017, y='STATES', x='UNEMPLOYMENT RATE', orientation='h', color='UNEMPLOYMENT RATE', text = 'UNEMPLOYMENT RATE')
fig.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(
    title={
        'text':"UNEMPLOYMENT RATE FOR THE YEAR 2017 Q1",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},template = "plotly_white", height = 900, width = 1400)


# In[9]:


import json


# In[10]:


nigeria_states = json.load(open(r"C:\Users\JAJA\Documents\nigeria_geojson.json", "r"))


# In[11]:


nigeria_states["features"][0]["properties"].keys()


# In[12]:


state_id_map = {}
for feature in nigeria_states["features"]:
    feature["id"] = feature["properties"]["statecode"]
    state_id_map[feature["properties"]["state"]] = feature["id"]


# In[13]:


unemployment_2017["id"] = unemployment_2017["STATES"].apply(lambda x: state_id_map[x])


# In[15]:


fig = px.choropleth(unemployment_2017, geojson=nigeria_states, locations='id', color='UNEMPLOYMENT RATE',scope = "africa", hover_name = "STATES", hover_data = ["TOTAL UNEMPLOYED"])
fig.update_geos(fitbounds="locations", visible=False)
fig.show()


# In[ ]:




