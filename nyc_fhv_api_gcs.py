from datetime import datetime
from airflow.sdk import dag
from airflow.providers.google.cloud.transfers.http_to_gcs import HttpToGCSOperator

@dag(
    dag_id="nyc_fhv_api_gcs",
    tags=["nyc_fhv"],
    default_args={"owner": "JW"},
    schedule="0 3 * * *",
    catchup=False,
    start_date=datetime(2026, 1, 1),
    end_date=datetime(2030, 1, 1),
    max_active_runs=1
)

def dag_creator():

    # API Docs: https://data.cityofnewyork.us/Transportation/For-Hire-Vehicles-FHV-Active/8wbx-tsch/about_data

    api_to_gcs = HttpToGCSOperator(
        task_id="api_to_gcs_csv",
        http_conn_id="nyc_fhv",
        endpoint="/resource/8wbx-tsch.csv?$limit=500000",
        method="GET",
        gcp_conn_id="gcp_conn_id",
        object_name=(
            "raw-data/fhv-active/"
            "year={{ logical_date.year }}/"
            "month={{ logical_date.strftime('%m') }}/"
            "day={{ (logical_date - macros.timedelta(days=1)).strftime('%d') }}/"
            "fhv_active_{{ (logical_date - macros.timedelta(days=1)).strftime('%Y%m%dT%H%M%S') }}_{{ macros.uuid.uuid4() }}.csv"
        ),
        mime_type="text/csv",
        bucket_name="{{ var.value.nyc_fhv_bucket }}"
    )

dag = dag_creator()