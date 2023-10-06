FROM python:3.10.13
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    'gcc'\
    'libpq-dev'\
    'python3-dev'\
    'g++'
WORKDIR /usr/src/app
COPY requirements/base.txt ./requirements/base.txt
RUN pip install -r ./requirements/base.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]