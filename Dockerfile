FROM python:3.10.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /ecomio-api
WORKDIR /ecomio-api
ADD . /ecomio-api/
RUN pip install pipenv
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]