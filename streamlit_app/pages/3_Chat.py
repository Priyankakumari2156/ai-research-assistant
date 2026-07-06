import streamlit as st
import requests

from config import API_URL

# ==========================================================
# Helper Functions
# ==========================================================

def send_request(question, action, document_ids):
    payload = {
        "question": question,
        "action": action,
        "document_ids": document_ids,
    }

    response = requests.post(
        f"{API_URL}/chat/",
        json=payload,
    )

    if response.status_code != 200:
        st.error(response.text)
        return None

    return response.json()


def add_message(role, content, sources=None):
    message = {
        "role": role,
        "content": content,
    }

    if sources:
        message["sources"] = sources

    st.session_state.messages.append(message)


# ==========================================================
# Load Documents
# ==========================================================

try:
    response = requests.get(f"{API_URL}/documents/")

    if response.status_code == 200:
        documents = response.json()
    else:
        documents = []

except Exception:
    documents = []

# ==========================================================
# Page
# ==========================================================

st.title("💬 AI Research Chat")

left_col, right_col = st.columns([1, 2])
# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.header("Chat")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # ==========================================================
    # Save Research Notes
    # ==========================================================

    if "latest_answer" in st.session_state:

        st.divider()

        st.subheader("📝 Save Research Note")

        default_title = "Research Note"

        action = st.session_state.get("latest_action")

        if action == "summary":
            default_title = "Paper Summary"

        elif action == "methodology":
            default_title = "Paper Methodology"

        elif action == "contributions":
            default_title = "Paper Contributions"

        elif action == "limitations":
            default_title = "Paper Limitations"

        elif action == "future_work":
            default_title = "Future Work"

        elif action == "applications":
            default_title = "Applications"

        note_title = st.text_input(
            "Research Note Title",
            value=default_title
        )

        if st.button("⭐ Save to Research Notes"):

            if not note_title.strip():

                st.warning("Please enter a title.")

            else:

                response = requests.post(

                    f"{API_URL}/notes/",

                    json={
                        "title": note_title,
                        "content": st.session_state["latest_answer"]
                    }

                )

                if response.status_code == 200:

                    st.success("✅ Research note saved successfully!")
                    st.session_state.pop("latest_answer", None)
                    st.session_state.pop("latest_action", None)
                    st.rerun()
                else:

                    st.error(response.text)


with left_col:

    # ==========================================================
    # Workspace
    # ==========================================================

    st.subheader("📚 Workspace")

 

    # ==========================================================
    # Document Selection
    # ==========================================================

    selected_documents = st.multiselect(
        "📚 Select Documents",
        options=documents,
        format_func=lambda doc: doc["filename"],
    )

    document_ids = [
        doc["document_id"]
        for doc in selected_documents
    ]

    st.metric(
        "Selected Papers",
        len(selected_documents)
    )

    # ==========================================================
    # Research Tools
    # ==========================================================

    RESEARCH_ACTIONS = {
        "📄 Summary": (
            "summary",
            "📄 Generate a summary of the selected paper.",
        ),
        "🔬 Methodology": (
            "methodology",
            "🔬 Explain the methodology used in the paper.",
        ),
        "📌 Contributions": (
            "contributions",
            "📌 List the key contributions.",
        ),
        "⚠ Limitations": (
            "limitations",
            "⚠ Explain the limitations.",
        ),
        "💡 Future Work": (
            "future_work",
            "💡 Describe the future work.",
        ),
        "📊 Applications": (
            "applications",
            "📊 Explain the practical applications.",
        ),
    }

    clicked_action = None
    display_text = None
    question = None

    # ==========================================================
    # 🧠 Research Tools
    # ==========================================================

    with st.expander("🧠 Research Tools", expanded=True):

        cols = st.columns(2)

        for index, (label, (action_name, prompt)) in enumerate(RESEARCH_ACTIONS.items()):

            if cols[index % 2].button(label):

                clicked_action = action_name
                question = prompt
                display_text = label

    # ==========================================================
    # 📊 Compare Papers
    # ==========================================================

    with st.expander("📊 Compare Research Papers"):

        if st.button("📊 Compare Selected Papers"):

            if len(selected_documents) < 2:

                st.warning(
                    "Please select at least two research papers."
                )

            else:

                with st.spinner("Comparing papers..."):

                    response = requests.post(
                        f"{API_URL}/compare/",
                        json={
                            "document_ids": document_ids
                        }
                    )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state["comparison"] = data["answer"]

                    st.success("Comparison generated successfully!")

                    st.markdown(data["answer"])

                    st.download_button(
                        "⬇ Download Comparison",
                        data=data["answer"],
                        file_name="paper_comparison.md",
                        mime="text/markdown"
                    )

                else:

                    st.error(response.text)

    # ==========================================================
    # 📚 Literature Review
    # ==========================================================

    with st.expander("📚 Literature Review"):

        if st.button("📚 Generate Literature Review"):

            if len(selected_documents) < 2:

                st.warning(
                    "Please select at least two papers."
                )

            else:

                with st.spinner("Generating literature review..."):

                    response = requests.post(
                        f"{API_URL}/literature/",
                        json={
                            "document_ids": document_ids
                        }
                    )

                if response.status_code == 200:

                    review = response.json()["answer"]

                    st.session_state["literature"] = review

                    st.success("Literature Review Generated")

                    st.markdown(review)

                    st.download_button(
                        "⬇ Download Literature Review",
                        data=review,
                        file_name="literature_review.md",
                        mime="text/markdown"
                    )

                else:

                    st.error(response.text)


with right_col:

    st.subheader("💬 Conversation")

    st.caption(
        "Ask questions about the selected research papers."
    )

    st.divider()

    # ==========================================================
    # Previous Chat
    # ==========================================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            if (
                message["role"] == "assistant"
                and "sources" in message
            ):

                with st.expander("📚 Retrieved Sources"):

                    for i, source in enumerate(
                        message["sources"],
                        start=1,
                    ):

                        st.markdown(f"### Source {i}")

                        st.write(f"📄 **Document:** {source.get('filename', 'Unknown')}")

                        st.write(f"**Chunk ID:** {source['chunk_id']}")

                        st.write(f"**Similarity:** {source['score']:.4f}")

                        st.write(source["text"])

                        st.divider()

    # ==========================================================
    # Manual Chat
    # ==========================================================

    manual_question = st.chat_input(
        "Ask a question about your uploaded documents..."
    )

    if manual_question:

        question = manual_question
        display_text = manual_question
        clicked_action = None

    # ==========================================================
    # Execute Request
    # ==========================================================

    if question:

        if not document_ids:

            st.warning(
                "Please select at least one document."
            )

            st.stop()

        add_message(
            "user",
            display_text,
        )

        with st.chat_message("user"):
            st.write(display_text)


        with st.spinner("Searching documents..."):

            data = send_request(
                question,
                clicked_action,
                document_ids,
            )

        if data:

            answer = data["answer"]
            sources = data.get("sources", [])

            # Save outputs for Export Report
            if clicked_action == "summary":
                st.session_state["summary"] = answer

            elif clicked_action == "methodology":
                st.session_state["methodology"] = answer

            elif clicked_action == "contributions":
                st.session_state["contributions"] = answer

            elif clicked_action == "limitations":
                st.session_state["limitations"] = answer

            elif clicked_action == "future_work":
                st.session_state["future_work"] = answer

            elif clicked_action == "applications":
                st.session_state["applications"] = answer

            # Save latest AI response
            st.session_state["latest_answer"] = answer
            st.session_state["latest_action"] = clicked_action

            add_message(
                "assistant",
                answer,
                sources,
            )

            with st.chat_message("assistant"):

                st.write(answer)

                with st.expander("📚 Retrieved Sources"):

                    for i, source in enumerate(
                        sources,
                        start=1,
                    ):

                        st.markdown(f"### Source {i}")

                        st.write(f"📄 **Document:** {source.get('filename', 'Unknown')}")

                        st.write(f"**Chunk ID:** {source['chunk_id']}")

                        st.write(f"**Similarity:** {source['score']:.4f}")

                        st.write(source["text"])

                        st.divider()



