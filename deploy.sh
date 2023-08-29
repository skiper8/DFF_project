#!/bin/bash

python -m venv venv
source venv/bin/activate
pip install -r requirement.txt
python manage.py migrate