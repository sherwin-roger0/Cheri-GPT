
def app():

    import streamlit as st
    from streamlit_chat import message
    import os
    import openai
    from dotenv import load_dotenv

    load_dotenv()
    openai.api_key = os.getenv('OPEN_API')
    
    st.balloons()


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

    form = st.form(key='form')
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
            if title=='hi' or title=="Hi":
                response.choices[0].text="hello"
            update_second(str(response.choices[0].text))
            st.code(response.choices[0].text)
            message(title,is_user=True,key=str(os.urandom(16).hex()))


    sound = st.empty()
    sound.audio("hello.mp3")
