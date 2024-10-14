import random

list_words = ["apple","banana","kiwi","strawberry"]
word = random.choice(list_words)

letters = []
for char in word:
  letters.append(char)


num_letters = len(letters)
print(num_letters) 
print(letters)


def input_letter():
  result = []
  letter_user = ""
  word_result = ""
  while letter_user != "exit":
    letter_user = input("Type a letter: ")
    for item in letters:
      if item == letter_user:
        result.append(item)
      else:
        result.append("_")
    for i in result:
      word_result += i
    print(word_result)



def results():
  word_result = ""
  for i in result:
    word_result += i
  print(word_result)

input_letter()
#results()
