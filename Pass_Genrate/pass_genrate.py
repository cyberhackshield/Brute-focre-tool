from pyfiglet import Figlet
import itertools

# Custom pass logo
f = Figlet(font="slant")
print(f.renderText("Custom Password Genrate"))
print("Created by raushan\n")

print("Choose Mode")
print("1. Custom Characters")
print("2. Target Information")

mode = input("Enter option: ")

output_file = open("wordlist.txt", "w")
count = 0


def save(password):
    global count
    output_file.write(password + "\n")
    count += 1
    print(f"\rGenerated: {count}", end="")


# -------------------------
# LEET MUTATION FUNCTION
# -------------------------
def leet_mutations(word):

    leet_map = {
        "a": ["@", "4"],
        "e": ["3"],
        "i": ["1"],
        "o": ["0"],
        "s": ["$"],
        "t": ["7"]
    }

    results = [word]

    for i, char in enumerate(word.lower()):
        if char in leet_map:
            new_results = []
            for r in results:
                for replacement in leet_map[char]:
                    mutated = r[:i] + replacement + r[i+1:]
                    new_results.append(mutated)
            results.extend(new_results)

    return list(set(results))


# -------------------------
# MODE 1 : CUSTOM CHARACTERS
# -------------------------
if mode == "1":

    letters = input("Enter letters (a-z or a,b,c) or press Enter: ")
    numbers = input("Enter numbers (0-9 or 1,2,3) or press Enter: ")
    special = input("Enter special chars (!,@,#) or press Enter: ")
    length = int(input("Enter password length: "))

    def parse_input(user_input):

        chars = []

        if not user_input:
            return chars

        if "-" in user_input:
            start, end = user_input.split("-")
            for c in range(ord(start), ord(end) + 1):
                chars.append(chr(c))

        elif "," in user_input:
            chars.extend(user_input.split(","))

        else:
            chars.extend(list(user_input))

        return chars

    char_set = []
    char_set += parse_input(letters)
    char_set += parse_input(numbers)
    char_set += parse_input(special)

    for p in itertools.product(char_set, repeat=length):
        password = "".join(p)
        save(password)


# -------------------------
# MODE 2 : TARGET INFO
# -------------------------
elif mode == "2":

    name = input("Target name: ")
    dob = input("Birth year: ")
    phone = input("Phone number: ")
    email = input("Email username: ")
    pet = input("Pet name: ")
    friend = input("Friend name: ")
    parent = input("Parent name: ")

    words = []

    for item in [name, pet, friend, parent, email]:
        if item:
            words.append(item)

    specials = ["!", "@", "#", "$"]
    numbers = ["123", "007", "786", dob]

    for word in words:

        save(word)

        # mutations
        save(word.lower())
        save(word.upper())
        save(word.capitalize())

        # leet mutations
        mutations = leet_mutations(word)

        for m in mutations:
            save(m)

        # numbers
        for n in numbers:
            save(word + n)
            save(n + word)

        # specials
        for s in specials:
            save(word + s)
            save(s + word)

        # common patterns
        save(word + "@123")
        save(word + dob)
        save(word + "123")
        save(word + "_123")

        # combinations
        for w2 in words:
            if word != w2:
                save(word + w2)
                save(word + "@" + w2)
                save(word + w2 + "123")

else:
    print("Invalid option")

output_file.close()

print(f"\n\nTotal passwords generated: {count}")
print("Saved to wordlist.txt")