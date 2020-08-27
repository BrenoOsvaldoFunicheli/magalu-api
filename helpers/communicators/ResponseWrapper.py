class SimpleResponse:

    def __init__(self, status, data=None, complement=None):

        self.status = status
        self.data = data
        self.complement = complement

    def get_response(self):
        pass

    def __repr__(self):
        return self.status
