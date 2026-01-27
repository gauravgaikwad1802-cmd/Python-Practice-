def check_password(password):
    if len(password)<8:
       return False
    if not any (char.title() for char in password):
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any (char.islower() for char in password):
        return False
    if not any (char.isupper() for char in password):
        return False
    if not any (char in "!@#$%^&*" for char in password):
        return False
    return True
result=check_password(password= "Gaurav_123")
print(result)


                 