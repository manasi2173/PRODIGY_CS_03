import re


def assess_password_strength(pass1):
    length = len(pass1)
    uppercase = any(char.isupper() for char in pass1)
    lowercase = any(char.islower() for char in pass1)
    digits = any(char.isdigit() for char in pass1)
    special_characters = re.match(r'^[\w]*$', pass1) is None

    strength = 0
    feed = []

    if length >= 8:
        strength += 1
    else:
        feed.append("Password should be at least 8 characters long.")

    if uppercase and lowercase:
        strength += 1
    else:
        feed.append("Password should contain both uppercase and lowercase letters.")

    if digits:
        strength += 1
    else:
        feed.append("Password should contain at least one digit.")

    if special_characters:
        strength += 1
    else:
        feed.append("Password should contain at least one special character.")

    if strength == 4:
        feed.append("Strong password!")
    elif strength >= 2:
        feed.append("Moderate password.")
    else:
        feed.append("Weak password. Please consider choosing a stronger one.")

    return feed


password = input("Enter your password: ")
feedback = assess_password_strength(password)
for message in feedback:
    print(message)