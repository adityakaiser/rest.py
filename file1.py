import random
import string

def generate_random_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    all_characters = lower + upper + digits
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    password += [random.choice(all_characters) for _ in range(length - 3)]
    random.shuffle(password)
    
    return "".join(password)

password_length = 10
generated_password = generate_random_password(password_length)

print(f"Generated Random Password: {generated_password}")