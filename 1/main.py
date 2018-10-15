#!/bin/python3

import time

#Defining Variables

lives=3
maze=[["P",0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,'E']]
escaped=0
px=0
py=0
size=5
puzzle=0
e=0
p=0

#Defining Functions

def exists(x):
    global size
    list=[]
    for i in range(0,size):
        list.append(str(i))
    if x in list:
        return True
    else:
        return False

def f(x):
    global maze
    global size
    thing=[]
    for n in range(0,size):
        thing.append(maze[n][x])
    print(thing)

def map():
    global size
    print("Map:")
    for i in range(0,size):
        f((size-1)-i)

def error():
    print("That's not an option.")

def go_north():
    global size
    global maze
    global px
    global py
    if py+1>size-1:
        print("You bump into a wall.")
    else:
        maze[px][py]=0
        maze[px][py+1]="P"
        py = py+1

def go_east():
    global size
    global maze
    global px
    global py
    if px+1>size-1:
        print("You bump into a wall.")
    else:
        maze[px][py]=0
        maze[px+1][py]="P"
        px=px+1

def go_south():
    global maze
    global px
    global py
    if py-1<0:
        print("You bump into a wall.")
    else:
        maze[px][py]=0
        maze[px][py-1]="P"
        py=py-1

def go_west():
    global maze
    global px
    global py
    if px-1<0:
        print("You bump into a wall.")
    else:
        maze[px][py]=0
        maze[px-1][py]="P"
        px=px-1

def wait():
    time.sleep(3)

def save():
    global px
    global py
    global lives
    filename=input("What file do you want to save to? ")
    with open(filename,"w") as f:
        f.write(str(px)+" "+str(py)+" "+str(lives)+"\n")
    with open("main.py","a") as f: #Fixes Trinket Not Saving Files
        f.write("")

def go():
    global puzzle
    global px
    global py
    px_cur=px
    py_cur=py
    while(px_cur==px and py_cur==py):
        wait()
        map()
        wait()
        print("You may go north(\"n\"), east(\"e\"), south(\"s\"), or west(\"w\").")
        wait()
        print("You can also type \"save\" to save the game.")
        direct=input("Where do you want to go? ")
        direct=direct.rstrip()
        direct=direct.lower()
        if direct=="n":
            go_north()
        elif direct=="e":
            go_east()
        elif direct=="s":
            go_south()
        elif direct=="w":
            go_west()
        elif direct=="save":
            save()
            exit()
        else:
            error()
    wait()
    map()
    wait()
    puzzle=0

def ask():
    global x
    x=input("Would you like to use graphene(\"graphene\"), the toothbrush(\"toothbrush\"), or cheese(\"cheese\")? ")
    x=x.rstrip()
    x=x.lower()
    time.sleep(1)

#Start Screen

print("Welcome to Escape the Maze.")
wait()
print("Bum, bum, bum!")
wait()
while(True):
    px=0
    py=0
    print("If you want to start a new game, type \"new\".")
    print("If you want to start a saved game, type \"save\".")
    print("If you want to leave the game, type \"exit\".")
    start=input(" ")
    start=start.rstrip()
    if start.lower()=="new":
        print("You have been abducted by evil monkeys.")
        wait()
        print("They have placed you inside a maze of rooms.")
        wait()
        print("It is your task to escape.")
        wait()
        print("You have super-strong graphene, a toothbrush, and cheese.")
        wait()
        break
    elif start.lower()=="save":
        filename=input("What save file do you want to open? ")
        try:
            with open(filename,"r") as m:
                t=m.read()
            t=t.split()
            px=t[0]
            py=t[1]
            if exists(px) and exists(py):
                px,py=int(px),int(py)
                lives=int(t[2])
                maze[0][0]=0
                maze[px][py]="P"
                go()
                break
            else:
                print("Bad save file.")
        except IndexError:
            print("Bad save file.")
        except ValueError:
            print("Bad save file.")
        except IOError:
            print("Not a real file.")
    elif start.lower()=="exit":
        exit()
    elif start=="3435":
        print("We are your monkey overlords and we approve this Python code.")
        wait()
        escaped=1
        lives=0
        break
    else:
        error()


#Game Loop

while(True):
    while(lives>0):
        if px==0 and py==0:
            print("You find yourself in a dark room.")
            wait()
            leave=input("Do you want to leave(if you do, say \"yes\")? ")
            leave=leave.rstrip()
            if leave.lower()=="yes":
                go()
            else:
                print("Your monkey overlords get bored by the experiment.")
                wait()
                print("Your monkey overlords replace the air with bananas.")
                wait()
                lives=0
        elif px==1 and py==0:
            if puzzle==0:
                print("You find that none of the doors have knobs.")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("It's only one atom thick. It makes a terrible doorknob.")
                    wait()
                    wait()
                elif x=="cheese":
                    print("What are you thinking?")
                    wait()
                elif x=="toothbrush":
                    print("It works!")
                    go()
                else:
                    error()
        elif px==0 and py==1:
            if puzzle==0:
                print("You look up.")
                wait()
                print("You find that the roof is about to collapse.")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("The roof doesn\'t collapse thanks to your brilliance.")
                    wait()
                    go()
                else:
                    print("The roof collapses.")
                    wait()
                    print("Your monkey overlords restore the roof, but not you.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
        elif (px==2 and py==0) or (px==1 and py==1) or (px==0 and py==2):
            print("You find a note.")
            wait()
            print("It states:")
            wait()
            print(" We are your monkey overlords.")
            wait()
            print(" The ethics monkey requires us to state that the \'E\' on your map stands for exit.")
            wait()
            wait()
            wait()
            print(" But that doesn\'t prevent us from trying to stop you!")
            wait()
            print(" [insert evil laugh]")
            go()
        elif px==3 and py==0:
            if puzzle==0:
                print("You hear an announcement.")
                wait()
                print("It states:\"This room will completely fill with water in 10 seconds.\"")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("The room fills with water, but your graphene spacesuit protects you.")
                    go()
                elif x=="toothbrush":
                    print("The room fills with water, and thanks to your toothbrush, your teeth are clean.")
                    wait()
                    wait()
                    print("Unfortunately, you die from asphyxiation.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                elif x=="cheese":
                    print("The room fills with water, and the cheese absorbs it.")
                    wait()
                    print("Unfortunately, you cannot sleep due to nightmares of the cheese absorbing YOU.")
                    wait()
                    wait()
                    print("Without sleep, you beg to die.")
                    wait()
                    print("This wish is immediately granted by your monkey overlords.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                else:
                    error()
        elif (px==0 and py==3) or (px==3 and py==1):
            if puzzle==0:
                print("You hear an angry monster.")
                wait()
                print("You see a poster saying: \"No cheese\"")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("You put on graphene armor.")
                    wait()
                    print("The monster tries to hurt you and fails.")
                    wait()
                    print("The monster faints from exhaustion.")
                    go()
                elif x=="cheese":
                    print("You throw your cheese on the ground.")
                    wait()
                    print("The monster has a severe cheese allergy and rests to deal with its hives.")
                    go()
                elif x=="toothbrush":
                    print("You take out your toothbrush.")
                    wait()
                    print("The monster takes the toothbrush and brushes its teeth with it.")
                    wait()
                    wait()
                    print("You leap into the mouth to take your toothbrush back.")
                    wait()
                    wait()
                    print("The monster eats you.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                else:
                    error()
        elif px==2 and py==1:
            if puzzle==0:
                print("The doors are locked.")
                wait()
                print("You find a note on the floor.")
                wait()
                print("It states: \"Your monkey overlords want something sweet. -Person who escaped maze\"")
                wait()
                wait()
                puzzle=1
            else:
                ask()
                if x=="cheese":
                    print("Your monkey overlords like the cheese you gave them.")
                    wait()
                    wait()
                    print("Your monkey overlords unlock the doors.")
                    go()
                elif x=="graphene" or x=="toothbrush":
                    print("Your monkey overlords\' teeth break.")
                    wait()
                    print("Your monkey overlords are angry with you.")
                    wait()
                    print("Your monkey overlords leave the doors locked forever.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                else:
                    print("You don\'t have that.")
        elif (px==4 and py==0) or (px==0 and py==4):
            if puzzle==0:
                print("You find a hole.")
                wait()
                print("A note by it states it was dug by the person who escaped.")
                wait()
                wait()
                j=input("Do you want to leave(if so, say \"yes\")? ")
                j=j.rstrip()
                if j.lower()=="yes":
                    wait()
                    print("You go through the hole.")
                    wait()
                    print("Your monkey overlords teleport you back inside.")
                else:
                    pass
                go()
        elif px==1 and (py==3 or py==4):
            if puzzle==0:
                print("You see a robot trying to divide by 0 on a calculator.")
                wait()
                wait()
                print("This calculator controls the maze.")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("You put the graphene on the calculator.")
                    wait()
                    print("Since graphene is flexible, the robot\'s arm pushes 1/0.")
                    wait()
                    print("The maze blows up.")
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                elif x=="toothbrush":
                    print("You punch out an extra one.")
                    wait()
                    print("The calculator calculates 1/10.")
                    go()
                elif x=="cheese":
                    print("OK.")
                    wait()
                    print("Now what?")
                    wait()
                else:
                    error()
        elif px==4 and py==1:
            if puzzle==0:
                print("The doors are locked.")
                wait()
                print("You see a computer.")
                wait()
                puzzle=1
            else:
                x=input("The computer says: grammar on(\"yes\" or \"no\")? ")
                x=x.rstrip()
                if x.lower()=="yes":
                    print("The computer says: I failed English, malfunctioning.")
                    wait()
                    print("The doors unlock.")
                    go()
                elif x.lower()=="no":
                    print("Your an well person. Thank me.")
                    wait()
                    print("Me love cantalope. Cantalope are great.")
                    wait()
                    print("Wait. Computers can\'t eat.")
                    wait()
                    print("You calculate whether computers can eat.")
                    wait()
                    print("You no math. Me math. Malfunctioning.")
                    wait()
                    print("The doors unlock.")
                    go()
                else:
                    error()
        elif px==2 and py==2:
            if puzzle==0:
                print("You find yourself in a forest.")
                wait()
                print("Your monkey overlords say you\'re in the Cambrian.")
                wait()
                print("You see a T. rex.")
                wait()
                ask()
                print("Before you can use your things, the T. rex goes after you.")
                wait()
                wait()
                puzzle=1
            else:
                c=input("Do you run(\"yes\" or \"no\")? ")
                c=c.rstrip()
                wait()
                if c.lower()=="yes":
                    print("You run. The T. rex outruns you and stomps on you.")
                    wait()
                    wait()
                    print("You lose one life.")
                    wait()
                    lives=lives-1
                elif c.lower()=="no":
                    print("You quickly realize that dinosaurs did not exist in the Cambrian.")
                    wait()
                    wait()
                    print("Your monkey overlords end the simulation.")
                    go()
                else:
                    error()
        elif (px==1 and py==2) or (px==2 and py==3):
            if puzzle==0:
                print("You see zombie-looking people walking through the door.")
                wait()
                print("They say they are vegetarians.")
                wait()
                print("They also have horrible breath.")
                wait()
                puzzle=1
            else:
                ask()
                if x=="graphene":
                    print("You use graphene to hit the zombie-looking people out of the way.")
                    wait()
                    go()
                elif x=="toothbrush":
                    print("The zombie-looking people use your toothbrush to clean their teeth.")
                    wait()
                    wait()
                    print("They give your toothbrush back and let you out.")
                    wait()
                    print("Why don\'t they bite you? Simple, they want \"grains\", not \"brains\".")
                    wait()
                    wait()
                    print("Remember, they\'re vegetarians.")
                    go()
                elif x=="cheese":
                    print("The zombie-looking people are confused.")
                    wait()
                    print("They refuse to let you out the door without an explanation.")
                    wait()
                    wait()
                    print("Without an explanation, you lose one life.")
                    wait()
                    lives=lives-1
                else:
                    error()
        elif px==3 and py==2:
            if puzzle==0:
                print("You see a machine that says: \"to brainwash, use cheese\"")
                wait()
                puzzle=1
            else:
                ask()
                if x=="cheese":
                    print("You used cheese.")
                    wait()
                    print("You lose all of your memories.")
                    wait()
                    print("You serve your monkey overlords for eternity.")
                    wait()
                    print("Game Over.")
                    wait()
                    print("For a second chance, click the stop button/time machine.")
                    while True:
                        pass
                else:
                    print("Your monkey overlords realize you\'re smarter than you look.")
                    wait()
                    wait()
                    print("Your monkey overlords ask: \"Is the answer to this question \"no\"?\"")
                    x=input("Answer \"yes\" or \"no\". ")
                    wait()
                    print("Realizing how dumb you are, your monkey overlords continue as before.")
                    wait()
                    go()
        elif (px==2 and py==4) or (px==3 and py==3) or (px==4 and py==2):
                print("You hear a happy monster.")
                wait()
                print("The monster warns you:")
                wait()
                print(" There are horrible, horrible monsters ahead.")
                wait()
                print(" There is a button that will eject the monsters.")
                wait()
                wait()
                wait()
                print(" The button is my favorite color...is that a fire hydrant?")
                wait()
                print(" Fire hydrants are really interesting. In fact...")
                wait()
                print("You fall asleep out of boredom. When you wake up, the monster is gone.")
                wait()
                e=0
                p=0
                go()
        elif (px==3 and py==4) or (px==4 and py==3):
            if puzzle==0:
                print("You see a very large, very angry monster.")
                wait()
                puzzle=1
            else:
                if e==0:
                    ask()
                    if x=="graphene":
                        print("You put on graphene armor and avoid being immediately crushed.")
                        wait()
                        wait()
                        e=1
                    elif x=="toothbrush" or x=="cheese":
                        print("You are immediately crushed by the monster.")
                        wait()
                        print("You lose one life.")
                        wait()
                        lives=lives-1
                    else:
                        error()
                elif p==0:
                    print("You see three buttons on the wall.")
                    wait()
                    print("One is red, one is green, and one is ultraviolet.")
                    wait()
                    wait()
                    wait()
                    p=1
                else:
                    x=input("Which button do you push(\"red\", \"green\", or \"ultraviolet\")? ")
                    x=x.rstrip()
                    x=x.lower()
                    wait()
                    if x=="red":
                        print("The monster is ejected.")
                        wait()
                        print("You wonder for a moment why your monkey overlords even included a monster eject button.")
                        wait()
                        wait()
                        wait()
                        go()
                    elif x=="green":
                        print("The monster\'s DVD player ejects a DVD.")
                        wait()
                        print("The monster is enraged.")
                        wait()
                        print("The monster pushes the ultraviolet button.")
                        wait()
                        print("Your favorite movie turns on.")
                        wait()
                        print("While you are distracted, the monster takes off your graphene armor.")
                        wait()
                        wait()
                        print("The monster eats you.")
                        wait()
                        print("You lose one life.")
                        wait()
                        lives=lives-1
                    elif x=="ultraviolet":
                        print("Your favorite movie turns on.")
                        wait()
                        print("While you are distracted, the monster takes off your graphene armor.")
                        wait()
                        wait()
                        print("The monster eats you.")
                        wait()
                        print("You lose one life.")
                        wait()
                        lives=lives-1
                    else:
                        error()
        elif px==4 and py==4:
            print("Congratulations! You Win...")
            wait()
            print("Absolutely nothing.")
            wait()
            print("Thank you for playing.")
            wait()
            escaped=1
            lives=0
        else:
            print("No content.")
            go()
    if escaped==1:
        print("If you want to restart the game, click the arrow at the top.")
        break
    else:
        print("You ran out of lives.")
        wait()
        print("Your monkey overlords are placing you in the start of the maze.")
        wait()
        maze=[["P",0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,'E']]
        px=0
        py=0
        e=0
        p=0
        print("Your monkey overlords have given you 3 lives.")
        wait()
        lives=3

