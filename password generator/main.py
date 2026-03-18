import secrets# this is the module which take the choice from a buch of choices but make it secure 
import string# it is just a string 


def generate_secure_password(length=20):
    charaters = string.ascii_letters + string.digits+string.punctuation


    password = ''.join(secrets.choice(charaters) for _ in range(length))
    return password


print(generate_secure_password())#generate the unique password of 12 digits 


