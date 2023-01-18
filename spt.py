import streamlit as st
from streamlit_chat import message

import openai
openai.api_key = "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"
st.set_page_config(page_title="Cheri-AI")
st.balloons()
import os

if "key" not in st.session_state:
    st.session_state["key"]=[]
    st.session_state["value"]=[]

def update_first():
    st.session_state["key"].append(title)
    st.session_state["value"].append(True)

def update_second(value):
    st.session_state["key"].append(value)
    st.session_state["value"].append(False)

st.header('Cheri AI created by Dr.Sherwin Roger :purple_heart:')

container = st.container()

form = st.form(key='my_form')
title=form.text_input(label='Enter some text')
form.form_submit_button(label='Submit',on_click=update_first,type='secondary')

with container:

    if title:
        for i,j in zip(st.session_state["key"],st.session_state["value"]):

            if i!='':
                if j==True:
                    message(str(i),is_user=j,key=str(os.urandom(16).hex()))
                else:
                    st.code(i)

        response = openai.Completion.create(
            prompt=title,
            model="text-davinci-003",
            temperature=0.5,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        if title=='hi':
            response.choices[0].text="hello"
        update_second(str(response.choices[0].text))
        st.code(response.choices[0].text)
        message(title,is_user=True,key=str(os.urandom(16).hex()))


sound = st.empty()
sound.audio("hello.mp3")
