import streamlit as st 

st.title("Halaman Dasboard")
st.image("0.jpg", caption="Nishimura Riki")

#fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(i['Jumlah']
                       for i in st.session_state['total_semua']
                       if i ['Tipe'] == 'Menabung')
    
    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")