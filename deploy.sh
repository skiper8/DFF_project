#!/bin/bash

python3 -m venv venv
source  venv/bin/activate
pip3 install -r requirement.txt
python3 manage.py migrate
python3 manage.py runserver