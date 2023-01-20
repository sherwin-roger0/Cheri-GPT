import app1
import app2
import streamlit as st

PAGES = {
    "Cheri - AI": app1,
    "Neytiri - AI": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
