# rest framework imports
from rest_framework.serializers import ModelSerializer

# my imports
from core.models import SendRequest


class SendRequestSerializer(ModelSerializer):

    class Meta:
        model = SendRequest
        fields = ['id',  'recipient', 'scheduled_time',
                  'kind_message', 'msg', 'status_full', 'sender']


class SendRequestAllSerializer(ModelSerializer):

    class Meta:
        model = SendRequest
        fields = ['status',
                  'scheduled_time', 'kind_message', 'msg']
