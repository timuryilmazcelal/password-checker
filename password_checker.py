import random
password = input("Enter your password: ")

special_characters = "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "<", ">", "?", "/", "`", "~"

random_lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

random_uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

random_numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def check_password_strength(password):


    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    if " " in password:
        print("Password should not contain spaces.")
        return

    if len(password) < 8:
        print("Password is too short. It must be at least 8 characters long.")

    for char in password:
        if char.isupper():
            has_upper = True
 

    for char in password:
        if char.islower():
            has_lower = True


    for char in password:
        if char.isdigit():
            has_digit = True

    for char in password:
        if not char.isalnum() and not char.isspace():
            has_special = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")

    if not has_lower:
        print("Password must contain at least one lowercase letter.")

    if not has_digit:
        print("Password must contain at least one digit.")

    if not has_special:
        print("Password must contain at least one special character.")

    def score():
        score = 0

        if len(password) >= 8:
            score += 1

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_digit:
            score += 1

        if has_special:
            score += 1



        if 4 <= score <= 5:
            print("Password strength: Strong")
        elif 2 <= score < 4:
            print("Password strength: Medium")
        else:
            print("Password strength: Weak")
    score()

    def password_suggest(password):

        extra = []
        if not has_special:
            extra.append(random.choice(special_characters))
        if not has_upper:
            extra.append(random.choice(random_uppercase))
        if not has_lower:
            extra.append(random.choice(random_lowercase))
        if not has_digit:
            extra.append(random.choice(random_numbers))
        while len(password) + len(extra) < 8:
            extra.append(random.choice(random_lowercase + random_uppercase + random_numbers + special_characters))
        
        new_password = ""

        for char in password:
            new_password += char
               
            if extra:
                new_password += extra.pop()

        while extra:
            new_password += extra.pop()
            
        return new_password
    
    suggested_password = password_suggest(password)
    print(f"Suggested password: {suggested_password}")



check_password_strength(password)
