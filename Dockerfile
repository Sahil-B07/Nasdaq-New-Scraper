FROM python:3.9-alpine

COPY task.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

CMD [ "python3","task.py" ] 