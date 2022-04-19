import random
#import hangman_word_list
#word_to_guess = random.choice(hangman_word_list.word_list)
from hangman_word_list import word_list
word_to_guess = random.choice(word_list)

print(word_to_guess)
underscore = '_'
guess_word = []
life_chance = 6

for i in range(0,len(word_to_guess)):
  guess_word.insert(i,underscore)
 
print(guess_word)
final_guess = ' '
end_of_game = False
while not (end_of_game):
  letter= input("Enter the letter: ").lower()
  letter_list = []
  
  # approach 1 Use for loop to  search the  position in word_to_Guess where entered letter exist
  #for pos,char in enumerate(word_to_guess):
    #if(char == letter):
      #letter_list.append(pos)   
      #for i in range(0,len(letter_list)):
        #guess_word[pos] = letter   
  #if(len(letter_list) == 0):
    #life_chance -= 1
    #print(f"life_Left1 : {life_chance}")
  

    # approach 2  Loop through the word_to guess and match it wih entered letter value 
  letter_found = " "  
  for i in range(0,len(word_to_guess)):   
    char = word_to_guess[i]
    if(char == letter):
      guess_word[i] = letter  
      letter_found = "Y"
      
  if(letter_found != "Y"):
    life_chance -= 1
    if(life_chance == 0):
      end_of_game = True
    else:
      print(f"life_Left : {life_chance}")

  
  final_guess = ' ' 
  for char in guess_word:
        final_guess += char
  print(f"Final_Guess: {final_guess}")
  
  if underscore not in final_guess:
    end_of_game = True


if(word_to_guess == final_guess):
  print("You won!!!")
elif(life_chance == 0):
  print("Sorry you have to Die :(")
else:
  print("lets continue Playing!")