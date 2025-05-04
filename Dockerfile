FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install pytest

CMD ["python", "scripts/run_example.py"]