import random

def choose():
    words = [
        "Apple", "Bicycle", "Candle", "Dragon", "Elephant", "Forest", "Galaxy", "Harmony", "Island", "Jungle",
        "Kite", "Lantern", "Mountain", "Notebook", "Ocean", "Penguin", "Quicksand"
    ]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled_word = ''.join(random.sample(word, len(word)))
    return jumbled_word

def thank(p1name, p2name, point_p1, point_p2):
    print(f"\nThank you, {p1name} and {p2name}, for playing!")
    score_summary = f"Your Scores are:\n{p1name}: {point_p1}\n{p2name}: {point_p2}"
    return score_summary

def play():
    p1name = input("Enter Name for Player 1: ")
    p2name = input("Enter Name for Player 2: ")
    point_p1 = 0
    point_p2 = 0
    turn = 1
    
    while True:
        picked_word = choose()
        qn = jumble(picked_word)
        print("\nJumbled word:", qn)
        
        # Player 1's turn
        if turn % 2 != 0:
            print(f"{p1name}, it's your turn.")
            ans = input("What's in your mind? ")
            if ans.lower() == picked_word.lower():
                print("Wow, you guessed it correctly!")
                point_p1 += 1
                print(f"Your Score is {point_p1}")
            else:
                print(f"Oops! The correct word was {picked_word}.")
                
        # Player 2's turn
        else:
            print(f"{p2name}, it's your turn.")
            ans = input("What's in your mind? ")
            if ans.lower() == picked_word.lower():
                print("Wow, you guessed it correctly!")
                point_p2 += 1
                print(f"Your Score is {point_p2}")
            else:
                print(f"Oops! The correct word was {picked_word}.")
        
        # Continue or quit
        c = int(input("Press 1 to continue and 0 to quit: "))
        if c == 0:
            print(thank(p1name, p2name, point_p1, point_p2))
            break
        
        turn += 1

play()
