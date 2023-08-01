release: python kanairo/manage.py makemigrations --no-input
release: python kanairo/manage.py migrate --no-input

web: gunicorn --chdir kanairo kanairo.wsgi
