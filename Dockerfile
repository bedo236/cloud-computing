# Base image
FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install NLTK

CMD ["python", "python_script.py"]
