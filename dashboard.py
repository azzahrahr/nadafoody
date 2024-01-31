import streamlit as st
import webbrowser

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.title("================")

tab1, tab2, tab3 = st.tabs(["Dimsum/Lumpia", "Manisan", "Kontak"])
with tab1:
    st.header("Dimsum Ayam")
    st.header("Rp. 50.000")
    st.image("images/ayam.jpg")
    st.write("-----------------")
    st.header("Dimsum Rumput Laut")
    st.header("Rp. 50.000")
    st.image("images/rumput.jpg")
    st.write("-----------------")
    st.header("Dimsum Udang")
    st.header("Rp. 50.000")
    st.image("images/udang.jpg")
    st.write("-----------------")
    st.header("Dimsum Kepiting")
    st.header("Rp. 50.000")
    st.image("images/kepiting.jpg")
    st.write("-----------------")
    st.header("Lumpia")
    st.header("Rp. 35.000")
    st.image("images/kepiting.jpg")
with tab2:
    st.header("Manisan Mangga")
    st.header("Rp. 45.000/kg")
    st.image("images/rumput.jpg")
    st.write("-----------------")
    
with tab3:
    st.subheader("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
        if st.button('Instagram'):
            webbrowser.open_new_tab('https://www.instagram.com/dimsumnyanada')
