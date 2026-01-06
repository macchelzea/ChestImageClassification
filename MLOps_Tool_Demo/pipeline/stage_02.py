import os

with open("artifacts/input.txt", "r") as f:
   s = f.read()
   print(s)


with open("artifacts/output.txt", "w") as f:
   f.write("Welcome guys.")
   

with open("artifacts/output.txt", "a") as f:
   f.write("\nWelcome ladies")
   
