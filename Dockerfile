FROM python:3

WORKDIR /app

COPY requirements-dev.txt /app/
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /app/

RUN python /app/manage.py migrate
