
import re


email= input("whats your email?").strip()

if re.search(r"^[^@]+@[^@]+\.(edu|com|org)$", email):

    print("valid")

else:
    print("invalid")































