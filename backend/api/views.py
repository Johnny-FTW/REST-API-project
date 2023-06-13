from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body # byte str of json
    data = {}
    try:
        data = json.loads(body) #str json -> py dic
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    data['content_type'] = request.content_type

    return JsonResponse(data)