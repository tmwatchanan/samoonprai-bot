FROM python:3.6-slim

EXPOSE 5000

RUN apt-get update \
&& apt-get install -y gcc g++ make \
&& apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app


CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
