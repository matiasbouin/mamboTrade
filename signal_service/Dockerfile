FROM python:3.11-slim

WORKDIR /app

COPY signal_service/signal_service.py .
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "-m", "uvicorn", "signal_service:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "/app"]
# Note: We remove `--reload` for containerized execution