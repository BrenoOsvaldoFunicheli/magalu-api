import re

class Phone:

    def __init__(self, number):
        response = PhoneValidator(number)

        if response:
            self.number = number
        else:
            raise Exception("This Phone doesn't valid number")    
    

class PhoneValidator:

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def is_valid(self):
        response = re.match(r"(\(?\d{2}\)?\s)?(\d{4,5}\-{0,1}\d{4})", self.phone_number)
        if response:
            return True
        else:    
            return False


if __name__ == "__main__":
    p = PhoneValidator("169810846")
    print(p.is_valid())