from validate_email import validate_email

class EmailValidator:

    def __init__(self, email):
        self.email = email

    def is_valid(self):
        return validate_email(self.email)
