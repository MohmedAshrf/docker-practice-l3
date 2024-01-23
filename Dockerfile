FROM python:3.9-slim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Run the collect.py script
RUN python collect.py

CMD ["python","test.py"]
