virtualenv -p python3
source ./bin/activate
pip install --upgrade pip
pip install requirements.txt
cd todoapp || exit
python3 manage.py migrate
python3 manage.py runserver