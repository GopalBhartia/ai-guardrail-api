# Use an explicit lightweight base image
FROM python:3.11-slim

# Set environment system behavior variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /code

# Copy requirements and install via layer caching strategy
COPY ./requirements.txt /code/requirements.txt
run pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application blueprints
COPY ./app /code/app

# Expose target network port
EXPOSE 8080

# Command to boot standard Uvicorn worker bound to deployment environments
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080