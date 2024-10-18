import redis

def create_client()
    redis_client = redis.StrictRedis(host='UPDATE_IP_ADDRESS', port=6379, db=0)

# Store conversation history in Redis
def store_conversation(client,session_id,conversation_history):
    client.set(session_id, conversation_history)

# Retrieve conversation history from Redis
def get_conversation(client,session_id):
    return client.get(session_id)

def test():
    client = redis.StrictRedis(host='UPDATE_IP_ADDRESS', port=6379, db=0)
    # Set a key-value pair
    client.set('test_key', 'Hello Redis!')
    # Retrieve the value
    value = client.get('test_key')
    print(value.decode('utf-8'))