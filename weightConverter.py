weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"You are {int(weight) * 0.45} kilos.")
if unit.upper() == 'K':
    print(f"You are {int(weight) / 0.45} pounds.")