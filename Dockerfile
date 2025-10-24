FROM python:3.13-slim-bullseye

ENV GROUP_ID=1000 USER_ID=1000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    gettext \
    --no-install-recommends

RUN mkdir /app
WORKDIR /app

RUN pip install -U pip && pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction

ADD ./entrypoint.sh /app/entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

EXPOSE 8000
