import random

list_words = ["apple","banana","kiwi","strawberry"]
word = random.choice(list_words)
letters = []
for char in word:
  letters.append(char)

num_letters = len(letters)
print(num_letters) 
print(letters)

empty_word = []
for item in range(num_letters):
  empty_word.append("_")
print("".join(empty_word))


def input_letter():
  letter_user = ""
  word_result = ""
  while letter_user != "exit":
    letter_user = input("Type a letter: ")
    for i, item in enumerate(letters):
      if item == letter_user:
        empty_word[i] = letter_user
    #for item in empty_word:
      #word_result += item
    #print(word_result)
    print(empty_word)

input_letter()

