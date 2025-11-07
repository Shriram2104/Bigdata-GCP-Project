# Assumptions & Edge Cases

- Project ID: ga4-attribution-demo-477304
- Datasets: streaming, staging (in US region)
- Lookback window: 30 days (configurable via dbt var 'lookback_days')
- Identity resolution: user_pseudo_id primary; if hashed email exists, can be used to join across devices
- Session window: 30 minutes inactivity
- Tie-breaker: when touches same timestamp, prefer deterministic order by utm_source priority list
- Dedupe: use event_id derived from hashed payload; dbt MERGE recommended for final raw table ingestion
- Latency expectation: streaming visible in seconds; dbt materialization depends on scheduler (manual run for demo)
