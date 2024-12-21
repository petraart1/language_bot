__all__ = [
    "User"
]

class User:
    _id: int
    _telegram_id: int
    _username: str
    _name: str

    def __init__(self, id: int, telegram_id: int=None, username: str=None, name: str=None):
        self._id = id
        self._telegram_id = telegram_id
        self._username = username
        self._name = name

    def get_id(self) -> int:
        return self._id

    def set_id(self, new_id: int) -> None:
        self._id = new_id

    def get_telegram_id(self) -> int:
        return self._telegram_id

    def set_telegram_id(self, new_telegram_id: int) -> None:
        self._id = new_telegram_id

    def get_username(self) -> str:
        return self._username

    def set_username(self, new_username: str) -> None:
        self._username = new_username

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name