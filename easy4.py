flag = input("Flag: ")

s = "x = 2;y = 5"

s1 = f"""
import random

{s}
for _ in range(10):x += y;y = 6
random.seed(y * x)
"""

s2 = """
r = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=16))

if r == flag: print("Correct flag.") 
else: print("Incorrect flag")
"""

exec(s1 + s2)
