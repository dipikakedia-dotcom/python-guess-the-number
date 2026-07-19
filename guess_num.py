import random
#for the first round of game
play_again="yes"
#checks condition after the first round based on user input. if "no"
# , skips the entire loops and prints last statement.
while play_again=="yes":

    secret_number= random.randint(1,100)
    attempts=0

    while True:
        i=int(input("Enter a number"))
        attempts+=1
        if i<1 or i>100:
            print ("INVALID NUMBER CHOSEN. KINDLY CHOOSE BETWEEN THE RANGE 1-100 ONLY.")
        elif i<secret_number:
            print("TOO LOW")
        elif i>secret_number:
            print("TOO HIGH")
        elif i==secret_number:
            print("CONGRATULATIONS YOUR GUESS IS CORRECT!")
            print("Number of guesses= ", attempts)
        #giving remarks for number of attempts. 
            if 0<attempts<4:
                print("Excellent")
            elif 3<attempts<6:
                print("Good")
            elif 5<attempts<9:
                print("Nice")
            else:
                print("Keep it Up")
            break
        #play again choice
    play_again=input("Do you want to play again? (yes/no): ").lower()
print("Thanks for Playing!")



