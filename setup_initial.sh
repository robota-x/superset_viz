create_config_file() {
    echo > config.ini << EOF
[MONZO]
account_id = <your account_id from Monzo>
auth_token = <your auth_token (will expire after a day or so)>

[SUPERSET]
mapbox_api_key = <your public token from mapbox>
secret_key = <some random key>

[DATABASE]
location = <the db location>
EOF
}

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
create_config_file
