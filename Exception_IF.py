def split_check(total, number_of_ppl):
  if number_of_ppl <= 1:
    raise ValueError ("More than 1 person is required to split the check")
    return math.ceil(total / number_of_ppl)

  try:
    total_due = float(input("What is the total? "))
    number_of_ppl = int(input("How many people? "))
    amount_due = split_check(total_due, number_of_ppl)
  except ValueError as err:
    print("oh,no!!!!  That's not a valid value.  Please try again....")
    print("({})".format(err))
  else:
    print("each person owes ${}".format(amount_due))
