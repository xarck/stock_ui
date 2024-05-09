import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("results.csv")
df = df.iloc[:,1:]

def color_predicted_trend(value):
    if value == "bullish":
        color = "green"
    elif value == "bearish":
        color = "red"
    elif value == "neutral":
        color = "yellow"
    else:
        color = "black"
    return f"background-color: {color}"

styled_df = df.style.applymap(color_predicted_trend, subset=df.columns[1:])

st.dataframe(styled_df)