from datetime import datetime
from airflow.sdk import dag
from airflow.providers.google.cloud.transfers.http_to_gcs import HttpToGCSOperator

@dag(
    dag_id="nyc_fhv_weather",
    tags=["nyc_fhv"],
    default_args={"owner": "JW"},
    schedule="@hourly",
    catchup=False,
    start_date=datetime(2026, 1, 1),
    end_date=datetime(2030, 1, 1),
    max_active_runs=1
)

def dag_creator():

    # API Docs: https://openweathermap.org/current

    # New York - Coordinates
    lat="40.7128"
    lon="-74.0060"

    object_name = (
        "raw-data/weather/"
        "year={{ logical_date.year }}/"
        "month={{ logical_date.strftime('%m') }}/"
        "day={{ logical_date.strftime('%d') }}/"
        "hour={{ logical_date.strftime('%H') }}/"
        "nyc_weather_{{ ts_nodash }}_{{ macros.uuid.uuid4() }}.json"
    )

    api_to_gcs = HttpToGCSOperator(
        task_id="weather_api_to_gcs_json",
        http_conn_id="nyc_weather",
        endpoint=f"/data/2.5/weather?lat={lat}&lon={lon}&appid={{{{ conn.nyc_weather.password }}}}&units=metric",
        method="GET",
        gcp_conn_id="gcp_conn_id",
        object_name=object_name,
        mime_type="application/json",
        bucket_name="{{ var.value.nyc_fhv_bucket }}"
    )

dag = dag_creator()