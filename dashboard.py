import streamlit as st
import webbrowser

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.title("================")

tab1, tab2, tab3 = st.tabs(["Dimsum", "Manisan", "Kontak"])
with tab1:
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
with tab2:
    st.write("Manisan Mangga")
    st.write("Rp. 45.000/kg")
    st.image("images/1.jpg")
    st.write("-----------------")
with tab3:
    st.write("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
 
    url = 'https://www.instagram.com/dimsumnyanada'

    if st.button('Instagram'):
        webbrowser.open_new_tab(url)
