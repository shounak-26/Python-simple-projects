def diamond_room():
    print("\nYou are now in a room filled with diamonds! \n"
            "And there is a door too!"
            "\n you have to choose the next door. Take some dimanonds and go this is last step..."
            "\n choose the door 1 or 2")
    answer = input(">")

    if answer == "1":
        game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
    elif answer == "2":
        print("\n Well done, There is your princess.")
        play_again()
    else:
        game_over("Go and learn how to type a number.")

def bear_room():
    print("hello You are in bear room"
                           "\n Bear is eating honey. If he sees u u will gone..."
                           "\n you have to choose the next door")

    select=input("||")
    if select == "1":
        game_over("Bear killed you")
    elif select == "2":
        print("\nYour Good time, the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
        game_over("Don't you know how to type something properly?")

def monster_room():
    print("hello You are in monster room"
                             "\n monster is eating sleeping. If he sees u, u will gone..."
                             "\n you have to choose the next door")
    answer = input("||")
    if answer == "1":
        diamond_room()
    elif answer == "2":
        game_over("The monster was hungry, he/it ate you.")
    else:
        game_over("Go and learn how to type a number.")

def play_again():
    print("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        name = input("Enter your name:")
        start(name)
    else:
        exit()

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()

name = input("Enter your name:")
def start(name):
    print("Hey" , name,", Welcome to the kingdom. You have to give the test to save your princess"
                       "\nYou are in the dark room.There are two doors infront of you."
                       "\nSelect te right door if you select wisely you will go to your princess, & if not then..."
                       "\nhaaaa....")

    select = input("||" ).lower()
    if select=="l":
        bear_room()
    elif select=="r":
        monster_room()
    else:
        game_over("Don't you know how to type something properly?")

#Calling the function
start(name)