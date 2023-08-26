# Base image
FROM python:3.9-slim-buster

WORKDIR /poke_app

COPY app /poke_app/app/
COPY tests /poke_app/tests/
COPY run.py /poke_app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=/app/api/

CMD ["python", "run.py"]