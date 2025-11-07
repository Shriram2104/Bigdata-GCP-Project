import streamlit as st
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client(project="ga4-attribution-demo-477304")

st.title("GA4 Attribution Demo — Live Events")

QUERY = """
SELECT event_id, user_pseudo_id, event_name, event_timestamp, utm_source, utm_medium
FROM `ga4-attribution-demo-477304.streaming.ga4_events_stream`
ORDER BY event_timestamp DESC
LIMIT 20
"""

@st.cache_data(ttl=10)
def load_data():
    return client.query(QUERY).to_dataframe()

st.subheader("Recent events")
df = load_data()
st.dataframe(df)

if st.button("Refresh"):
    st.experimental_rerun()
