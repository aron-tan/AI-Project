import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Question 2 - Vaccine Distribution Modelling")

st.header("Result for each state:")

df = pd.read_csv("result.csv")

st.write(df)



