FROM python:3.11

ENV DIR=/app

WORKDIR ${DIR}

RUN pip install poetry

ADD . app

RUN poetry shell

RUN poetry init

CMD ["uvicorn", "main:app"]
