
git add .
git commit -m "Changes"
git push heroku master
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate
heroku run python3 manage.py migrate --run-syncdb
