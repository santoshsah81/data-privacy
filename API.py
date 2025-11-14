#Write a Python program that reads a file containing a list of usernames and passwords, one pair per line (separated by a comma). It checks each password to see if it has been leaked in a data breach. You can use the "Have I Been Pwned" API (https://haveibeenpwned.com/API/v3) to check if a password has been leaked.
import hashlib
import requests

def check_password_pwned(password: str) -> int:
    """
    Returns the number of times the password has appeared in data breaches.
    If 0, the password has not been found.
    """

    # Step 1: Hash the password using SHA-1 (HIBP requires SHA-1)
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1[:5]       # First 5 characters
    suffix = sha1[5:]       # Remainder of the hash

    # Step 2: Query the API for all hashes starting with prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError("Error fetching data from HaveIBeenPwned API")

    # Step 3: Check if our hash suffix is in the returned list
    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return int(count)

    return 0  # Not found


def check_passwords_in_file(filename: str):
    """
    Reads a file of username,password pairs and checks each password for breaches.
    """

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            username, password = line.split(',')

            count = check_password_pwned(password)

            if count > 0:
                print(f"[!] Password for user '{username}' has been leaked {count} times.")
            else:
                print(f"[✓] Password for user '{username}' is safe (not found in breaches).")


# ----------------------
# MAIN PROGRAM
# ----------------------
if __name__ == "__main__":
    filename = input("Enter the filename containing username,password list: ")
    check_passwords_in_file(filename)
