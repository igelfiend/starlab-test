# STARLAB APPLICATION
## Description
This repo contains application for starlab.

This application has tree, form with employee info and form with new subordinate's employee info.

Employees can be choosed via tree. If element is selected at will be highlighted with green background.

Employee's info form allows to do edit stuff. To confirm changes is needed to press `Update`. Besides, it has `Ass subordinate` button that shows new employees form and freezes both tree and employee info form.

New employee form can be either cancled via `Cancel` button or confirmed by pressing `Save` button. In both cases this form will be hidden from user and tree and employee info form will be unfreezed.

In case of any errors error panel will be shown with short info. In case of success element update or appending user will be notified too.

## Installation
All code are packed into docker, so you could hit `./initialize.bash` and everything will be ready.

## Execution
For execution you could either run `./run.bash` or do it manually with `docker-compose up starlab-test-app`.

In case of `./run.bash` pgadmin will be executed too.
Default address for app is [localhost] or [127.0.0.1](http://127.0.0.1)

## Data surf

Besides of backend service there is available a pgadmin service. Can be accessed at [127.0.0.1:5050](http://127.0.0.1:5050).

Credentials are:

* login: `pgadmin4@pgadmin.org`
* password: `admin`

Database credentials are:

* dbname: `starlab-test`
* user: `postgres`
* password: `postgres`
