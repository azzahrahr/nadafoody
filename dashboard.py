import streamlit as st

st.title("Nada Shop")
st.image("images/1.png")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Dimsum/Lumpia", "Manisan", "Kue Lebaran", "Kontak"])
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
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/manisan1.jpg")
        st.write(''':red[Rp.0]''')
    with col2:
        st.image("images/manisan2.jpg")
        st.write(''':red[Rp.0]''')
    with col3:
        st.image("images/manisan5.jpg")
        st.write(''':red[Rp.0]''')
    with col4:
        st.image("images/manisan7.jpg")
        st.write(''':red[Rp.0]''')

with tab3:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/snack1.jpg")
        st.write(''':red[Rp.0]''')
        st.divider()
        st.image("images/snack5.jpg")
        st.write(''':red[Rp.0]''')
    with col2:
        st.image("images/snack2.jpg")
        st.write(''':red[Rp.0]''')
        st.divider()
        st.image("images/snack8.jpg")
        st.write(''':red[Rp.0]''')
    with col3:
        st.image("images/snack3.jpg")
        st.write(''':red[Rp.0]''')
        st.divider()
        st.image("images/snack6.jpg")
        st.write(''':red[Rp.0]''')
    with col4:
        st.image("images/snack4.jpg")
        st.write(''':red[Rp.0]''')
        st.divider()
        st.image("images/snack7.jpg")
        st.write(''':red[Rp.0]''')

with tab4:
    st.subheader("Silahkan hubungi kontak yang tersedia untuk melakukan pemesanan.")
    st.link_button("Instagram", "https://www.instagram.com/dimsumnyanada")
