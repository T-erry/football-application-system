# use Python 3.8  as base image 
FROM python:3.8
# Set the working directory
WORKDIR /app

# Copy only requirements first (to cache pip install layer)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Set Django settings module
ENV DJANGO_SETTINGS_MODULE=football.settings

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]