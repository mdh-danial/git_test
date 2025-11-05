# testing git with python

# variables (1st commit)
name = input("What is your name my friend?")

# conditionals (2nd commit)
try:
    check_name = str(name)
except ValueError:
    print("There's no way this will print, right?")

if check_name.lower() == "world":
    print("Is that you, world?")
else:
    print(f"Nevermind. Hello, {name}")

# loops (3rd commit)
print("Your name is spelt:", end=" ")
n = len(check_name)
for i in range(n):
    if i == n - 1:
        print(check_name[i])
    else:
        print(check_name[i], end="-")

# functions (4th commit)