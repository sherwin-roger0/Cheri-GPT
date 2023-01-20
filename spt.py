import streamlit as st
import hydralit_components as hc
import app1
import app2

st.set_page_config(layout="wide",initial_sidebar_state='collapsed',)


menu_data = [

]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Cheri-AI',
    login_name='Neytiri-AI',
    hide_streamlit_markers=False, 
    sticky_nav=True,
    sticky_mode='pinned', 
)

st.info(f"{menu_id}")

if menu_id=="Cheri-AI":
    app1.app()
else:
    app2.app()
