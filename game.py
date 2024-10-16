import random
import draw

list_words = ["apple","banana","kiwi","strawberry"]
word = random.choice(list_words)
letters = []
for char in word:
  letters.append(char)

num_letters = len(letters)
# while testing:
# print(letters)

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
      draw.error_drawing(num_tries)
  
    word_completed = True
    for item in empty_word:
      if item == "_":
        word_completed = False
    if word_completed:
      print("".join(empty_word))
      print("\n Congratulations!!!")
      break
   
    # print(num_tries)
    print("".join(empty_word))
  if num_tries == 0:
    print("\n Game Over")
    
input_letter()

