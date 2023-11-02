import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")
uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start camera"):
    # start the camera
    cam_image = st.camera_input("Camera")

if cam_image:
    # Create a pil Image instance
    img = Image.open(cam_image)
    # Convert pil image to gray scale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)
elif uploaded_image:
    up_img = Image.open(uploaded_image)
    gray_upimg = up_img.convert("L")
    st.image(gray_upimg)

st.rerun()