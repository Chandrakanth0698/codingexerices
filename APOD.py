import streamlit as st
import requests
st.set_page_config(layout="wide")

url = "https://api.nasa.gov/planetary/apod" \
      f"?api_key={st.secrets['API_key']}"

request = requests.get(url)
content = request.json()
print(content)
st.header("Astronomical image of the day")
st.info(f"Today's Date: {content['date']}")
st.header(content["title"])
st.image(f"{content['hdurl']}")
st.write(f"{content['explanation']}")
