class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.log_level = 'INFO'

    def set_level(self, val):
        if not self.__instance:
            raise ValueError('The instance has not created')
        self.log_level = val

    @staticmethod
    def get_logger():
        if not Logger.__instance:
            Logger.__new__(Logger)
        return Logger.__instance
