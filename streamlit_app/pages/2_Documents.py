import streamlit as st
import requests

from config import API_URL

st.title("📚 Documents")

# Refresh button
if st.button("🔄 Refresh"):
    st.rerun()

response = requests.get(f"{API_URL}/documents/")

if response.status_code != 200:
    st.error("Could not load documents.")
    st.stop()

documents = response.json()

if len(documents) == 0:
    st.info("No documents uploaded.")
    st.stop()

for doc in documents:

    with st.container():

        col1, col2 = st.columns([4, 1])

        with col1:

            st.subheader(doc["filename"])

            st.write(f"**Document ID:** {doc['document_id']}")
            st.write(f"**Chunks:** {doc['chunks']}")

            if "size_kb" in doc:
                st.write(f"**Size:** {doc['size_kb']} KB")

        with col2:

            if st.button(
                "🗑 Delete",
                key=doc["document_id"]
            ):

                delete = requests.delete(
                    f"{API_URL}/documents/{doc['document_id']}"
                )

                if delete.status_code == 200:
                    st.success("Deleted successfully.")
                    st.rerun()
                else:
                    st.error("Delete failed.")

        st.divider()