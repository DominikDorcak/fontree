class NotFoundException(Exception):
    def __init__(self):
        self.message = "Requested value not found"
        self.errorcode = 404
        super().__init__(self.message)