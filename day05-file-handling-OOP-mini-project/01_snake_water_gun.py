import random

player_1 = random.choice([-1,0,1])

youstr = input("Enter your Choice: ")


you_dict = {"s" : 1, "w" : -1, "g" : 0}

reverse_dict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = you_dict[youstr]


print(f"You chose {reverse_dict[you]}\nComputer chose {reverse_dict[player_1]}")

if player_1 == you:
    print("It's a Draw!")

else: 
    if(player_1 == -1 and you == 1):
        print("You Win!")
    elif(player_1 == -1 and you == 0):
        print("You Lose!")
    elif(player_1 == 0 and you == 1):
        print("You Win!")
    elif(player_1 == 0 and you == -1):
        print("You Lose!")
    elif(player_1 == 1 and you == 0):
        print("You Win!")
    elif(player_1 == 1 and you == -1):
        print("You Lose!")
    else:
        print("Something went wrong!")


    
    
    


