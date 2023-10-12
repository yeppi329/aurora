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

# Wait for few minute and run db migraiton
while ! python manage.py loaddata group_data  2>&1; do
   echo "load group_data"
   sleep 1
done

while ! python manage.py loaddata content_type_data  2>&1; do
   echo "load content_type_data"
   sleep 1
done

while ! python manage.py loaddata auth_permission  2>&1; do
   echo "load auth_permission"
   sleep 1
done

echo "Django docker is fully configured successfully."

exec "$@"