#!/bin/bash

virtualenv -p python3
source ./bin/activate
pip3 install --upgrade pip
pip3 install requirements.txt
cd todoapp || exit
python3 manage.py migrate
python3 manage.py runserver