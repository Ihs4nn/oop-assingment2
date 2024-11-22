class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def is_authorized(self, action):
        permissions = {
            'admin': ['add', 'remove', 'move', 'view']
        }
        return action in permissions.get(self.role, [])