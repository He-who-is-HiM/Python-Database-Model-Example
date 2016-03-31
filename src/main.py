from Users import Users
from Groups import Groups

user = Users().get("John")
groups = Groups().get_related_users("Administrators")