from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import requests
import json


class DDOSAttackView(APIView):
    def post(self, request):
        ip = request.META.get('REMOTE_ADDR')
        bearer = request.META.get('HTTP_AUTHORIZATION')
        if bearer != 'Bearer mf8nrqICaHYD1y8wRMBksWm7U7gLgXy1mSWjhI0q':
            return Response({'error': 'Invalid bearer key'}, status=400)
        count = cache.get(ip, 0)
        if count >= 100:
            return Response({'error': 'IP blocked permanently'}, status=400)
        cache.set(ip, count+1, 60)
        if count >= 10:
            cache.set(f'blocked:{ip}', True, 1200)
            return Response({'error': 'IP blocked for 20 minutes'}, status=400)
        return Response(json.loads(requests.get('https://api.mockaroo.com/api/bd80f7e0?count=1&key=69de55f0').content))


class AuthenticatedView(APIView):
    def get(self, request):
        bearer = request.META.get('HTTP_AUTHORIZATION')
        if bearer != 'Bearer mf8nrqICaHYD1y8wRMBksWm7U7gLgXy1mSWjhI0q':
            return Response({'error': 'Invalid bearer key'}, status=400)
        return Response({'message': 'Authenticated API'})
