FROM python:3.10-slim-buster AS base
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"

FROM base AS deps
RUN apt-get update && \
    apt-get install -y curl gcc git make && \
    curl -sSL https://install.python-poetry.org | python3 -

FROM deps AS runtime
WORKDIR /hero_camp
