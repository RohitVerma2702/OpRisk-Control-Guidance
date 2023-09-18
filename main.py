import streamlit as st
import prompting
import streamlit.components.v1 as components

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("OpRisk Control Guidance")

with st.sidebar:
    risk = st.text_area("Please provide Risk details.", value="")
    num_controls = st.number_input(
        "Number of Control Results...", min_value=3, max_value=10
    )
    control_type = st.multiselect(
        "Please select control type.",
        ["Preventative", "Detective", "Corrective"],
    )
    clicked = st.button("Submit")

if clicked:
    if not risk or not num_controls or not control_type:
        st.sidebar.warning("Please fill in all the information.")

    else:
        response = prompting.generate_controls(risk, num_controls, control_type)

        st.header(risk)
        controls = response["choices"][0]["message"]["content"]
        st.write(controls, unsafe_allow_html=True)
