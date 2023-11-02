import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("""Welcome to [Your Company Name], where cutting-edge AI and ML solutions
 meet your unique needs. We specialize in harnessing the power of artificial 
 intelligence and machine learning to drive innovation and efficiency across
  industries. Our expert team is dedicated to crafting customized solutions,
  utilizing sophisticated algorithms and models to provide you with advanced
   analytics and actionable insights.

At [Your Company Name], we pride ourselves on being at the forefront of
 technological advancements. Explore how our intelligent technologies can 
 transform your business and propel you into the future. Join us on the journey 
 to redefine possibilities with AI and ML.

Discover the potential. Experience the innovation. Choose [Your Company Name]
 for a smarter tomorrow.""")

st.subheader("Our Team")
col1, col2, col3 = st.columns(3)
df = pd.read_csv('data.csv')
df1, df2, df3 = df[:4], df[4:8], df[8:]

with col1:
    for index, row in df1.iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df2.iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df3.iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")
