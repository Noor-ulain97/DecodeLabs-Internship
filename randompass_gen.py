import secrets
import string

def generate_password(length, use_symbols):
    if use_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password


def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"


def main():
    print("====== PASSWORD GENERATOR ======")

    while True:
        print("\n1. Generate Password")
        print("2. Exit")

        choice = input("Select option: ")

        if choice == "1":
            try:
                length = int(input("Enter password length: "))

                if length < 4:
                    print("Length too short (minimum 4).")
                    continue

                symbol_input = input("Include symbols? (yes/no): ").lower()
                use_symbols = symbol_input == "yes"

                password = generate_password(length, use_symbols)
                strength = check_strength(password)

                print("\nGenerated Password:", password)
                print("Strength:", strength)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            print("Goodbye 🔐")
            break

        else:
            print("Invalid option!")


main()1