import streamlit as st
import pandas as pd
import modules as md
import asyncio

if 'queue' not in st.session_state:
   st.session_state['queue'] = []

def submit_btn_clicked():
  meta_data = md.RenderMetadata()
  meta_data.input_image_format = st.session_state.image_format
  meta_data.output_video_format = st.session_state.video_format
  asyncio.run(md.render_video(meta_data))
  
  # st.session_state['queue'].append(task)

# text_input_input_form = st.text_input("Input Image Format (ex: /storage/01_data/images/%04d_raw_image.bmp)", key="image_format")
# text_input_output_form = st.text_input("Output Video Format (ex: /storage/01_data/result.mp4)", key="video_format")

# st.form_submit_button(label="Submit", help=None, on_click=None, args=None, kwargs=None,   type="secondary", disabled=False, use_container_width=False)
form = st.form(key='my-form')
form.text_input("Input Image Format (ex: /storage/01_data/images/%04d_raw_image.bmp)", key="image_format", placeholder="/storage/01_data/images/%04d_raw_image.bmp")
form.text_input("Output Video Format (ex: /storage/01_data/result.mov)", key="video_format", placeholder="/storage/01_data/result.mov")
submit = form.form_submit_button('Render Video', on_click=submit_btn_clicked)

st.text(body=st.session_state['queue'])