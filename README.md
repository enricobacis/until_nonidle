# until_nonidle
Execute something as long as the user is idling.

## requirements

* xprintidle
* psutil

## example

    ./until_nonidle.py sleep 10

The `sleep 10` command terminates if the user comes back from idling.
