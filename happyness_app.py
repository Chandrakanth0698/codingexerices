import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")
df = pd.read_csv("happy.csv")

x_axis = st.selectbox("Select the data for X axis", options=df.columns)
y_axis = st.selectbox("Select the data for Y axis", options=df.columns)


st.header(f"{x_axis} and {y_axis}")

figure = px.scatter(data_frame=df, x=x_axis, y=y_axis)
st.plotly_chart(figure)
