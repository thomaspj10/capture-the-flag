flag = input("Flag: ")

s = "bzefaza3bze8fcz2b6zzf7z"

banned_chars = "zx5"

for char in banned_chars:
    s = s.replace(char, "")

if flag == s:
    print("Correct flag")
else:
    print("Incorrect flag")    
