
FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
WORKDIR /app
CMD ["python3", "/app/demo/manage.py", "runserver", "0.0.0.0:8000"]
