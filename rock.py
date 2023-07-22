import random
print("\nLet's start the game!")
u = input("Enter a choice of yours(rock, paper, scissors): ") # for user to choose
p = ["rock", "paper", "scissors"]
c = random.choice(p) # for computer to choose
while True:
    print(f"\nYou have chosen {u} and computer have chose {c}.")
    if u == c:
       print(f"Both of the players selected {u}. So it is a tie!")
    elif u == "rock" and c=="scissors":
        print("rock smashes scissors! You win!")
    elif u=="rock" and c=="paper":
        print("paper covers rock! You lose.")
    elif u == "paper" and c=="rock":
        print("paper covers rock! You win!")
    elif u=="paper" and c=="scissors":
        print("scissors cuts paper! You lose.")
    elif u== "scissors" and c=="paper":
        print("scissors cuts paper! You win!")
    elif u=="scissors" and c=="rock":
        print("rock smashes scissors! You lose.")
    else: 
       print("Invalid input! choose between rock, paper and scissors only ")
    # to play the game again
    a=input("\nWant to play again yes or no? : ")
    if a=="no":
       break
    elif a=="yes":
        print("\nLet's play again!")
        u = input("\nEnter a choice of yours(rock, paper, scissors): ")
        p = ["rock", "paper", "scissors"]
        c = random.choice(p)
        True
    else:
       print("Invalid input! Choose yes or no only")
       break
       
       

