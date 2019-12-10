MANAGE=weather_forecast/manage.py

if test -f "$MANAGE"; then
    python "$MANAGE" runserver 127.0.0.1:8000
else
    echo "$MANAGE DOES NOT EXIST!"
fi