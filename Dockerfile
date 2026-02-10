FROM sagemath/sagemath:latest

# Set working directory
WORKDIR /app

# Install Python dependencies
USER root
RUN apt-get update && apt-get install -y python3-pip

# Copy application files
COPY requirements.txt .
COPY app.py .
COPY templates/ templates/

# Install Flask and gunicorn
RUN pip3 install Flask gunicorn

# Expose port
EXPOSE 10000

# Set environment variable for port
ENV PORT=10000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--timeout", "120", "app:app"]
