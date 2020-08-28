# app imports
from core.models import SendRequest
from core.api.serializers import SendRequestSerializer,SendRequestAllSerializer
from core.api.handler import SendRequestHandler

# django imports
from django.shortcuts import get_object_or_404

# django rest imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

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


        return SendRequest.objects.filter(record_status="A").order_by('scheduled_time')

    def create(self, request):
        data = request.data
        
        # setting value of the current user that created this record
        data['sender'] = request.user
        
        handler = SendRequestHandler(data)

        response = handler.try_create_object()

        if(response.status):
            return Response(SendRequestSerializer(response.data).data)
        

        return Response({"Error": response.complement}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """
            Parameters
            ----------
                request: some values that are sending with reques

                pk: value that represent the object
        """
        send_request = get_object_or_404(SendRequest, pk=pk)

        send_request.record_status = "D"
        send_request.save()

        # here you can set some domain knowlegde
        # to block deleted situation when
        return Response({"OK": "The values was deleted"})
       
    def partial_update(self, request, *args, **kwargs):
        
        id_send = kwargs.get("pk", None)

        s = SendRequestHandler(request.data)

        response = s.try_update_object(id_send) 

        return Response({"Result": response.complement}, status=response.status)

    @action(methods=["get"], detail=False)
    def needed_send(self, request):

        objects_need_send = SendRequest.objects.filter(record_status="A", status="W")

        serializer = SendRequestAllSerializer(objects_need_send)

        from rest_framework.renderers import JSONRenderer

        json = JSONRenderer().render(serializer.data)
        print(json)
        return Response(json)
