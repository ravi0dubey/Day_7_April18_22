import random
word_bank = ["Patna", "Paris","Toronto","London"]
word_to_guess = random.choice(word_bank)
print(word_to_guess)
letter = ' '
guess_word = []

for i in range(0,len(word_to_guess)):
  guess_word.insert(i,letter)
 
print(guess_word)

while(guess_word != word_to_guess):
  letter= input("Enter the letter: ")
  letter_list = []
  for pos,char in enumerate(word_to_guess):
    if(char == letter):
      letter_list.append(pos)   
      for i in range(0,len(letter_list)):
        print(f"Letter List : {letter_list}")
        print(f"Length of Letter_list: {len(letter_list)}")
        print(f'pos: {pos}')
        guess_word.insert(pos,letter)
        print(f"Guess Word : {guess_word}")
