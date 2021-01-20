#!/bin/bash

virtualenv -p python3
source ./bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver