# globalize_weather.py
# --------------------
# By MWC Contributors
#
# This shell shell script adds `weather` to your global PATH, so that you'll be able to 
# run it from any Terminal session. If you want this, just run:
#
# source globalize_weather.sh

CHECK=$(which weather 2>&1)
if [ $CHECK = "weather not found" ]; then
    echo "The weather script was not found. Make sure you are in a Poetry shell and that you have run poetry install."
else
    echo "\n# Adding path for weather" >> ~/.mwc_rc
    echo "export PATH=\"$(dirname $(which weather)):\$PATH\"" >> ~/.mwc_rc
    source ~/.mwc_rc
fi
