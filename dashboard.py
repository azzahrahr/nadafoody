import streamlit as st

st.title("Nada Shop")
st.image("images/ayam.jpg")
st.divider()

tab1, tab2, tab3 = st.tabs(["Dimsum/Lumpia", "Manisan", "Kontak"])
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Dimsum Ayam")
        st.write(''':red[Rp. 50.000]''')
        st.image("images/ayam.jpg")
        st.divider()
        st.subheader("Lumpia")
        st.subheader("Rp. 35.000")
        st.image("images/kepiting.jpg")
    with col2:
        st.subheader("Dimsum Rumput Laut")
        st.write(''':red[Rp. 50.000]''')
        st.image("images/rumput.jpg")
    with col3:
        st.subheader("Dimsum Udang")
        st.write(''':red[Rp. 50.000]''')
        st.image("images/udang.jpg")
    with col4:
        st.subheader("Dimsum Kepiting")
        st.write(''':red[Rp. 50.000]''')
        st.image("images/kepiting.jpg")
    
with tab2:
    st.subheader("Manisan Mangga")
    st.subheader("Rp. 45.000/kg")
    st.image("images/manisan1.jpg")
    st.write("-----------------")
    
with tab3:
    st.subheader("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
    st.link_button("Instagram", "https://www.instagram.com/dimsumnyanada")
