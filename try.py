# (x > 3) will raise an error because x is not defined:
try:
  x > 3
except:
  print("Something went wrong")
print("Even if it raised an error, the program keeps running")
