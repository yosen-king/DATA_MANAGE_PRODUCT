# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:45:49 2022

@author: youjs
"""

# streamlit_app.py

import streamlit as st
import mysql.connector
import pandas as pd

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from macro_data;")
head = run_query("SHOW COLUMNS from macro_data;")
head = [i[0] for i in head]

# create the dataframe
df = pd.DataFrame(rows[0:],columns=head)



# display the dataframe
st.markdown("<center>数据库数据展现<center>",unsafe_allow_html  = True)
st.dataframe(df)
# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")
    
    
    














