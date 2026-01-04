FROM python:3.11-slim

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "-u", "src/worker.py"]

# "-u" to run python file in unbuffered mode to view startup and dequeue logs