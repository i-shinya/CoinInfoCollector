from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from mymodule.myenums import TradeCode
from trade.models import TradeManage, UserInfo

# Create your views here.
class HelloApi(APIView):
    def get(self, request, format=None):
        user = UserInfo.objects.filter(id=1)
        return Response(
            {"message": TradeCode.BIT_FLYER.value}, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        request_data = request.data
        return Response(
            {"message": request_data["message"]}, status=status.HTTP_201_CREATED
        )
