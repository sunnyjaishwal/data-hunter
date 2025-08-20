from rest_framework.throttling import UserRateThrottle, SimpleRateThrottle


class UserCrawlerRateThrottle(SimpleRateThrottle):
    scope = 'user_crawler'

    def get_cache_key(self, request, view):
        user = getattr(request, 'user', None)

        if not user or not user.is_authenticated:
            return None 

        crawler = None
        try:
            crawler = request.data.get('crawler_name') 
        except Exception:
            pass

        if not crawler:
            return None

        ident = f"{user.pk}-{crawler}"

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
