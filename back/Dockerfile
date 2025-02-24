FROM python:3.13-alpine

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync

ENV PYTHONPATH="/app:$PYTHONPATH"

ENTRYPOINT ["sh", "./dev-entrypoint.sh"]
