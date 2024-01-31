import streamlit as st
import webbrowser

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.title("================")

options=["Home", "Menu", "Contact"]  # required

selected_option = st.sidebar.selectbox('Select an option', options)

if selected_option == "Home":
    st.title(f"Selamat datang")

if selected_option == "Menu":
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
    
if selected_option == "Contact":
    st.write("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
 
    url = 'https://www.instagram.com/dimsumnyanada'

    if st.button('Instagram'):
        webbrowser.open_new_tab(url)
