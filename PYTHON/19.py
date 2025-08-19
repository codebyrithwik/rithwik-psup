fuel = int(input("Choose fuel type (1. Petrol, 2. Diesel, 3. Electric): "))
match fuel:
    case 1: print("You chose Petrol.")
    case 2: print("You chose Diesel.")
    case 3: print("You chose Electric.")
    case _: print("Invalid choice!")