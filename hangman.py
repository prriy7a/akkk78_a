import random,hangman_stages
wordlist=["apple","ant","buffalo","bat","ball","banana","cow","donkey","egg","chikku","balu","giri"]
lives=6
chosen_word=random.choice(wordlist)
# print(chosen_word)
display=[]
for letter in chosen_word:
    display+="_"
# displays=""
# for letter in display:
#     displays+=letter
# print(displays)
print(display)
game_over=False
while not game_over:
    guess=input("Guess a letter").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!")
    if '_' not in display:
        game_over=True
        print("You Win!!")
    print(hangman_stages.stages[lives])