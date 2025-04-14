# ---et0n--- 15/05/2024

import hashlib
import time
import sys
from colorama import init, Fore, Style
from itertools import product

def loading_animation():
    """Displays a loading animation"""
    for _ in range(10):  # Limit the number of dots to prevent endless loop in the terminal
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")  # Erase the last character
        sys.stdout.flush()

def run_brute_force(target_hash, charset, max_length):
    print("\n[+] Starting Brute Force Attack...\n")
    start = time.time()
    attempts = 0

    # Use loading animation while initializing
    sys.stdout.write("Working")
    sys.stdout.flush()
    loading_animation()
    
    print("\n[+] Starting the attack. Attempting passwords...\n")
    
    for length in range(1, max_length + 1):
        for guess_tuple in product(charset, repeat=length):
            guess = ''.join(guess_tuple)
            attempts += 1
            
            # Show current attempt
            sys.stdout.write(Fore.LIGHTWHITE_EX + f"\rAttempting: {guess}  (Attempt #{attempts})")
            sys.stdout.flush()
            
            # Calculate hash for current attempt
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                duration = time.time() - start
                print(Fore.GREEN + f"\nPassword found: {guess}")
                print(f"Attempts: {attempts}")
                print(f"Time taken: {duration:.2f} seconds\n")
                return

    print("\nOops, passwords did not match!")

