# Cоздать класс Logger, который предоставляет глобальный доступ к одному экземпляру логгера в приложении.
# Класс Logger имеет атрибут log_level, который хранит текущий уровень логирования, по умолчанию нужно проставить
# значением INFO
# Класс Logger также должен иметь:
# метод класса set_level, который принимает новый уровень логирования и записывает его в атрибут log_level.
# При этом обязательно проверьте был ли создан экземпляр. В случае отсутствия экземпляра необходимо необходимо
# возбуждать исключение  ValueError('The instance has not created')
# статический метод get_logger, который возвращает экземпляр синглтона. Если экземпляр еще не существует,
# его необходимо создать

# class Logger:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super(Logger, cls).__new__(cls)
#             cls.__instance.initialize_settings()
#         return cls.__instance
#
#     @classmethod
#     def initialize_settings(cls):
#         cls.log_level = "INFO"
#
#     @classmethod
#     def set_level(cls, val):
#         if not cls.__instance:
#             raise ValueError('The instance has not created')
#         cls.log_level = val
#
#     @staticmethod
#     def get_logger():
#         if not Logger.__instance:
#             Logger.__new__(Logger)
#         return Logger.__instance
#
#
# logger_1 = Logger.get_logger()
# print(logger_1.log_level)  # Выведет "INFO"
# Logger.set_level("DEBUG")
# print(logger_1.log_level)  # Выведет "DEBUG"
#
# logger_2 = Logger.get_logger()
# print(logger_2.log_level)  # Выведет "DEBUG"
# print(logger_2 is logger_1)


# ----------------------------------------------------------------------------------------------------------------------

# (2)

# В данном примере у нас имеется несколько пустых классов и на каждым вещается декоратор singleton, который вы должны будете реализовать
# Функция-декоратор singleton должна сохранять в себе для каждого класса один созданный экземпляр при первом вызове.
# При последующих вызовах возвращать ранее созданный экземпляр для данного класса



# v1
# def singleton(cls=None):
#
#     cls.__instance = None
#
#     def wrapper(*args, **kwargs):
#         nonlocal cls
#         if cls.__instance is None:
#             cls.__instance = cls()
#             return cls.__instance
#         return cls.__instance
#
#     return wrapper
##################################################

# v1

def singleton(cls):
    class Cls:
        inst = None
        def __new__(cls):
            if not cls.inst:
                cls.inst = super(Cls, cls).__new__(cls)
            return cls.inst
    return Cls



@singleton
class Logger:
    pass


@singleton
class AppConfig:
    pass


@singleton
class SMTPServerConfig:
    pass


log = Logger()
app_conf = AppConfig()
app_conf_2 = AppConfig()
smtp_conf = SMTPServerConfig()
assert log is Logger()
assert app_conf is app_conf_2
assert smtp_conf is SMTPServerConfig()
assert log is not app_conf
assert log is not smtp_conf
assert app_conf is not smtp_conf
print('Good')
