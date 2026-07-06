import streamlit as st
import requests

from config import API_URL

st.title("📄 Upload Research Papers")

uploaded_files = st.file_uploader(
    "Choose one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.write("### Selected Files")

    for pdf in uploaded_files:
        st.write(f"📄 {pdf.name}")

    if st.button("Upload All"):

        with st.spinner("Uploading documents..."):

            files = []

            for pdf in uploaded_files:

                files.append(
                    (
                        "files",          # <-- must match FastAPI parameter name
                        (
                            pdf.name,
                            pdf,
                            "application/pdf"
                        )
                    )
                )

            response = requests.post(
                f"{API_URL}/upload/",
                files=files
            )

        if response.status_code == 200:

            result = response.json()

            st.success(
                f"Successfully uploaded {result['uploaded']} document(s)."
            )

            for doc in result["documents"]:

                with st.expander(doc["original_filename"]):

                    st.write(f"**Document ID:** {doc['document_id']}")
                    st.write(f"**Chunks:** {doc['total_chunks']}")
                    st.write(f"**Characters:** {doc['characters']}")
                    st.write(f"**Status:** {doc['status']}")

        else:

            st.error("Upload failed")

            st.code(response.text)