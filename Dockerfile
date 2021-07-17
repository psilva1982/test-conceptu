FROM python:3

WORKDIR /app
COPY requirements-dev.txt /app/

RUN apt-get update && apt-get install postgresql-client -y && \
    pip install --no-cache-dir -r requirements-dev.txt

COPY . /app/

#CMD [ "/app/entrypoint.sh" ]