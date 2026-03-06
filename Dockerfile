FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

RUN apt update && apt upgrade -y
RUN apt-get install -y libnspr4\
    libnss3\
    libdbus-1-3\
    libatk1.0-0\
    libatk-bridge2.0-0\
    libatspi2.0-0\
    libxcomposite1\
    libxdamage1\
    libxfixes3\
    libxrandr2\
    libgbm1\
    libxkbcommon0\
    libasound2\
    libcups2

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --no-dev --frozen
RUN uv run --no-dev playwright install chromium

COPY app app
COPY front front
