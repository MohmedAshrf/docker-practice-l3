FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install requests beautifulsoup4
CMD ["python","main.py"]
