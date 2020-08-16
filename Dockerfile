FROM python:alpine

WORKDIR /app

COPY . .

EXPOSE 4000

RUN pip3 install flask mysql-connector-python flask_cors

ENTRYPOINT python3 app.py