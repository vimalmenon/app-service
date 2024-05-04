FROM python:3.11.9-slim

ENV DIR=/app

WORKDIR ${DIR}

ADD . .

RUN pip install poetry

RUN poetry install

CMD ["poetry", "run", "uvicorn", "main:app"]
