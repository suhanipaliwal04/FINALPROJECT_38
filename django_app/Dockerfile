FROM python:3.10-slim

WORKDIR /app

COPY . /app/

# Install Django
RUN pip install django

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

EXPOSE 8000
