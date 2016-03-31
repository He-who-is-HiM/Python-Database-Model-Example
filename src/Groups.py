import Database


class Groups(Database):
    def get(self, name):
        return self.query("SELECT * FROM Groups WHERE name = {0}", [name])

    def get_all(self):
        return self.query("SELECT * FROM Groups")

    def get_related_users(self, name):
        return self.query("SELECT * FROM Users WHERE groupId = (SELECT groupId FROM Groups WHERE name = {0})", [name])