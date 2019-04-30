# Viz Experiment with Superset

A repo to play around with Apache Superset and visualise (for now) some statistic about my Monzo usage. 
Comes with a small python script to import data from Monzo APIs and save it in a few database tables.


## Requirements

* [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
* python 3.6+ due to usage of f-strings
* Psql (see notes about this in the installation section)

## Installation


env
requirements
login oauth
create config.ini and copy
db creation
run commands to import stuff (add dashboard import!)

## Usage

# Architecture

This in nothing more than a base Superset installation ()
monzo dutch taped with superset
data folder
config.ini
dashboards

## Caveats and general weirdness

- This fiddle uses PSQL as the backend, but it should be somewhat easy to switch to a different one. Apparently Superset really shines when used alongside Druid.
- Tests are...what tests?
- Two different db are used for auth tables and Monzo imported data, with hardocoded names. If you load the examples, they will be loaded in the user db. This is a legacy of me playing with settings.
- Tooltip content is specified with JS. I've used ES6 syntax so don't use an old browser.
- The imported data is not really cleaned, or even imported fully, as I just cherry-picked a few info to play around with. Easy to extend/change that by tinkering with the files in monzo_interface.
- The Monzo APIs interface requires a token that has to be copied manually, as no full OAuth token negotiation has been implemented.

## Bugs

- The SqlAlchemy version is out of date and contains a sql injection vulnerability. It's pinned to an older version due to a compatibility issue with superset.
- Time grain selection in few charts breaks the backend with a `ValueError`. Looks like a specific bug with PSQL [see here and related for manual fixes to the package](https://github.com/apache/incubator-superset/issues/5015)
- Security is...not present. Superset is 'production ready' and implements a good set of controls, none is configured in this repo.
- Tooltips in the 'London spending' chart are not showing the correct amount of money spent if there are too many transactions
