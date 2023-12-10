FROM python:3.10-slim

WORKDIR /app

COPY launcher.py /app/
COPY scripts/ /app/scripts/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "launcher.py"]
