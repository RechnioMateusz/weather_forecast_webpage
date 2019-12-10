# Path to manage.py
MANAGE=weather_forecast/manage.py

# If manage.py exists run server, echo otherwise
if test -f "$MANAGE"; then

    # ASCII art by 'jgs' from https://ascii.co.uk/art
    echo "                     _"
    echo "                   _( }"
    echo "         -=   _  <<  \\"
    echo "             \`.\\__/\`/\\\\"
    echo "       -=      '--'\\\\  \`"
    echo "            -=     //"
    echo "  Running server   \\)"

    python "$MANAGE" runserver 127.0.0.1:8000
else
    echo "$MANAGE DOES NOT EXIST!"
fi
