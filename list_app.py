def show_help():
    print("what should we pick up from the store?")
    print("""
Enter 'DONE' to stop adding itemsself.
Enter 'HELP' for this helpself.
""")

show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item =='HELP':
        show_help()
        continue
