import random
import string

def generate_password():
    length = int(input("Enter the desired length of the password: "))                      

    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    all_characters = lower_case_letters + upper_case_letters + numbers + symbols

    password_characters = random.sample(all_characters, length)

    generated_password = "".join(password_characters)

    return generated_password

password = generate_password()
print("Generated Password:", password)
