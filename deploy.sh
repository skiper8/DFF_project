#!/bin/bash

python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
