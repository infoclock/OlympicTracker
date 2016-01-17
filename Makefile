default: run

DATABASE_NAME=db.sqlite3

configure:
	python3 configure.py

rebuild: deldb syncdb initdb

deldb:
	rm -f $(DATABASE_NAME)

syncdb:
	python3 manage.py syncdb --noinput

initdb:
	sqlite3 $(DATABASE_NAME) < seed.sql

run:
	python3 manage.py runserver

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm

veryclean: deldb clean
	rm -f allauthdemo/settings_generated.py
