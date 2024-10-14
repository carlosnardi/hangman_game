import random

list_words = ["apple","banana","kiwi","strawberry"]
word = random.choice(list_words)
letters = []
for char in word:
  letters.append(char)

num_letters = len(letters)
print(letters)

empty_word = []
for item in range(num_letters):
  empty_word.append("_")
print("".join(empty_word))


def input_letter():
  letter_user = ""
  num_tries = 6
  while num_tries > 0:
    answer = "wrong"
    letter_user = input("Type a letter: ")
    for i, item in enumerate(letters):
      if item == letter_user:
        empty_word[i] = letter_user
        answer = "right"        
    if answer == "wrong":
      num_tries -= 1
    
   # for item in range(num_letters):
     # if em
   
    print(num_tries)
    print("".join(empty_word))
  if num_tries == 0:
    print("Game Over")
    
input_letter()

