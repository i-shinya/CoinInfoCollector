from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from mymodule.myenums import TradeCode

# Create your views here.
class ExternalApi(APIView):
    def get(self, request, format=None):
        return Response({"message": TradeCode.ZAIF.value}, status=status.HTTP_200_OK)
