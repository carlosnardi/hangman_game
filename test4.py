

list = ["a","b","c"]

list2 = ["_","_","_"]

while True: 
  for i, item in enumerate(list):
    user = input("letter: ")
    if item == user:
      list2[i] = user
    else:
      pass
    print(list2)

    
