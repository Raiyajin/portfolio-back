#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Empty the database and its tables
python manage.py flush --no-input

# Create new migrations if needed
python manage.py makemigrations

# Transfer the migration to the postgres database
python manage.py migrate

# Apply fixtures
python manage.py loaddata /app/apps/**/fixtures/*.yaml

python manage.py runserver 0.0.0.0:8000