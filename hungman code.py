import random
from hangman_words import word_list
from hangman_art import stages,logo
chosen_word =random.choice(word_list)
lives=6
print(lives)
print(f'pssst, the  solution is {chosen_word}.')
print(logo)
display=[]


for i in range(len(chosen_word)):
    display.append("_")
while "_" in display:
    guess=input("Guess a letter:").lower()
    print(guess)
    a=list(guess)
    for i in range (len(chosen_word)):
        letter =chosen_word[i]
        if letter== guess:
            display[i]=letter
    if  guess not in chosen_word :
        lives=lives-1
   
        if lives == 0:
            print("you losse")
            print(stages[lives])
            exit(1)
    print(f"{' '.join(display)}")
    print(stages[lives])
else:
    print("you have won")
