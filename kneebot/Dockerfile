FROM python:3.9
WORKDIR /kneebot

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD sleep 5 && python3 main.py
