import streamlit as st
import streamlit.components.v1 as components

st.title("親アプリ")

st.write("下に別ページをiframeで埋め込みます。")

components.iframe(
    "https://app-app-deploy-bjzeu3dv6jk9ugrp4y4clq.streamlit.app/embed_app",
    height=800,
    scrolling=True
)
