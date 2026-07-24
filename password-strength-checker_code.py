from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + "=" * 60)
print(Fore.CYAN + "Password Strength Checker")
print(Fore.CYAN + "Note: Press Ctrl + C to exit the program.")
print(Fore.CYAN + "=" * 60)


try:

    while True:

        score = 0

        en = input("\tPassword : ")

        # Length Check
        if len(en) >= 12:
            print("\t", Fore.GREEN + "✔ Password length is Strong")
            score += 1

        elif len(en) >= 8:
            print("\t", Fore.YELLOW + "✔ Password length is Medium")
        else:
            print("\t", Fore.RED + "✘ Password is too short!")

        # Capital Letter Check
        if any(ch.isupper() for ch in en):
            print("\t✔ Capital letter present")
            score += 1
        else:
            print("\t✘ At least 1 Capital letter required")

        # Small Letter Check
        if any(ch.islower() for ch in en):
            print("\t✔ Small letter present")
            score += 1
        else:
            print("\t✘ At least 1 Small letter required")

        # Digit Check
        if sum(ch.isdigit() for ch in en) >= 2:
            print("\t✔ At least 2 Digits present")
            score += 1
        else:
            print("\t✘ At least 2 Digits required")

        # Special Character Check
        if any(ch in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for ch in en):
            print("\t✔ Special character present")
            score += 1
        else:
            print("\t✘ At least 1 Special character required")

        print("\n", "-" * 60)

        # Overall Password Strength
        if score == 5:
            print(Fore.GREEN + "\n🟢 Overall Password Strength : STRONG")

        elif score >= 3:
            print(Fore.YELLOW + "\n🟡 Overall Password Strength : MEDIUM")

        else:
            print(Fore.RED + "\n🔴 Overall Password Strength : WEAK")

        print("\n", "=" * 60, "\n")

except KeyboardInterrupt:
    print(Fore.CYAN + "\n\nProgram Stopped. Thank you for using Password Checker ❤️")
