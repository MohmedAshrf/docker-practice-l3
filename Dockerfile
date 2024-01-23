FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN python collect.py
CMD ["python","test.py"]
