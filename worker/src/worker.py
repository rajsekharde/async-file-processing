import redis

print("Worker starting up...")

r = redis.Redis(host="redis", port=6379, decode_responses=True)

QUEUE_NAME = "jobs"

while True:
    print("Worker waiting for job...")
    queue_name, job_id = r.brpop(QUEUE_NAME)
    print(f"Worker received job_id: {job_id}")
