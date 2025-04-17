import hashlib
import time

def run_dictionary_attack(target_hash, wordlist_path):
    print("\n[+] Starting Dictionary Attack...\n")
    start = time.time()
    attempts = 0

    try:
        with open(wordlist_path, 'r', errors='ignore') as file:
            for line in file:
                word = line.strip()
                attempts += 1
                word_hash = hashlib.sha256(word.encode()).hexdigest()
                if word_hash == target_hash:
                    duration = time.time() - start
                    print(f"\nPassword found: {word}")
                    print(f"Attempts: {attempts}")
                    print(f"Time taken: {duration:.2f} seconds\n")
                    return
        print("Oops, password not found.")
    except FileNotFoundError:
        print("Oh no! Wordlist file not found.")

