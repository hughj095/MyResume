# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR C:\Users\johnm\OneDrive\Desktop\MyResume

# Copy the current directory contents into the container at /app
COPY . C:\Users\johnm\OneDrive\Desktop\MyResume

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV ClientID=2

# Run app.py when the container launches
CMD ["python", "portfolio3.0_docker2.py"]
