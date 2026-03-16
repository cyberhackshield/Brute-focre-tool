import hashlib
from pyfiglet import Figlet


# Custom pass logo
f = Figlet(font="slant")
print(f.renderText("Hash Genrated!"))
print("Created by raushan\n")

word = input("Enter word: ")

print("\nChoose Hash Type")
print("1. MD5")
print("2. SHA1")
print("3. SHA256")
print("4. SHA512")

choice = input("Enter option: ")

if choice == "1":
    result = hashlib.md5(word.encode()).hexdigest()

elif choice == "2":
    result = hashlib.sha1(word.encode()).hexdigest()

elif choice == "3":
    result = hashlib.sha256(word.encode()).hexdigest()

elif choice == "4":
    result = hashlib.sha512(word.encode()).hexdigest()

else:
    print("Invalid option")
    exit()

print("\nGenerated Hash:")
print(result)