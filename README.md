# [ELT] New York City - "For Hire Vehicles"

**Data Pipeline | End-to-End | Medallion architecture**

`API --> Airflow --> GCS --> BigQuery <-- dbt`

Projekt przedstawiający cały cykl operacji na danych - od pobrania ich ze źródeł zewnętrznych, przez składowanie w Google Cloud Storage, aż po przetwarzanie w BigQuery. Jego celem jest praktyczne wykorzystanie kluczowych technologii i wzorców stosowanych w data engineeringu.


1. Pobranie surowych danych z API (NYC Open Data + OpenWeatherMap) przy użyciu `Airflow DAG` i zapis w `GCS`
2. Załadowanie danych do tabeli `BigQuery` (***bronze***) przy użyciu `Airflow DAG`
3. Transformacja danych na poziom ***silver*** oraz ***gold*** przy użyciu `dbt`

---

**[E]LT** - Extract

* Pobranie danych pogodowych: [nyc_fhv_weather.py](https://github.com/jonaszwalkowiak/nyc-fhv/blob/master/nyc_fhv_weather.py)

* Pobranie danych o pojazdach oraz kierowcach: [nyc_fhv_api_gcs.py](https://github.com/jonaszwalkowiak/nyc-fhv/blob/master/nyc_fhv_api_gcs.py) | [nyc_fhv_drivers_api_gcs.py](https://github.com/jonaszwalkowiak/nyc-fhv/blob/master/nyc_fhv_drivers_api_gcs.py)

**E[L]T** - Load

* ...

**EL[T]** - Transform

* ...