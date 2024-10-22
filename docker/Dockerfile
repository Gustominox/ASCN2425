# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive
ARG GIT_TOKEN


# Install system dependencies including git
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install PostgreSQL (15.4)
RUN apt-get update && apt-get install -y postgresql

COPY moonshot .

WORKDIR /moonshot

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Generate a secure SECRET_KEY using Django's built-in utility
#RUN SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())") && \
 #   echo "SECRET_KEY=$SECRET_KEY" >> ./.env

# Expose the port that the application will run on
EXPOSE 8000

# Run migrations and start the server
#CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]