# pylint: disable=missing-module-docstring
import pathlib
from pathlib import Path
import duckdb
import streamlit as st

(Path() / "data").mkdir(exist_ok=True)

DB_PATH = pathlib.Path("data/exercises_sql_tables.duckdb")

if not DB_PATH.exists():
    with open("init_db.py", encoding="utf-8") as file:
        exec(file.read())  # pylint: disable=exec-used


def check_user_query(user_query: str) -> None:
    """
    Checks that user's query is correct by comparing the number of columns and their values
    """
    result = con.execute(user_query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError:
        st.write("Some columns are missing")


con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    available_theme_df = con.execute("SELECT DISTINCT theme from memory_state").df()
    theme = st.selectbox(
        "What would you like to review?",
        available_theme_df["theme"].unique(),
        index=None,
        placeholder="Select a theme",
    )
    if theme:
        st.write("You selected: ", theme)
        SELECT_EXERCISE_QUERY = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        SELECT_EXERCISE_QUERY = "SELECT * FROM memory_state"

    exercise = (
        con.execute(SELECT_EXERCISE_QUERY)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", encoding="utf-8") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")


if query:
    check_user_query(query)

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab2:
    st.write(answer)
