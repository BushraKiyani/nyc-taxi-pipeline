import os
from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()
PROJECT_ID = os.getenv("GCP_PROJECT_ID")

if not PROJECT_ID:
    raise ValueError("GCP_PROJECT_ID not set. Check your .env file.")

client = bigquery.Client(project=PROJECT_ID)

query = """
SELECT COUNT(*) as total_trips
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
"""

result = client.query(query).result()

for row in result:
    print(f"Total trips in 2022: {row.total_trips:,}")