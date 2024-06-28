# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR C:\Users\johnm\OneDrive\Desktop\MyResume

# Copy the current directory contents into the container at /app
COPY . C:\Users\johnm\OneDrive\Desktop\MyResume
