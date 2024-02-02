import streamlit as st

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.title("-----------------")

tab1, tab2, tab3 = st.tabs(["Dimsum/Lumpia", "Manisan", "Kontak"])
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.header("Dimsum Ayam")
        st.header("Rp. 50.000")
        st.image("images/ayam.jpg")
        st.write("----------------")
        st.header("Lumpia")
        st.header("Rp. 35.000")
        st.image("images/kepiting.jpg")
    with col2:
        st.header("Dimsum Rumput Laut")
        st.header("Rp. 50.000")
        st.image("images/rumput.jpg")
    with col3:
        st.header("Dimsum Udang")
        st.header("Rp. 50.000")
        st.image("images/udang.jpg")
    with col4:
        st.header("Dimsum Kepiting")
        st.header("Rp. 50.000")
        st.image("images/kepiting.jpg")
    
with tab2:
    st.header("Manisan Mangga")
    st.header("Rp. 45.000/kg")
    st.image("images/rumput.jpg")
    st.write("-----------------")
    
with tab3:
    st.subheader("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
    st.link_button("Instagram", "https://www.instagram.com/dimsumnyanada")
