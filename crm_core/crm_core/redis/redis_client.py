import redis

_connections = {}

def get_redis_client(db=0):
    if db not in _connections:
        _connections[db] = redis.Redis(host='localhost', port=6379, db=db)
    return _connections[db]
