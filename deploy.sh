python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py csu
python3 manage.py test
coverage run --source='.' manage.py test
coverage report
deactivate
