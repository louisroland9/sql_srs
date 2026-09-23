import streamlit as st  
import pandas as pd
import duckdb
import io


csv = """
beverage,price
Orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
Cookie juice,2.5
Chocolatine,2
Muffin,3
"""

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
select * from beverages
cross join food_items
"""

solution = duckdb.sql(answer).df()

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.write(beverages)
    st.write("table: food_items")
    st.write(food_items)
    st.write("expected:")
    st.write(solution)


with tab2:
    st.write(answer)