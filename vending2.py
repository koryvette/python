candy = ["TAKE 5", "SNICKERS", "WHATCHAMACALLIT", "REESE CUP", "KIT KAT"]
chips = ["FUNYUNS", "CHEETOHS", "DORITOS", "LAYS", "PRETZELS"]
drinks = ["COKE", "DR PEPPER", "MT DEW", "BIG RED"]

while True:
    try:
        choice = input("Would you like a drink, candy, or chips?").lower()
        if choice == 'drink':
            snack = drinks.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        elif choice.upper() == 'DONE' or choice.upper() == 'QUIT':
            break
        else:
            print("sorry, I didn't understand your request")
            continue
    except IndexError:
        print("We are all out of {}".format(choice))
    else:
        print("here's your {}: {}".format(choice, snack))
