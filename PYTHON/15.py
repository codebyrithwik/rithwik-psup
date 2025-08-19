ch = input("Enter a character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch.isalpha():
        print(f"{ch} is an Alphabet.")
    elif ch.isdigit():
        print(f"{ch} is a Digit.")
    else:
        print(f"{ch} is a Special Character.")