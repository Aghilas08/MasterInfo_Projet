###### Dockerfile #########

FROM python:3.11-slim

COPY . /app

WORKDIR /app

# installation d'un client postgesql
RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
