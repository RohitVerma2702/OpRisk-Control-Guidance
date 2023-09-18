import os
import openai
import toml
import streamlit as st

# secrets = toml.load("secrets.toml")
# openai.api_key = secrets["openai_api_key"]

os.environ["OPENAI_API_KEY"] = st.secrets["secret_key"]

def generate_controls(risk, num_controls, control_type):
    text = f"""Imagine you are an Operational Risk Officer.
        Suggest me {num_controls} {control_type} controls for {risk} risk.
        Please present the data in an HTML table format with a header with a black background color and white center aligned font, use inline style for styling the header. Use the following columns:
        Control Title: This should contain the control title with at least 5 to 10 words long like a meaningful sentence.
        Control Description: This should describe the control in at least 50 to 100 words with providing a recommendation on the frequency of this control.
        Control Type: This should show the control type.
        Please take some time to think and then provide a complete response and make sure to provide only the HTML table, I don't need any explanation."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=1,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
