# Viz Experiment with Superset

A repo to play around with Apache Superset and visualise (for now) some statistic about my Monzo usage.
Comes with a small python script to import data from Monzo APIs and save it in a few database tables.

This in nothing more than a base Superset installation with pip, with some helper scripts in python/bash to import some data and a couple of sample graphs/dashboards. For proper usage, I would gravitate toward the docker image and a sturdier database integration

## Requirements

- [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
- python 3.6+ due to usage of f-strings
- Psql (see notes about this in the installation section)

## Installation

- run `bash setup_one.sh`. This will create a virtualenv, install the requirements and create a config file
- fill in the data in the newly created `config.ini` file in the root folder of the project.
  - to obtain credentials for Monzo, visit [the dev playground](developers.monzo.com/api/playground) and login
  - the database location is in sqlalchemy format, for example `postgresql+psycopg2:///superset` connects to psql with no user/pwd and uses the DB `superset`
  - (optional, to be able to load maps in your charts) login into mapbox and get your public token [here](https://account.mapbox.com/access-tokens/)
- run `bash setup_two.sh` to create the db and update the schema, import the transactions from Monzo and import the dashboard/data sources in Superset. You will have to enter some data to setup a login

## Usage

- ensure your virtual env is active (`source venv/bin/activate`)
- run `bash startup.sh` to spin up the dev server on localhost (defaults to port 8088)
- dashboards and data source should already be configured
- (optional) the command `superset load_examples` import some base examples and data from superset itself.
- run `python monzo_helper update_data` to force a refresh of your Monzo transactions. You might need to refresh your token before doing it.

## Caveats and general weirdness

- This fiddle uses PSQL as the backend, but it should be somewhat easy to switch to a different one. Apparently Superset really shines when used alongside Druid.
- Tests are...what tests?
- Tooltip content is specified with JS. I've used ES6 syntax so don't use an old browser.
- The imported data is not really cleaned, or even imported fully, as I just cherry-picked a few info to play around with. Easy to extend/change that by tinkering with the files in monzo_interface.
- The Monzo APIs interface requires a token that has to be copied manually, as no full OAuth token negotiation has been implemented.

## Bugs

- The SqlAlchemy version is out of date and contains a sql injection vulnerability. It's pinned to an older version due to a compatibility issue with superset.
- Time grain selection in few charts breaks the backend with a `ValueError`. Looks like a specific bug with PSQL [see here and related for manual fixes to the package](https://github.com/apache/incubator-superset/issues/5015)
- Security is...not present. Superset is 'production ready' and implements a good set of controls, none is configured in this repo.
- Tooltips in the 'London spending' chart are not showing the correct amount of money spent if there are too many transactions
