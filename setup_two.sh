source venv/bin/activate

export PYTHONPATH=$(pwd) 

python monzo_helper.py initialize_database import_data

fabmanager create-admin --app superset
superset db upgrade
superset init

superset import_datasources -p datasources/data_sources.yaml
superset import_dashboards -p dashboards/spending.json