import random
word_bank = ["patna", "paris","toronto","london"]
word_to_guess = random.choice(word_bank)
print(word_to_guess)
letter = '_'
guess_word = []
life_chance = 6

for i in range(0,len(word_to_guess)):
  guess_word.insert(i,letter)
 
print(guess_word)
final_guess = ' '

while not (final_guess == word_to_guess):
  letter= input("Enter the letter: ").lower()
  letter_list = []
  for pos,char in enumerate(word_to_guess):
    if(char == letter):
      letter_list.append(pos)   
      for i in range(0,len(letter_list)):
        #print(f"Letter List : {letter_list}")
        #print(f"Length of Letter_list: {len(letter_list)}")
       
        guess_word[pos] = letter
       # print(f"Guess Word : {guess_word}")

  if(len(letter_list) == 0):
    life_chance -= 1
    print(f"life_Left : {life_chance}")
  
  final_guess = ' ' 
  for char in guess_word:
        final_guess += char
  print(f"Final_Guess: {final_guess}")
  print(f"Word to Guess: {word_to_guess}")


if(word_to_guess == final_guess):
  print("You won!!!")
elif(life_chance == 0):
  print("Sorry you have to Die :(")
else:
  print("lets continue Playing!")