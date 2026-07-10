from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def health(request):
    return Response({
        "status": "ok",
        "message": "WineShop API Running"
    })


urlpatterns = [

    path("health/", health),

]