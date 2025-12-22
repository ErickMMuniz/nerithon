## Install AIRFLOW

```
#fish
export AIRFLOW_VERSION=3.1.3
export PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-$AIRFLOW_VERSION/constraints-$PYTHON_VERSION.txt"
uv pip install "apache-airflx`ow==$AIRFLOW_VERSION" --constraint $CONSTRAINT_URL
```

## Create db 

## Install AIRFLOW

```
airflow db migrateINFO:     127.0.0.1:50958 - "GET /api/v2/dagTags?limit=10&offset=0&order_by=name&tag_name_pattern= HTTP/1.1" 200 OK
INFO:     127.0.0.1:50978 - "GET /ui/dags?dag_runs_limit=14&limit=50&offset=0&exclude_stale=true&order_by=dag_display_name HTTP/1.1" 200 OK
INFO:     127.0.0.1:50958 - "
```

