import os

# Create new empty list named shopping_list
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Create a function named add_to_list that declares paramter named item
def add_to_list (item):
    show_list()
    if len(shopping_list):
        position = input("Where should i add {}?\n"
                         "press ENTER to add to the end of the list\n"
                         ">".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

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

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)

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
        add_to_list(new_item)
show_list()
