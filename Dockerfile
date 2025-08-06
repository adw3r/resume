FROM ghcr.io/astral-sh/uv:debian-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    wget \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxshmfence1 \
    libasound2 \
    libx11-xcb1 \
    libxext6 \
    libxfixes3 \
    libx11-6 \
    libxcb1 \
    libxkbcommon0 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgtk-3-0 \
    libexpat1 \
    fonts-liberation \
    ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --frozen --no-dev
RUN uv run playwright install chromium

COPY app app
COPY front front
