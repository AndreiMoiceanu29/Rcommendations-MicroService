RUN python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apk update && apk add tk

COPY recommendations .

CMD ["python","-u","recommendations.py"]