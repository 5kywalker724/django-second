FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /design
COPY requirements.txt /design/
RUN pip install -r requirements.txt
COPY . /design/