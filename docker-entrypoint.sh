#!/bin/bash
echo "Makemigrations the Database at startup of project"

# Wait for few minute and run db makemigrations
while ! python manage.py makemigrations  2>&1; do
   echo "Makemigrations is in progress status"
   sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"