import streamlit as st  
import pandas as pd
import duckdb


tab1, tab2, tab3 = st.tabs(["tab1", "tab2", "tab3"])
data = {"a":[1,2,3], "b":[4,5,6]}
df = pd.DataFrame(data)


with tab1:
    st.write(df)
    input_sql = st.text_area(label="Entrez votre requête SQL")
    df_output = duckdb.sql(input_sql)
    st.write(df_output)


with tab2:
    input_text = st.text_area(label="Entrez votre texte")
    st.write(input_text)

with tab3:
    st.write("Allez le Stade")