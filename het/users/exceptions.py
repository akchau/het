class AccountBaseException(Exception):
    """Базовый класс исключений для аккаунта."""


class SectionNotFoundException(AccountBaseException):
    """Исключение если не найдена такая секция меню."""
    def __init__(self, name, message="Секция {name} не найдена."):
        formatted_message = message.format(name=name)
        super().__init__(formatted_message)


class NotCorrectHeadException(AccountBaseException):
    """Исключение если не подключен распаковщик."""
    def __init__(self, message="Неверно указан заголовок."):
        formatted_message = message.format()
        super().__init__(formatted_message)


class NotCorrectContextDictException(AccountBaseException):
    """Исключение если не подключен распаковщик."""
    def __init__(self, message="Неверно указан заголовок."):
        formatted_message = message.format()
        super().__init__(formatted_message)