import streamlit as st
import requests

from config import API_URL

st.title("📄 Export Research Report")

st.write(
    "Generate a complete research report from your AI outputs."
)

summary = st.text_area(
    "Paper Summary"
)

comparison = st.text_area(
    "Paper Comparison"
)

literature = st.text_area(
    "Literature Review"
)

notes = st.text_area(
    "Research Notes"
)

chat = st.text_area(
    "Chat History"
)

if st.button("Generate Markdown Report"):

    response = requests.post(

        f"{API_URL}/export/markdown",

        json={

            "summary": summary,

            "comparison": comparison,

            "literature": literature,

            "notes": notes,

            "chat": chat

        }

    )

    if response.status_code == 200:

        markdown = response.json()["markdown"]

        st.success("Report generated successfully!")

        st.markdown(markdown)

        st.download_button(

            label="⬇ Download Markdown",

            data=markdown,

            file_name="AI_Research_Report.md",

            mime="text/markdown"

        )

    else:

        st.error(response.text)