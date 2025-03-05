FROM python:3.13-alpine

ARG APP_PATH=/app
ARG VENV_PATH="${APP_PATH}/.venv-docker"

WORKDIR ${APP_PATH}

COPY pyproject.toml .

RUN pip install uv

ENV PATH="${VENV_PATH}/bin:$PATH" \
    PYTHONPATH="/app:$PYTHONPATH" \
    VIRTUAL_ENV=${VENV_PATH} \
    UV_PROJECT_ENVIRONMENT="${VENV_PATH}" \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["sh", "./dev-entrypoint.sh"]