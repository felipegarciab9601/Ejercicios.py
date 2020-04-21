
inaceptable = 0.0
aceptable = 0.4


dinero = 2400

score = float(input("Please insert the score of the user: "))

if score == 0.0:
  print("Insuficient, Your bonus would be : " + str(dinero*0.0))
elif score == 0.4:
  print("Aceptable, Your bonus would be: " + str(dinero*0.4))  
elif score >= 0.6:
  print("Wonderful, Your bonus would be : " + str(dinero*score))
else:
  print("Sorry request can't be processed")  