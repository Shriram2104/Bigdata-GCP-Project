# stream_events.py
from google.cloud import bigquery
import time, random, hashlib
from datetime import datetime, timezone

client = bigquery.Client()

PROJECT = "ga4-attribution-demo-477304"
DATASET = "streaming"
TABLE = "ga4_events_stream"

table_ref = f"{PROJECT}.{DATASET}.{TABLE}"

def make_event(user_pseudo_id, event_name):
    ts = datetime.now(timezone.utc).isoformat()
    event_id = hashlib.sha1(f"{user_pseudo_id}-{ts}-{event_name}".encode()).hexdigest()
    return {
        "event_id": event_id,
        "user_pseudo_id": user_pseudo_id,
        "event_name": event_name,
        "event_timestamp": ts,
        "utm_source": random.choice(["google","facebook","email","direct"]),
        "utm_medium": random.choice(["cpc","organic","email","none"])
    }

def stream_events(n=10):
    rows = [make_event(f"user_{random.randint(1,5)}", random.choice(["page_view","click","purchase"])) for _ in range(n)]
    errors = client.insert_rows_json(table_ref, rows)
    if errors:
        print("Errors:", errors)
    else:
        print(f"Inserted {len(rows)} events.")

if __name__ == "__main__":
    stream_events(10)
