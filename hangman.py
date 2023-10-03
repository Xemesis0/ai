#importing files
import random
from hangman_art import stages,logo
from hangman_words import word_list
#choosing words at random
chosen_word=random.choice(word_list)


#giving number of chances
lives= len(chosen_word)
print(f'psst,the solution is {chosen_word}.')

#displaying logo
print(logo)
dis=[]
a=[]

#game code
for i in range(len(chosen_word)):
    dis.append("_")

while "_" in dis:
    guess=input("Guess a letter:").lower()
    a.append(guess)
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==guess:
            dis[i]=letter
        elif guess in a:
            print("dont repeat")
            lives=lives+1
            break
    if guess not in chosen_word:
        lives=lives-1
        print("HINT:it is related to anime")

        if lives==0:
            print("ㄚㄖㄩ ㄥㄖ丂乇 🤣🤣🤣")
            exit(1)
    print(f"{''.join(dis)}")
    print(stages[lives])
else:
    print("ɎØɄ ₩Ø₦")
    exit(1)
    
