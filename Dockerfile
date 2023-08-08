FROM python:3.10.3-slim

RUN mkdir mycode
WORKDIR /mycode

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]