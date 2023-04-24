import os

os.system("virtualenv venv")
os.system("venv/bin/activate")
os.system("python manage.py runserver")