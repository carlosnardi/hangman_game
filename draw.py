def error_drawing(number):
  if number == 5:
    print(r"""
  ________
/        |
|        O
|
|
|
| 
  """)

  if number == 4:
    print(r"""
 ________
/        |
|        O
|        |
|
|
|  
  """)

  if number == 3:
    print(r"""
  ________
 /        |
 |        O
 |       /|
 |
 |
 |
  """)

  if number == 2:
    print(r"""
  ________
 /        |
 |        O
 |       /|\
 |
 |
 |
  """)

  if number == 1:
    print(r"""
  ________
 /        |
 |        O
 |       /|\
 |       /
 |
 |
  """)

  if number == 0:
    print(r"""
  ________
 /        |
 |        O
 |       /|\
 |       / \
 |
 |
  """)