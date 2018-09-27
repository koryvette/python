import os

# Create new empty list named shopping_list
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Create a function named add_to_list that declares paramter named item
def add_to_list (item):
    # add the item to the list
    shopping_list.append(item)
    # notify user that the item was successfully added
    print("{} was successfully added.  you now have {} items".format(item,len(shopping_list)))
    show_list()

def show_help():
    print("what should we pick up from the store?")
    print("""
Enter 'DONE' to stop adding itemsself.
Enter 'HELP' for this helpself.
Enter 'SHOW' to show complete list.
""")

def show_list():
    clear_screen()
    print("Here's you list:")
    for item in shopping_list:
        print("* " + item)

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() =='HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    else:
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)
show_list()
