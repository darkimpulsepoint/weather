import json

from django.http import HttpResponse
from django.shortcuts import render

from .utils import *
# Create your views here.


def start(request):
    return render(request, "hub/index.html")


def get_videos(request):
    search = request.GET.get("search")
    page = request.GET.get("page", 1)
    videos = parse_hub(search, page)
    json_object = json.dumps(videos)
    return HttpResponse(json_object)