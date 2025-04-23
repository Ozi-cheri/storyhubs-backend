from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to Storyhubs Api!"
    })

@api_view(['POST'])
def logout_route(request):
    return Response({"message": "You have successfully logged out."})