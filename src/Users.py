import Database


class Users(Database):
    def get(self, user):
        return self.query("SELECT TOP 1 * FROM Users WHERE name = {0}", [user])

    def get_all(self):
        return self.query("SELECT * FROM Users")

    def get_all_registered(self):
        return self.query("SELECT * FROM Users WHERE registered = 1")

    def get_registered(self, user):
        return self.query("SELECT TOP 1 * FROM Users WHERE name = {0} AND registered = 1", [user])