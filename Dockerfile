FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache --user -r requirements.txt

COPY . .

CMD ["bash", "db_init.sh"]

EXPOSE 5000
