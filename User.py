from check_user_curr import check_number
from check_user_curr import check_password


class User:
    def __init__(self,name:str, id:int, password:str):
        self.name = name
        self._id = id
        self.password = password
        check_number(self._id)
        check_password(self.password)