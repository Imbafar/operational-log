# FROM amd64/python:3.9
# FROM python:3.7-slim
FROM --platform=linux/amd64 python:3.7-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0:80"]

