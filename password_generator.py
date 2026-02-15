import random
import string

print("---- Simple Password Generator ----")

try:
    length = int(input("Enter the length of password: "))

    if length <= 0:
        print("Length must be greater than 0")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

except:
    print("Please enter a valid number!")
