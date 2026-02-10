FROM python:3.11-slim

WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY app.py .
COPY templates/ templates/

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Set environment variable for port
ENV PORT=10000

# Run the application with gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT --timeout 120 --workers 1 app:app
