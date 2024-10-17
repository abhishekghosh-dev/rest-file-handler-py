# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY /app /app

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run app.py when the container launches
CMD ["python", "file-handler.py"]
