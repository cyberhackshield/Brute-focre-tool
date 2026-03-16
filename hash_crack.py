import hashlib
from pyfiglet import Figlet


# Custom pass logo
f = Figlet(font="slant")
print(f.renderText("Hash Craked!"))
print("Created by raushan\n")

print("=== Python Hash Cracker ===")

target_hash = input("Enter hash: ").lower()

print("\nSelect Hash Type")
print("1. MD5")
print("2. SHA1")
print("3. SHA256")
print("4. SHA512")

choice = input("Enter option: ")
wordlist = input("Enter wordlist file: ")

# select hash function
if choice == "1":
    hash_function = hashlib.md5
elif choice == "2":
    hash_function = hashlib.sha1
elif choice == "3":
    hash_function = hashlib.sha256
elif choice == "4":
    hash_function = hashlib.sha512
else:
    print("Invalid option")
    exit()

print("\nCracking password...\n")

try:
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:

            # clean wordlist line
            word = line.strip()

            if not word:
                continue

            # remove junk after '!'
            word = word.split("!")[0]

            hashed = hash_function(word.encode()).hexdigest()

            # show only short preview
            display_word = word[:20]

            print(f"Comparing: {display_word}", end="\r")

            if hashed == target_hash:
                print(f"\n\n[+] Password Found: {word}")
                break
        else:
            print("\n[-] Password not found in wordlist")

except FileNotFoundError:
    print("Wordlist file not found")