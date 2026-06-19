from google.cloud import bigquery

PROJECT_ID = "project-2185fd63-3ec8-490c-8f5"

client = bigquery.Client(project=PROJECT_ID)

query = """
SELECT COUNT(*) as total_trips
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
"""

result = client.query(query).result()

for row in result:
    print(f"Total trips in 2022: {row.total_trips:,}")