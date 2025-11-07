# GA4 Attribution Demo

Project packaged for demo. Replace `ga4-attribution-demo-477304` and adjust `profiles.yml` as needed for your environment.

## Quick start (Windows)
1. Create a virtualenv and activate it:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Create your dbt profile at `%USERPROFILE%\.dbt\profiles.yml` (use the template in docs). Ensure `keyfile` points to your service account JSON.
4. Run dbt:
   ```powershell
   dbt debug
   dbt build
   ```
5. Stream sample events:
   ```powershell
   set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\key.json
   python stream_events.py
   ```
6. Run Streamlit dashboard:
   ```powershell
   set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\key.json
   streamlit run app.py
   ```

## Notes
- Project uses BigQuery project id `ga4-attribution-demo-477304` and dataset names: `streaming` and `staging`.
- Region: US
