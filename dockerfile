FROM python:3.11-alpine as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-alpine
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN apk update && apk add \
    gcc \
    musl-dev \
    libpq-dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/

CMD ["gunicorn", "app.main:app", "-b", ":80", "--worker-class", "aiohttp.GunicornWebWorker", "--reload", "--access-logfile", "-"]
