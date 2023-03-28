from hashlib import sha256

flag = input("Flag: ")

if len(flag) != 4:
    print("The flag must be 4 characters long.")
    exit()

valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
for char in flag:
    if char not in valid_chars:
        print("The flag contains invalid characters.")
        exit()

hashed_flag = sha256(flag.encode('utf-8')).hexdigest()

if hashed_flag == "400654291cf7624e414656ae228380e9694ae22a6d404c6e2e9b3e23a8e5760f":
    print("Correct flag.")
else:
    print("Incorrect flag.")
