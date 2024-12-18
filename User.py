class User:
    def __init__(
            self,
            username,
            email,
            password
    ):
        self.__username = ""
        self.__email = ""
        self.__password = ""

        self.set_username(username)
        self.set_email(email)
        self.set_password(password)

    def set_username(self, username):
        if len(username) < 15:
            return 1
        self.__username = username
        
    def get_username(self):
        return self.__username
    
    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
    
    def set_password(self, password):
        if len(password) < 8:
            return 1
        elif len(password) > 128:
            return 2
        self.__password = password

    def get_password(self):
        return self.__password
    