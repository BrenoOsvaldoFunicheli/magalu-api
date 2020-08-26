from helpers.validators import PhoneValidator
from helpers.validators import EmailValidator

class SmsHandler:

    @staticmethod
    def is_valid(phone_number):
        
        return PhoneValidator(phone_number).is_valid()


class EmailHandler:

    @staticmethod
    def is_valid(email):
        return EmailValidator(email).is_valid()

    @staticmethod
    def why():
        return "Email is not valid"

class WhatsappHandler:

    @staticmethod
    def is_valid(phone_number):
        return PhoneValidator(phone_number).is_valid()

    @staticmethod
    def why():
        return "Number Don't Match"

class PushHandler:

    @staticmethod
    def is_valid(phone_number):
        return PhoneValidator(phone_number).is_valid()

    @staticmethod
    def why():
        return "Number Don't Match"

class ErrorHandler:
    @staticmethod
    def is_valid(phone_number):
        return False

    @staticmethod
    def why():
        return "Number Don't Match"
    

class ComunicateValidatorStrategy:

    def __init__(self):
        self.decider = {
            'SMS': SmsHandler,
            'WTA': WhatsappHandler,
            'EML': EmailHandler,
            'PSH': PushHandler,
        }

    def decide(self, kind_message):
        return self.decider.get(kind_message, ErrorHandler)
