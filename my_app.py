#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().system('pip install --upgrade protobuf')


# In[23]:


import pandas as pd
import streamlit as st
import numpy as np

# Add a title to the dashboard
st.title("My Dashboard")

# Add a header to the dashboard
st.header("This is a header")

# Add a text element to the dashboard
st.text("This is some text")

# Add a dataframe to the dashboard
df = pd.read_csv("scopus.csv")
st.dataframe(df)

# Add a chart to the dashboard
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Add a map to the dashboard
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Add a slider to the dashboard
slider = st.slider('Select a value')

# Add a button to the dashboard
button = st.button('Click me')

# Add a checkbox to the dashboard
checkbox = st.checkbox('Check me')


# In[24]:


streamlit run streamlit_app.py

