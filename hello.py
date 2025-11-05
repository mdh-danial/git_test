# testing git with python

# variables (1st commit)
name = input("What is your name my friend?")
name = name.strip()

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
def spell(name):
    n = len(name)
    for i in range(n):
        if i == n - 1:
            print(check_name[i])
        else:
            print(check_name[i], end="-")

# recursion
def blocks(letters, n):
    
    # base case
    if letters <= 0:
        return
    
    # printing whitespace
    for i in range(letters - 1):
        print(" ", end="")
    
    # print block (#)
    for i in range(n):
        if i == n - 1:
            print("#")
        else:
            print("#", end="")
    
    # recursive case
    blocks(letters - 1, n + 1)
    


while True:
    check = input("Wanna see something cool? (y/n)")
    check = check.strip().lower()

    if check == "y":
        # recurse
        letters = len(name)
        blocks(letters, 1)
        break
    elif check == "n":
        print("Ok... :(") 
        break
    else:
        print("Please enter y or n.")