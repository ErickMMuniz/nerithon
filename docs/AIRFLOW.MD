## Install AIRFLOW

```
#fish
export AIRFLOW_VERSION=3.1.3
export PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-$AIRFLOW_VERSION/constraints-$PYTHON_VERSION.txt"
uv pip install "apache-airflow==$AIRFLOW_VERSION" --constraint $CONSTRAINT_URL
```

## Create db 

## Install AIRFLOW

```
airflow db migrate
```

