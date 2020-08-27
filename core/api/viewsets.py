# app imports
from core.models import SendRequest
from core.api.serializers import SendRequestSerializer
from core.api.handler import SendRequestHandler

# django imports
from django.shortcuts import get_object_or_404

# django rest imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

#   import to implement jwt
from rest_framework.permissions import IsAuthenticated

class SendRequestViewSet(ModelViewSet):

    serializer_class = SendRequestSerializer
    permission_classes = (IsAuthenticated, )

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

        handler = SendRequestHandler(data)

        response = handler.create_object()

        if(response.status):
            return Response(SendRequestSerializer(response.data).data)

        return Response({"Error": response.complement})

    def destroy(self, request, pk):
        """
            Parameters
            ----------
                request: some values that are sending with reques

                pk: value that represent the object
        """
        send_request = get_object_or_404(SendRequest, pk=pk)

        if send_request.status == 'W':
            send_request.delete()
            return Response({"OK": "The values was deleted"})
        else:
            return Response({"Error": "You cannot delete one record that was delivered"})

    def partial_update(self, request, *args, **kwargs):
        id_send = kwargs.get("pk", None)

        s = SendRequestHandler(request.data)

        response = s.try_update_object(id_send) 
        
        return Response({"Result": response.complement})
