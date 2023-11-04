import streamlit as st
from send_email import send_email
import pandas as pd

st.header("Contact Us")
df = pd.read_csv(r"D:\pythonProject\Codingexercise\topics.csv")
with st.form(key="contact_form"):
    user_email = st.text_input("Enter Email address")
    topic_selected = st.selectbox(label="Select a topic", options=df['topic'])
    raw_message = st.text_area("Enter message")
    message = f"""\
Subject: Email from company website

from: {user_email}
topic: {topic_selected}
message:{raw_message}
    """
    button = st.form_submit_button()
    if button:
        send_email(message,password=st.secrets['YOUR_SMTP_GMAIL_PASSWORD'])
        st.info("email sent successfully")

