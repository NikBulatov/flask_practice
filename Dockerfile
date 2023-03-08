# from what image run commands after container initialization
FROM python:3.11.2-buster as base

# This flag is important to output python logs correctly in docker!
ENV PYTHONUNBUFFERED 1
# Flag to optimize container size a bit by removing runtime python cache
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

FROM base as dep-poetry
ENV POETRY_HOME /opt/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install --no-cache poetry==1.3.2
ENV POETRY_BIN $POETRY_HOME/bin/poetry

COPY pyproject.toml poetry.lock ./
RUN $POETRY_BIN config --local virtualenvs.create false
RUN $POETRY_BIN install --no-root

COPY . .

EXPOSE 5000

CMD ["flask init_db"]
CMD ["flask create_users"]
CMD ["flask", "db init"]
CMD ["flask", "db migrate -m \"create models\""]
CMD ["python", "wsgi.py"]

