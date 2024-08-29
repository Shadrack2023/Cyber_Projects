import random
import re

# Path to the password list file
file_path = '/home/scr34tur3/Documents/hackthebox/reports/wifi-hacking-101/edenhill/edenhill_passwordlist'

# List of special characters to choose from
special_characters = ["!", ".", "*", "&", "#", "$"]

# Function to read passwords from a file
def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

# Function to generate new passwords by combining special characters and numbers
def generate_passwords(password_list):
    new_passwords = []
    for password in password_list:
        num = str(random.randint(1, 9999))  # Generate a random number as a string
        special_char = random.choice(special_characters)  # Choose a random special character
        new_password = special_char + password + num  # Combine special character, password, and number
        new_passwords.append(new_password[1:] + new_password[0])  # Add the new password to the list
    return new_passwords

# Read passwords from the file
passwords = read_passwords(file_path)

# Generate new passwords
new_password_list = generate_passwords(passwords)

# Print the new passwords
for new_password in new_password_list:
    print(new_password)
