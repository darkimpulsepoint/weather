import os
from config.settings import BASE_DIR

from django.shortcuts import render


# Create your views here.


def view_js_for_app(request, app_name):
    files = os.listdir(f"{BASE_DIR}/{app_name}/static/{app_name}/js")
    hrefs = [
        {
            "name": file,
            "href": f"/static/{app_name}/js/{file}"
        } for file in files
    ]
    context = {
        "hrefs": hrefs
    }
    return render(request, "debug_tools/index.html", context=context)
