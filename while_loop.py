password = input("please enter your super secret password: ")
attempt_count = 1
while password != 'slim shady':
  if attempt_count >= 3:
    sys.exit("too many attempts")
  password = input("Invalid password, please try again:  ")
  attempt_count += 1
print("Welcome to Detroit!!")
