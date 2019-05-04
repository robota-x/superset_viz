# setup venv and install deps
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# create config file
cat << EOF > config.ini
[MONZO]
account_id = <your account_id from Monzo>
auth_token = <your auth_token (will expire after a day or so)>

[SUPERSET]
mapbox_api_key = <your public token from mapbox>
secret_key = <some random key>

[DATABASE]
location = <the db location>
EOF
