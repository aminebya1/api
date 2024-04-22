FROM python:3.10

ENV PYTHONUNBEFFERED = 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" , "8000" ]