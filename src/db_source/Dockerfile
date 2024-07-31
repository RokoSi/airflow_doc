FROM python:3.11.6


LABEL authors="chernyshev"

RUN pip install poetry \
    && pyhton m venv venv\
    && . venv/bin/activate \
    && pip install poetry

WORKDIR /var/db_source

COPY pyproject.toml /var/db_source/

RUN poetry install --no-root \
    && poetry update



COPY . /var/db_source

EXPOSE 5624:5624




CMD ["python", "main.py"]