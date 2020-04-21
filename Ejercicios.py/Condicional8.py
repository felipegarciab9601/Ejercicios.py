user = str(input("Please introduce your name: "))
age_user = int(input("Please introduce your age: "))


if age_user <0:
  print("Invalid age please try again")
elif age_user <4:
  print("Your entrance is free")
elif age_user <=18:
  print("Your entrance will be $5")
elif age_user >18:
  print("Your entrance will be $10")
else:
  print("Sorry command not valid")    
