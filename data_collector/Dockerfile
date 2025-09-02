# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY data_collector/data_collector.py .

# Copy the shared requirements file and install dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python", "data_collector.py"]