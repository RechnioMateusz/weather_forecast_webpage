REQS=python_requirements.txt
MANAGE=weather_forecast/manage.py

if test -f "$REQS"; then
    pip install -r "$REQS"
else
    echo "$REQS DOES NOT EXIST!"
fi

if test -f "$MANAGE"; then
    python "$MANAGE" makemigrations
    python "$MANAGE" migrate
    python "$MANAGE" createsuperuser --noinput --username admin --email admin@gmail.com
else
    echo "$MANAGE DOES NOT EXIST!"
fi