import requests, datetime
from .models import UUIDValue
from rest_framework.views import APIView
from rest_framework.response import Response

class UUIDView(APIView):
    """
    Randomly generates UUID
    Returns key-pair value of generated UUID

    key: timestamp
    value: UUID
    """

    def get(self, request):
        response = Response()
        new_entry = UUIDValue()
        new_entry.save()
        queryset = UUIDValue.objects.all().order_by('-time_stamp') # Get queryset, sort by timestamp and order by newest entry
        timestamps = [query.time_stamp for query in queryset]
        uuids = [query.uuid for query in queryset]

        response.data = {k:v for k, v in zip(timestamps, uuids)}
        response.status_code = 200
        return response