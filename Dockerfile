# Use Python 3.8 as base image
FROM python:3.8


# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app/

# Install core dependencies.
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    python3-dev \
    gcc \
    netcat-openbsd \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Expose the port
EXPOSE 8000

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Run the application
ENTRYPOINT [ "sh" , "/app/entrypoint.sh"]

