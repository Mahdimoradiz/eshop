from django.core.exceptions import ValidationError as DjangoValidationError


class StartWithZero:
    message = "Phone number should start with 0"
    code = "invalid"
    
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code    
    
    def __call__(self, value):
        if value[0] != '0':
            raise DjangoValidationError(self.message, code=self.code)