import streamlit as st
from PIL import Image
import base64

st.title("photos views of the hotel")

image = Image.open("image/pic profile.jpeg")
#st.image(image,caption="The beautiful villas hotel")

image1 =Image.open("image/pic4.jpeg")
#st.image(image1,caption="The fabulous interior")

image2 = Image.open("image/pic3.jpeg")

col1,col2,col3= st.columns(3)
with col1:
    st.image(image1, caption="The fabulous interior")


with col2:
    st.image(image,caption="The beautiful villas hotel")

with col3:
    st.image(image2,caption="The serene interior")

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image/background10.jpg")
img2 = get_img_as_base64("image/background9.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img2}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
