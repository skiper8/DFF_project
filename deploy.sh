python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
coverage run --source='.' manage.py test
coverage report
python3 manage.py runserver 0.0.0.0:8000
deactivate