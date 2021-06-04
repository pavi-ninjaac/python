class User:
    active_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def activate(self):
        if self not in self.__class__.active_users:
            self.__class__.active_users.append(self)

    def deactivate(self):
        if self in self.__class__.active_users:
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users
    def find_active(self,obj):
        return obj in self.__class__.active_users


me = User("Keith", "keith@example.com")

print(f"Active: {me.is_active()} Active Users: {User.active_users}")
me.activate()
print(f"Active: {me.is_active()} Active Users: {User.active_users}")
print('diff')
print(f"Active: {me.find_active(me)} Active Users: {User.active_users}")

me.deactivate()
print(f"Active: {me.is_active()} Active Users: {User.active_users}")

print(f"Active users off of `me`: {me.active_users}, Class level: {User.active_users}")
me.active_users = "Just me"
print(f"Active users off of `me`: {me.active_users}, Class level: {User.active_users}")