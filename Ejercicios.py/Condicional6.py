renta = int(input("Please introduce your annual rent: "))

if renta<10000:
  print("Your impositive would be 5%")
elif renta == 10000 and renta<20000:
  print("Your impositve would be 15%")
elif renta == 20001 and renta<35000:
  print("Your impositive would be 20%")  
elif renta == 35001 and renta<60000:
  print("Your impositive would be 30%") 
elif renta>60000:
  print("Your impositive would be for 45%")   
else:
  print("Amount is not valid")  