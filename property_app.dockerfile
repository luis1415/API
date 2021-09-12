FROM python:3.7

RUN apt-get update -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY  . .

CMD ["uvicorn", "--host", "0.0.0.0", "property_app:app"]   
EXPOSE 8000