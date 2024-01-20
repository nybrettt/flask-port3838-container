# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
 
# Install the necessary packages
RUN pip install Flask
RUN pip install APScheduler
RUN pip install psycopg2-binary
RUN pip install python-dotenv

# Make port 3838 available to the world outside this container
EXPOSE 3838

# When you run the Docker container, pass the DATABASE_URL as an environment variable:

# Run app.py when the container launches
CMD ["python", "app.py"]
