choice = int(input("Menu:\n1. Tea\n2. Coffee\n3. Juice\nEnter choice: "))
match choice:
    case 1: print("You selected Tea.")
    case 2: print("You selected Coffee.")
    case 3: print("You selected Juice.")
    case _: print("Invalid choice!")