import streamlit as st
import requests

from config import API_URL

st.title("📝 Research Notes")

response = requests.get(
    f"{API_URL}/notes/"
)

if response.status_code != 200:

    st.error("Unable to load notes.")

    st.stop()

notes = response.json()

if len(notes) == 0:

    st.info("No saved notes.")

else:

    for note in notes:

        with st.expander(note["title"]):

            st.write(note["content"])

            if st.button(
                "🗑 Delete",
                key=note["id"]
            ):

                requests.delete(
                    f"{API_URL}/notes/{note['id']}"
                )

                st.rerun()