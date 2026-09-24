# pylint: disable=missing-module-docstring
import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
Orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
Cookie juice,2.5
Chocolatine,2
Muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
select * from beverages
cross join food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme",
    )

    st.write("You selected: ", option)

with st.sidebar:
    option = st.selectbox(
        "What owuld you like to review?",
        ("Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme",
    )

st.write("You selected: ", option)

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.write(beverages)
    st.write("table: food_items")
    st.write(food_items)
    st.write("expected:")
    st.write(solution_df)

with tab2:
    st.write(ANSWER_STR)
