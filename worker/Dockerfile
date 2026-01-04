FROM python:3.11-slim

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8001

CMD ["python", "src.worker.py"]