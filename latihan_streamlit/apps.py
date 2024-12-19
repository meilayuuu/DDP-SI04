import streamlit as st


# st.title("Hallo Guys")
# st.markdown("Tebak siapa ini?")
# st.image("0.jpg", caption="Ini pacar aku 😘")

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung 🤑")

pg = st.navigation(
    {
     "Menu Utama" : [dashboard], 
     "Transaksi" : [nabung],
        
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()