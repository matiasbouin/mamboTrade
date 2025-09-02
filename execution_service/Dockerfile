FROM python:3.11-slim

WORKDIR /app

COPY execution_service/execution_service.py .
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# This service will run indefinitely
CMD ["python", "/app/execution_service.py"]