from art import help_message, game_over 
from random import randint
from art import hangman_stages, win, start_menu 

def main():
    
    difficulty = start_menu()
    
    if difficulty == 'easy':
        easy()
    elif difficulty == 'normal':
        normal()
    elif difficulty == 'hard':
        hard()
    elif difficulty == 'impossible':
        impossible()
    
words = {
    'easy': ['APPLE', 'BRAIN', 'FLOOR', 'ISSUE', 'MONEY'],
    'normal': ['CREATE', 'CHOICE', 'ADVISE', 'BURDEN', 'CAREER'],
    'hard': ['ACQUIRE', 'BENEATH', 'ATTEMPT', 'FOREIGN', 'JOURNEY'],
    'impossible': ['ABSTRACT', 'APPENDIX', 'DISCOVER', 'DOCTRINE', 'INHERENT']
}

def initial_message():
    print(help_message)
    print("Guess the word!")
    return 0

def get_random_word(difficulty):
    number = randint(0,4)
    word = words[difficulty][number]
    return word

def game_engine(word):
    attempts = 0
    hits = []
    for l in word:
        hits.append('*')
    while attempts <= 6:
        star_word = ''.join(hits)
        if not '*' in star_word:
            print("\033c", end="")
            print(win)
            return 0
        initial_message()
        print(f"{hangman_stages[attempts]}                  ", end='')
        print(''.join(hits))
        user_attempt = input("\n\nGuess a letter:  ").strip().upper()
        if user_attempt in hits:
            continue
        if user_attempt.isalpha() and len(user_attempt) == 1 and user_attempt in word:
                for index, letter in enumerate(word):
                    if user_attempt == letter:
                        hits.pop(index)
                        hits.insert(index, letter)
                    else:
                        pass
                print("\033c", end="")
        else:    
            print("\033c", end="")
            print("You have used one attempt!")
            attempts += 1
    print("\033c", end="")
    print(game_over + hangman_stages[7])
    print(f"The word was '{word}'!")

    
    

def easy():
    word = get_random_word('easy')
    game_engine(word)
    return 0


def normal():
    word = get_random_word('normal')
    game_engine(word)
    return 0
   

    
def hard():
    word = get_random_word('hard')
    game_engine(word)
    return 0



    
def impossible():
    word = get_random_word('impossible')
    game_engine(word)
    return 0


if __name__ == "__main__":
    main()