FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY fetch_models.py .

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Make the report directory
RUN mkdir /reports

# Run fetch_models.py when the container launches
CMD ["python", "fetch_models.py"]
