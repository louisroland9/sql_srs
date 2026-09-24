# pylint: disable=missing-module-docstring
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
select * from beverages
cross join food_items
"""

#solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme",
    )

    st.write("You selected: ", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
    st.write(exercise)

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)

#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")

# tab1, tab2 = st.tabs(["Tables", "Solution"])

# with tab1:
#     st.write("table: beverages")
#     st.write(beverages)
#     st.write("table: food_items")
#     st.write(food_items)
#     st.write("expected:")
#     st.write(solution_df)


# with tab2:
#     st.write(ANSWER_STR)
