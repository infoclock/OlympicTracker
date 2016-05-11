# InfoClock

http://infoclock.palcu.ro/
http://infoclock.palcu.ro/ranking

## Getting Running


1. Install Python. I used Python 3.4.3 at the moment but 2.7.x works fine too.

2. Install a ``virtualenv`` and requirements:

        $ cd OlympicTracker
        $ virtualenv mypy
        $ . mypy/bin/activate
        $ pip install -r requirements.txt


3. Set up and Run:

        $ make configure   # Builds a seed.sql that can be used in `make rebuild`
        $ make rebuild     # A bit better than `python manage.py syncdb`
        $ make run         # The same as `python manage.py runserver`

4. Load problem data

        $ ./manage.py shell < init_script.py

5. Visit http://127.0.0.1:8000/
