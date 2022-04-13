import streamlit as st
from model_training_service import Extend


def app():

    # Creating an object of prediction service
    pred = Extend()

    api_key = "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"

    # Using the streamlit cache
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input, api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Create long text from short text")
        st.write("From short text, create long text")
        s_example = (
            "Artificial intelligence (AI) is intelligence demonstrated by machines."
        )
        input = st.text_area(
            "Use the example below or input your own text in English (between 1,000 and 10,000 characters)",
            value=s_example,
            max_chars=10000,
            height=330,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 API Key Not Found!")
        st.info(
            "💡 Copy paste your OpenAI API key that you can find in User -> API Keys section once you log in to the OpenAI API Playground"
        )
