FROM python:3.10-alpine as build-stage
WORKDIR /app
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /app/
RUN poetry export --output requirements.txt


FROM python:3.10-slim as production-stage
EXPOSE 80
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build-stage /app/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./alembic.ini /app/
COPY ./alembic /app/alembic
COPY ./ccfatigue /app/ccfatigue

CMD [ "uvicorn", "ccfatigue.main:app", "--host", "0.0.0.0", "--port", "80" ]
