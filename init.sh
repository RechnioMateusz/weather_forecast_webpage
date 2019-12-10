# Path to python requirements file
REQS=python_requirements.txt

# Path manage.py
MANAGE=weather_forecast/manage.py

# ASCII art by 'jgs' from https://ascii.co.uk/art
echo "      ,"
echo "     /(  ___________"
echo "    |  >:===========\`        Working on initialization"
echo "     )("
echo "     \"\""


# If manage.py exists run server, echo otherwise
if test -f "$REQS"; then
    pip install -r "$REQS"
else
    echo "$REQS DOES NOT EXIST!"
fi

# If manage.py exists makemigrations, migrate, create super user, echo otherwise
if test -f "$MANAGE"; then
    python "$MANAGE" makemigrations
    python "$MANAGE" migrate
    python "$MANAGE" createsuperuser --noinput --username admin --email admin@gmail.com
else
    echo "$MANAGE DOES NOT EXIST!"
fi
