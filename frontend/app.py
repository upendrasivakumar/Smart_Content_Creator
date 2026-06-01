import streamlit as st
import requests

BACKEND_URL = st.secrets["be_server_url"]

st.set_page_config(
    page_title="Smart Content Generator",
    layout="wide"
)

st.title("🚀 Smart Content Creator")

st.write("Generate Blogs, LinkedIn Posts, Captions, Emails, and More — All Powered by AI")

topic = st.text_input(
    "Enter Topic"
)

technology = st.selectbox(
    "Select Technology",
    [
        "Python",
        "React",
        "MERN",
        "NodeJS",
        "FastAPI",
        "AI",
        "GenAI"
    ]
)

content_type = st.selectbox(
    "What Would You Like to Create",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "YouTube Description"
    ]
)

tone = st.selectbox(
    "Content Style",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)

generate = st.button("Generate Content")

if generate:

    if topic == "":
        st.warning("Please enter topic")
    else:

        with st.spinner("Generating Content..."):

            response = requests.post(
                f"{BACKEND_URL}/generate",
                params={
                    "topic": topic,
                    "technology": technology,
                    "content_type": content_type,
                    "tone": tone
                }
            )

            # result = response.json()
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.json()["content"])

            st.success("Content Generated Successfully")

            st.subheader("Generated Content")

           