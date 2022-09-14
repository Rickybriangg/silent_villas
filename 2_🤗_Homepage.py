#import pandas as pd
import base64
import streamlit as st
from PIL import Image

EMAIL = "rickybriangg@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/profile.php?id=100077698713869",
    "Instagram": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}

st.set_page_config(page_title="silent villa plams",page_icon=':hotel:',layout="wide")


st.sidebar.success("Select the page above")



logo = Image.open("image/logo.png")
logo2 =Image.open("image/logo2.png")


col5,col6 = st.columns(2)
with col5:
    st.image(logo)

with col6:
    st.image(logo2)


st.write("----")
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#st.title("SILENT VILLA PLAMS")
#st.markdown("Affordable ,reliable,explict and comfortability")

#st.caption("A place where everyone desires")
#st.markdown("The silent villas plams in silent environment ")
st.subheader("The serene features")
col7,col8 = st.columns(2)
with col7:
    st.write("---")
    st.write("""-✔Located in South Coast Diani, 
    -   ✔We Offers two (2)-bedroom units spread in the lavish green gardens.
   -  ✔The luxury residence is positioned in a prime location a few meters from the beach. 
  -   ✔The roof terrace provides you with gorgeous ocean views.
-   ✔	Enjoy the unbeatable Rates now for a 2- Bedroom unit that can accommodates 4-6 Pax.
"""
              )
with col8:
    st.write("""
-	✔Open plan dining, living and a fully equipped kitchen on self-catering.
-	✔Spacious bedrooms open onto a large private balcony
-	✔Swimming pool access 
-	✔Long-term stay available 
"""
            )


@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image/pic profile.jpeg")
img2 = get_img_as_base64("image/background2.jpg")

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

