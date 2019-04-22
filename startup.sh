export PYTHONPATH=$(pwd) 

## setup
# fabmanager create-admin --app superset
# superset db upgrade
# superset init
# superset import_datasources -p data_sources.yaml

## run
superset runserver -d