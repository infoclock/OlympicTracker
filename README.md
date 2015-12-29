# InfoClock


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
6. Check out allauthdemo/urls.py . That's where the main app resides.


At this point you should have a site that allows registration and
login of local users. If you enabled Google or Facebook during ``make configure``,
those destinations should allow you to join and log in to the site.

## Some Notes

### A word about seed data

During development I find that I frequently want to erase and rebuild the database,
and setting up seed data like the admin user and ``Sites`` objects can be tedious.
There are ways to set this up in code (the ``allauth`` source does this) but I've
chosen to do it with a SQL file, produced with:

    Makefile --> runs Python configure.py --> produces seed.sql

I want to point out that this use of Makefiles and seed data is nothing to do with
``allauth``, it's just my hack way of getting set up and running.

You can edit ``seed.sql`` then destroy and rebuild your database easily with this:

    make rebuild

