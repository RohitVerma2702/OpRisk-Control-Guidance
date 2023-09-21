import streamlit as st
import prompting
from PIL import Image
import streamlit.components.v1 as components

im = Image.open("./assets/images/RS-square-logo.jpeg")

st.set_page_config(
    layout="wide", page_title="RiskSpotlight - OpRisk Control Guidance", page_icon=im
)

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("OpRisk Control Guidance")

col1, col2 = st.columns(2)

with col1:
    risk = st.text_area("Please provide Risk details.", value="", height=120)
    clicked = st.button("Submit")

with col2:
    num_controls = st.number_input(
        "Number of Control Results...", min_value=3, max_value=10
    )
    control_type = st.multiselect(
        "Please select control type.",
        ["Preventative", "Detective", "Corrective"],
    )

if clicked:
    if not risk or not num_controls or not control_type:
        st.sidebar.warning("Please fill in all the information.")

    else:
        with st.spinner("Please wait..."):
            response = prompting.generate_controls(risk, num_controls, control_type)

            st.header(risk)
            controls = response["choices"][0]["message"]["content"]
            st.write(controls, unsafe_allow_html=True)
