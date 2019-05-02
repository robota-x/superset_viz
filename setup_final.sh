source venv/bin/activate

export PYTHONPATH=$(pwd) 

fabmanager create-admin --app superset
superset db upgrade
superset init
python monzo_helper write_models import_data

superset import_datasources -p datasources/data_sources.yaml
superset import_dashboards -p dashboards/spending.yaml