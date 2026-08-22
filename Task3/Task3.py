import random
import string

# Ask the user for the desired password length
length = int(input("Enter password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random password
password = ""

for _ in range(length):
    password += random.choice(characters)

# Display the generated password
print("Your random password is:", password)