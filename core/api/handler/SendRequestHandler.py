import datetime as dt

# my classes
from core.models import SendRequest
from .TypeMessageHandler import ComunicateValidatorStrategy
from helpers.communicators import SimpleResponse

# django imports
from django.shortcuts import get_object_or_404


class SendRequestHandler:

    def __init__(self, snd_request):
        self.snd_request = snd_request
        self.validators = {
            "recipient": self.validate_recipient, "scheduled": self.validate_scheduled_time
        }

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

    def validate_scheduled_time(self):
        scheduled = self.snd_request.get('scheduled_time', None)

        if scheduled is None:
            scheduled = dt.datetime.now()
        else:
            scheduled = dt.datetime.strptime(scheduled, '%Y-%m-%d')

        limit_schedule = dt.datetime.now()-dt.timedelta(hours=0.2)

        return limit_schedule < scheduled

    def is_valid(self, conditions=[True]):
        """
            Parameters
            ----------
                condition: this parameter is an array with
                all condition values that it was tested
                to validate object sented

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

        return all(conditions)

    def create_object(self):
        """
            Description
            -----------
                This method tests if object is valid to send and persist it
                Insted of send object or other message I send The response object

            Conditions
            ----------
                Valid method acept some params that are conditions that 
                need to be validated

        """

        conditions = [
            self.validators.get("recipient", None)(),
            self.validators.get("scheduled", None)()
        ]

        if self.is_valid(conditions):
            #   remove csrf token to make object
            self.snd_request.pop('csrfmiddlewaretoken', None)

            # make object to send
            obj = SendRequest(**self.snd_request)

            obj.save()

            return SimpleResponse(True, obj)
        else:
            return SimpleResponse(False, complement="Some of fields isn't valid")

    def get_need_conditions(self):

        conditions = [True]

        if self.snd_request.get("recipient", False) or self.snd_request.get("kind_message", False):
            conditions.append(self.validators.get("recipient")())

        if self.snd_request.get("scheduled_time", False):
            conditions.append(self.validators.get("scheduled")())

        
        return conditions

    def try_update_object(self, pk):
        """
            Description
            -----------
                First This method get need conditions to send to 
                method of the validation, after it valides if 

        """
        conditions = self.get_need_conditions()
        
        if self.is_valid(conditions):
            
            try:
                send_object = get_object_or_404(SendRequest, pk=pk)

                if send_object.status == "W":

                    self.remove_url_params(['id'])

                    send_request = SendRequest.objects.filter(pk=pk)

                    send_request.update(**self.snd_request)

                    return SimpleResponse(status=True, complement="Object Alter")
                else:
                    raise Exception("This object is done, you cannot modify")
            except Exception as e:
                return SimpleResponse(False, complement=str(e))

        return SimpleResponse(False, complement="This object isn't valid") 

    def remove_url_params(self, params=[]):
        """
            Params
            ------
                params: values that need to be removed of object
                to conclude operations
        """

        for i in params:
            self.snd_request.pop(i, None)