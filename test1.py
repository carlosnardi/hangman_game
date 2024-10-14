import random

list_words = ["apple","banana","kiwi","strawberry"]

word = random.choice(list_words)

num_letters = len(word)

print(num_letters)

letters = ""
for item in range(num_letters):
  letter = "_"
  letters += letter
  
print(letters)



