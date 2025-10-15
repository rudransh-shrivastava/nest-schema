FROM python:3.14.0-alpine

WORKDIR /action

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh main.py ./

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/action/entrypoint.sh"]
