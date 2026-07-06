import streamlit as st
import requests

from config import API_URL

st.set_page_config(
    page_title="AI Research Assistant",
    layout="wide"
)

st.title("🤖 AI Research Assistant Dashboard")

response = requests.get(
    f"{API_URL}/dashboard/"
)

if response.status_code != 200:

    st.error("Unable to load dashboard.")

    st.stop()

dashboard = response.json()

col1, col2, col3 = st.columns(3)

col1.metric(
    "📄 Documents",
    dashboard["documents"]
)

col2.metric(
    "📝 Research Notes",
    dashboard["notes"]
)

col3.metric(
    "💬 Chat History",
    dashboard["chat_history"]
)

st.divider()

st.subheader("Workspace Status")

status1, status2, status3 = st.columns(3)

status1.success(
    "Summary"
) if dashboard["summary"] else status1.warning("Summary")

status2.success(
    "Comparison"
) if dashboard["comparison"] else status2.warning("Comparison")

status3.success(
    "Literature"
) if dashboard["literature"] else status3.warning("Literature")

status4, status5, status6 = st.columns(3)

status4.success(
    "Methodology"
) if dashboard["methodology"] else status4.warning("Methodology")

status5.success(
    "Contributions"
) if dashboard["contributions"] else status5.warning("Contributions")

status6.success(
    "Applications"
) if dashboard["applications"] else status6.warning("Applications")