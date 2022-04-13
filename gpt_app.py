import app1
import app2
import app3
import app4
import app5
import app6
import streamlit as st

st.set_page_config(page_title="NewNative", page_icon="🟢", layout="centered")

# Pages as key-value pairs
PAGES = {
    "Dashboard": app1,
    "Summarization": app2,
    "Q&A": app3,
    "Explain": app4,
    "Notes": app5,
    "Long Text": app6,
    # "GPT-3 Sandbox": app3,
}

st.sidebar.title("Navigation:")

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
