FROM python

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install -r requirements.txt

COPY . /backend/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
