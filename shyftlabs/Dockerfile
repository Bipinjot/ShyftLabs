FROM python:3
ENV HOST 0.0.0.0
ENV PORT 8000
EXPOSE 8000

RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
CMD python manage.py runserver --insecure 0.0.0.0:8000
