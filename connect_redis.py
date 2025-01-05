import redis
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def get_redis_connection():
    try:
        # Connect to Redis using environment variables
        redis_client = redis.StrictRedis(
            host=os.getenv('REDIS_HOST'),
            port=int(os.getenv('REDIS_PORT')),
            password=os.getenv('REDIS_PASSWORD'),
            decode_responses=True
        )
        redis_client.ping()  # Check the connection
        print("Successfully connected to Redis!")
        return redis_client
    except redis.exceptions.ConnectionError as e:
        print(f"Redis connection error: {e}")
        return None
