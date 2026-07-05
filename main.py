import random
import string
print("***********************")
print("   PASSWORD GENERATOR")
print("***********************")
length = int(input("Enter the password length: "))
characters = string.ascii_lowercase
a = input("Do you need uppercase letters? (Y/N): ")
if a.lower() == "y":
    characters += string.ascii_uppercase
b = input("Do you need digits? (Y/N): ")
if b.lower() == "y":
    characters += string.digits
c = input("Do you need punctuation? (Y/N): ")
if c.lower() == "y":
    characters += string.punctuation
password = ""
for i in range(length):
    password += random.choice(characters)
print("\nGenerated Password:")
print(password)