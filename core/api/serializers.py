# rest framework imports
from rest_framework.serializers import ModelSerializer

# my imports
from core.models import SendRequest


class SendRequestSerializer(ModelSerializer):

    class Meta:
        model = SendRequest
        fields = ['id', 'scheduled_time', 'recipient','type_message', 'msg']
