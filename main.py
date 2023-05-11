import streamlit as st
import pandas as pd
import modules as md
import asyncio

if 'queue' not in st.session_state:
  st.session_state['queue'] = pd.DataFrame(columns=['Input Image Format', 'Output Video Format'])

def add_btn_clicked():
  df:pd.DataFrame = st.session_state['queue']
  if st.session_state.image_format == '' or st.session_state.image_format == None:
    return
  if st.session_state.video_format == '' or st.session_state.video_format == None:
    return
  df.loc[len(df.index)] = [st.session_state.image_format, st.session_state.video_format]

def remove_btn_clicked():
  df:pd.DataFrame = st.session_state['queue']
  df.drop(index=[len(df.index)-1], inplace = True)

def render_btn_clicked():
  df:pd.DataFrame = st.session_state['queue']
  queue = df.values
  df.drop(df.index, inplace=True)
  placeholder = st.empty()
  for pram in queue:
    placeholder.info(f"Start Rendering... \n  {pram[0]} ----- > {pram[1]}]")
    meta_data = md.RenderMetadata()
    meta_data.input_image_format = pram[0]
    meta_data.output_video_format = pram[1]
    result = md.render_video(meta_data)
    print(f"{pram} -> {result}")
    if result == 256:
      placeholder.error(f"Fail :: {pram}")
    else:
      placeholder.success(f"Complete :: {pram}")

def render_main_page():
  st.title("App :: Images -> Video")
  left, right = st.columns([2,1])
  with left:
    form = st.form(key='my-form')
    form.text_input("Input Image Format (ex: /storage/01_data/images/%04d_raw_image.bmp)", key="image_format", placeholder="/storage/01_data/images/%04d_raw_image.bmp")
    form.text_input("Output Video Format (ex: /storage/01_data/result.mov)", key="video_format", placeholder="/storage/01_data/result.mov")
    submit = form.form_submit_button('Add Queue', on_click=add_btn_clicked, use_container_width=True)
  with right:
    st.button(label="Remove last item", on_click=remove_btn_clicked, type='primary', use_container_width=True)
    st.button(label="Render Video", on_click=render_btn_clicked, type='secondary', use_container_width=True)
  st.text("Render Queue")
  st.dataframe(st.session_state['queue'], use_container_width=True)

render_main_page()