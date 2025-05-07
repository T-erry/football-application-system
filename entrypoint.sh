
# Wait for PostgreSQL to be ready
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done


python manage.py migrate --noinput

python manage.py load_json_data 

#Collect static files example django-rest-framework or django-admin packages these statics in out STATIC_ROOT directory
python manage.py collectstatic --no-input


exec gunicorn football.wsgi:application --bind 0.0.0.0:8000 --workers 3 
