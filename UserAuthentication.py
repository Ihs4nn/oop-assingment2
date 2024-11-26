from UserDetails import User

# Predefined User for prototype:
accepted_user = User("admin1", "1", "admin")

def validate_login(userid, password):
    # Validates user credentials based on username and password accepted above
    if userid == accepted_user.username and password == accepted_user.password:
        return True
    return False