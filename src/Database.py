class Database:
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__host = None
        self.__port = None
        pass

    def connect(self, host, port):
        self.__host = host
        self.__port = port
        pass

    def authenticate(self, username, password):
        self.__username = username
        self.__password = password
        pass

    def query(self, querystring, parameters):
        # query goes here
        return []  # result gets returned here
        pass