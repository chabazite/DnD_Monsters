# Set base image (host OS)
FROM python:3.10-slim-buster


# Update pip 
RUN pip install --upgrade pip

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install -r requirements.txt

COPY . .cd

# Specify the command to run on container start
CMD [ "python", "./app.py" ]