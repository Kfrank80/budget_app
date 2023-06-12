class CustomExceptions(Exception):
    pass


class NullStrArgument(CustomExceptions):

    def __init__(self, function, message):
        self.function = function
        self.message = message

    pass
