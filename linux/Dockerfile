FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl passwd \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m Codyssey

WORKDIR /app

COPY server.py .

USER Codyssey

EXPOSE 8080

CMD ["python", "server.py"]