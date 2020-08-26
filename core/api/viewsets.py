# my app imports
from core.models import  SendRequest
from .serializers import SendRequestSerializer

# django rest imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class SendRequestViewSet(ModelViewSet):

    serializer_class = SendRequestSerializer

    def get_queryset(self):
        """
            Parameters
            ----------
            None
                This function doesn't has some parameters,
                because all params are providing by request session.

            Returns
            -------
            QuerySet

                This function returns query with objects
                that can be filtered or not, if the.
        """

        params = self.request.query_params

        user = self.request.user

        return SendRequest.objects.order_by('scheduled_time')

    def create(self, request):
        data = request.data
        
        return Response({'ok':'ok'})
        