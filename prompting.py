import os
import openai
import toml
import streamlit as st

# secrets = toml.load("secrets.toml")
# openai.api_key = secrets["openai_api_key"]

openai.api_key = st.secrets["openai_api_key"]


def generate_controls(risk, num_controls, control_type):
    text = f"""Imagine you are an Operational Risk Officer.
        Suggest me "{num_controls}" "{control_type}" controls for "{risk}" risk.
        Please present the data in an HTML table format with a header with a black background color and white center aligned font, use inline style for styling the header. Use the following columns:
        1. Control Title: This should contain the control title with atleast 15 to 20 words long title like a meaningful sentence that uses verbs. Please make sure to not mention control type in control title. For example, instead of writing just the control title as "Multi Factor Authentication" you can use a statement like "Require users to do Multi Factor Authentication" like a sentence.
        2. Control Description: This should describe the control in at least 50 to 100 words with providing a recommendation on the frequency of this control.
        3. Control Type: This should show the control type. Please make sure to only write the control type name itself, do not use any suffix or prefix for example, instead of using "Preventative Control" use "Preventative" only. Make sure the control types belong to this list: "{control_type} only".
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
