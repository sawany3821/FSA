"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

urlpatterns = [
    # path("api/corporations/", include("corporations.urls")),
    # path("api/documents/", include("documents.urls")),
]


@api_view(("GET",))
def url_list(request):
    url_list = []
    for url in urlpatterns:
        route = url.pattern._route
        if route != "":
            url_list.append(route)
    return Response({"results": url_list})


urlpatterns += [
    path("", url_list),
]

# DEBUGがTrueの場合
if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
