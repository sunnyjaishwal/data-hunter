
DOMAIN_PARAMETER_MAP = {
    'hotel': ['hotel_id', 'check_in_date', 'check_out_date', 'guest_count'],
    'airline': ['source_iata', 'destination_iata', 'departure_date'],
    
}

import redis
import json

class CrawlerRedisClient:
    
    def __init__(self):
        self.redis_url = 'redis://localhost:6379'
        self.client = redis.from_url(self.redis_url)
   
    def build_key(self, crawler_name, parameter, domain):
        key_parts = [crawler_name]
        param_fields = DOMAIN_PARAMETER_MAP.get(domain, [])
        for field in param_fields:
            key_parts.append(str(parameter.get(field, "")))
        return ":".join(p for p in key_parts if p)
    
    def set_crawler_response(self, key, response, expiration:int= 300):
        self.client.set(key, json.dumps(response), ex=expiration)
       
        
    def get_crawler_response(self, key):
        value =  self.client.get(key)
        return json.loads(value) if value else None
