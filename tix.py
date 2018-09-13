import math

TICKET_PRICE = 10

tickets_remaining = 100


# output how many tickets remain using tickets_remaining available
while tickets_remaining >= 1:
  print("there are {} tickets remaining.".format(tickets_remaining))

# gather user's name and assign it to a variable

  user_name = input("Please enter your first name: ")
# prompt user by name and ask how many tickets they would like
  num_tix = input("Hello {}, there are {} tickets remaining.  How many would you like:  ".format(user_name,tickets_remaining))

  try:
    num_tix = int(num_tix)
    if num_tix > tickets_remaining:
      raise ValueError("there are only {} tickets remaining".format(tickets_remaining))
  except ValueError as err:
    print("please enter a valid number of tickets to purchase.")

    # expect a ValueError
    num_tix = int(num_tix)
    # calculate the price (number of tix x price) and assign it to a variable
  else:
    tix_cost = num_tix * TICKET_PRICE

    # output the price to the screen
    print("Your total cost is $ {}".format(tix_cost))

    # prompt user if they want to proceed. Y/N?
    decision = input("Would you like to purchase {} tickets? Y/N ".format(num_tix))

    # if Y,
    if decision.upper() == "Y":
      # print out to the screen "SOLD! The tickets are yours!!  We'll see you Saturday!!!"
      print("SOLD! The tickets are yours!!  We'll see you Saturday!!!")

      # declare the number of tix remaining after purchase
      tickets_remaining -= num_tix

    #otherwise....
    else:
      print("Thanks for browsing {}".format(user_name))
    # Thank them by name
    
