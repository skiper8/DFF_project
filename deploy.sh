python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --input
coverage run --source='.' manage.py test
coverage html
deactivate