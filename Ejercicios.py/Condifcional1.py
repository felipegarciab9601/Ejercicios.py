password = "Sergio3104"

passuser=str(input("Please introduce the password: "))

if passuser == password.lower():
  passuser = True
  print("Contraseña correcta")
else:
  passuser = False
  print("Contraseña incorrecta")  