# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run the collect.py script (if needed)
# Comment out the line below if not necessary during build
RUN python collect.py

# CMD specifies the default command to run on container start
CMD ["python", "test.py"]
