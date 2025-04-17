import argparse
import os
from colorama import init, Fore, Style
from cracker.brute_force import run_brute_force
from cracker.dictionary_attack import run_dictionary_attack

# Initialize colorama
init(autoreset=True)

def print_logo():
    with open("assets/logo.txt") as f:
        logo = f.read()
    print(Fore.GREEN + logo)

def interactive_menu():
    print_logo()
    print(Fore.CYAN + "\n[1] Brute Force Attack")
    print(Fore.CYAN + "[2] Dictionary Attack")
    print(Fore.RED + "[3] Exit")

    choice = input(Fore.YELLOW + "\n>> Choose an option: ")
    if choice == "1":
        hash_input = input("Enter hash to crack: ")
        charset = input("Charset (e.g., abc123): ")
        max_length = int(input("Max password length: "))
        run_brute_force(hash_input, charset, max_length)
    elif choice == "2":
        hash_input = input("Enter hash to crack: ")
        wordlist = input("Path to wordlist: ")
        run_dictionary_attack(hash_input, wordlist)
    else:
        print("Buh-bye...")

def cli_mode(args):
    if args.attack == "brute":
        run_brute_force(args.hash, args.charset, args.max_length)
    elif args.attack == "dict":
        run_dictionary_attack(args.hash, args.wordlist)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute Force Password Cracker")
    parser.add_argument("--attack", choices=["brute", "dict"], help="Attack type")
    parser.add_argument("--hash", help="Hash to crack")
    parser.add_argument("--charset", help="Charset for brute force")
    parser.add_argument("--max-length", type=int, help="Max password length")
    parser.add_argument("--wordlist", help="Path to dictionary file")

    args = parser.parse_args()

    if args.attack:
        cli_mode(args)
    else:
        interactive_menu()

