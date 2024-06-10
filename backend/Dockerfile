# Use the official Python 3.10 image as a base
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Copy the wait script and superuser creation script
COPY wait_for_db.py /app/
COPY create_superuser.py /app/

# Expose the port
EXPOSE 8000

# Run the wait script, make migrations, apply migrations, create superuser, and start the server
CMD ["sh", "-c", "python wait_for_db.py && python manage.py makemigrations && python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]