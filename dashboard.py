import streamlit as st
from streamlit_option_menu import option_menu as om
import webbrowser

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.title("Selamat Datang :wave:")

selected = option_menu(
         menu_title=None,  # required
         options=["Home", "Menu", "Contact"],  # required
         icons=["house", "list", "envelope"],  # optional
         menu_icon="cast",  # optional
         default_index=0,  # optional
         orientation="horizontal",
)

if selected == "Home":
    st.title(f"Selamat datang")
   
if selected == "Menu":
    st.write("Dimsum Ayam")
    st.write("Rp. 45.000")
    st.image("images/ayam.jpg")
    st.write("-----------------")
    st.write("Dimsum Rumput Laut")
    st.write("Rp. 45.000")
    st.image("images/rumput.jpg")
    st.write("-----------------")
    st.write("Dimsum Udang")
    st.write("Rp. 45.000")
    st.image("images/udang.jpg")
    st.write("-----------------")
    st.write("Dimsum Kepiting")
    st.write("Rp. 45.000")
    st.image("images/kepiting.jpg")
    
if selected == "Contact":
    st.write("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
 
    url = 'https://www.instagram.com/dimsumnyanada'

    if st.button('Instagram'):
        webbrowser.open_new_tab(url)
