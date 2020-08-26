import datetime

# my classes
from core.models import SendRequest
from .TypeMessageHandler import ComunicateValidatorStrategy
from helpers.communicators import SimpleResponse

class SendRequestHandler:

    def __init__(self, snd_request):
        self.snd_request = snd_request

    def validate_recipient(self):
        """
            Description
            -----------
                Strategy implentation that decide who validator
                will be run, based in kind_of_message
        """

        validator = ComunicateValidatorStrategy().decide(
            self.snd_request.get('kind_message', None))

        return validator.is_valid(self.snd_request.get('recipient', None))

    def validate_time(self):
        x = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        print()

    def is_valid(self):
        """
            Description
            -----------
                This method is a Middleware validator, that validates
                if the senderRequest is correct to insert some value 
                when received of the Resquest

            Return
            ------
                If SendRequest object is valid, then returns True 
                else returns False

        """

        #   chain of conditions that will be verified
        #   with all operation, it's
        chain_conditions = [
            self.validate_recipient(),

        ]

        return all(chain_conditions)


    def create_object(self):

        if self.is_valid():
            #   remove csrf token to make object
            self.snd_request.pop('csrfmiddlewaretoken', None)

            # make object to send
            obj = SendRequest(**self.snd_request)
            
            obj.save()
            
            #   Insted of send object or other message
            #   I send The response object
            return SimpleResponse(True, obj)
        else:
            return SimpleResponse(False, complement="Some of fields isn't valid")
