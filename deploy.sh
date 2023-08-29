#!/bin/bash

pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirement.txt
python3 manage.py migrate