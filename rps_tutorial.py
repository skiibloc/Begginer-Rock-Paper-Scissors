#Rock Paper Scissors
import random

usr_wins=0
cmp_wins=0
usr_tie=0
cmp_tie=0

while True:
    usr_choice=input("Rock, Paper or Scissors or Q to quit: ").lower()
    if usr_choice=="q":
        break
    if usr_choice=="rock":
        print("User chose Rock")
    elif usr_choice=="paper":
        print("User chose Paper")
    elif usr_choice=="scissors":
        print("User chose Scissors")
    else:
        print("Cannot understad please input again")
        continue
    
    cmp_choice=random.randint(1,3)
    if cmp_choice==1:
        print("Computer chose Rock")
    if cmp_choice==2:
        print("Computer chose Paper")
    if cmp_choice==3:
        print("Computer chose Scissors")
    
    if usr_choice=="rock":
        if cmp_choice==1:
            print("Tie")
            usr_tie=usr_tie + 1
            cmp_tie=cmp_tie + 1
        if cmp_choice==2:
            print("Computer Wins")
            cmp_wins=cmp_wins + 1
        if cmp_choice==3:
            print("User Wins")
            usr_wins=usr_wins + 1
    
    if usr_choice=="paper":
        if cmp_choice==1:
            print("User Wins")
            usr_wins=usr_wins + 1
        if cmp_choice==2:
            print("Tie")
            usr_tie=usr_tie + 1
            cmp_tie=cmp_tie + 1
        if cmp_choice==3:
            print("Computer Wins")
            cmp_wins=cmp_wins + 1
    
    if usr_choice=="scissors":
        if cmp_choice==1:
            print("Computer Wins")
            cmp_wins=cmp_wins + 1
        if cmp_choice==2:
            print("User Wins")
            usr_wins=usr_wins + 1
        if cmp_choice==3:
            print("Tie")
            usr_tie=usr_tie + 1

print("Computer Wins", cmp_wins)
print("User Wins", usr_wins)
print("You tied", usr_tie, "times")
if usr_wins>cmp_wins:
    print("User Won")
if usr_wins<cmp_wins:
    print("Computer Won")
if usr_wins==cmp_wins:
    print("This round ended in a tie")
print("Goodbye!")
    

    