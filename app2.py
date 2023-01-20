def app():  
  import openai
  import streamlit as st
  from dotenv import load_dotenv
  import os

  load_dotenv()
  openai.api_key = os.getenv('OPEN_API')

  st.snow()

  st.header('Neytiri-AI created by Dr.Sherwin Roger :purple_heart:')

  form = st.form(key='my_form')
  title=form.text_input(label='Enter ur imagination to convert it into an image:-')
  form.form_submit_button(label='Submit',type='secondary')

  container=st.container()

  with container:
    if title:
      response = openai.Image.create(
      prompt=title,
      n=1,
      size="512x512"
      )
      image_url = response['data'][0]['url']
      st.image(image_url)