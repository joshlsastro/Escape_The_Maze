#!/bin/python3

import time

#Defining Variables

lives=3
maze=[["P",0,0],[0,0,0],[0,0,'M']]
escaped=0
px=0
py=0
size=3
puzzle=0
e=0
p=0

#Defining Functions

def exists(x):
  global size
  l=[]
  for i in range(0,size):
    l.append(str(i))
  if x in l:
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
  x=input("Would you like to use the laptop(\"laptop\"), the steam engine(\"steam\"), or cheese(\"cheese\")? ")
  x=x.rstrip()
  x=x.lower()
  time.sleep(1)

#Start Screen

print("Welcome to the Escape the Maze Demo.")
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
    print("You have entered a maze of rooms.")
    wait()
    print("It is your task to find the 'M'.")
    wait()
    print("You have a laptop, a steam engine, and cheese.")
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
  else:
    error()

#Game Loop

while(True):
  while(lives>0):
      if px==0 and py==0:
        if puzzle==0:
          print("You find yourself in a room with locked doors.")
          wait()
          print("A machine on the door says: ")
          wait()
          print(" To unlock the doors, you must answer two questions.")
          puzzle=1
        elif puzzle==1:
          wait()
          x=input(" What is the brightest star (besides the Sun)? ")
          x=x.lower()
          if x=="sirius" or x=="sirius a":
            print(" Correct!")
            wait()
            print(" As for the second question,")
            wait()
            x=input(" Is the answer to this question 'no'?")
            wait()
            print(" WRONG!")
            wait()
            print(" The doors will remain locked.")
            wait()
            puzzle=2
          elif x=="r136a1":
            print("Programmer: Wait, what?")
            wait()
            print("How did you know that?")
            wait()
            x=input("Did you look at the source code or did you just know that? ")
            print("It doesn't matter, either way it's impressive.")
            wait()
            wait()
            print("As a reward, you get an extra chance.")
            lives+=1
            go()
          else:
            print(" WRONG!")
            wait()
            print(" The doors will remain locked.")
            wait()
            puzzle=2
        elif puzzle==2:
          ask()
          if x=="laptop":
            print("You bash the laptop against the door.")
            wait()
            print("It's not very effective.")
            wait()
          elif x=="steam":
            print("You use the steam engine to force the door open.")
            wait()
            go()
          elif x=="cheese":
            print("Why?")
            wait()
            wait()
          else:
            error()
      elif (px==1 and py==0) or (px==0 and py==2):
        if puzzle==0:
          print("You see a bunch of geese.")
          wait()
          print("It appears that they are attempting to overthrow humans.")
          wait()
          wait()
          puzzle=1
        elif puzzle==1:
          ask()
          if x=="laptop":
            print("You attempt to program the geese to fly away.")
            wait()
            print("The program fails and you are thrown in goose prison.")
            wait()
            print("You lose one chance.")
            lives=lives-1
          elif x=="steam":
            print("You use your steam engine to blow the geese away.")
            go()
          elif x=="cheese":
            print("You attempt to feed the geese cheese.")
            wait()
            print("The geese are not satisfied and throw you in goose prison.")
            wait()
            print("You lose one chance.")
            lives=lives-1
          else:
            error()
      elif px==1 and py==2:
        if puzzle==0:
          print("You fall onto a raft in a small lake.")
          wait()
          print("A note states that you need to drain the lake to get to the door.")
          wait()
          puzzle=1
        elif puzzle==1:
          ask()
          if x=="laptop":
            print("ERROR: Cannot drain lake.")
            wait()
          elif x=="steam":
            print("You use the steam engine to pump the water out of the lake.")
            wait()
            go()
          elif x=="cheese":
            print("You throw cheese into the lake.")
            wait()
            print("Luckily, it absorbs all of the water.")
            wait()
            go()
          else:
            error()
      elif px==1 and py==1:
        if puzzle==0:
          print("You see an angry monster.")
          wait()
          puzzle=1
        elif puzzle==1:
          ask()
          if x=="laptop":
            print("The monster sees you playing fun games.")
            wait()
            print("The jealous monster steals your laptop.")
            wait()
            print("You get it back in exchange for losing a chance.")
            wait()
            wait()
            lives=lives-1
          elif x=="steam":
            print("You push the monster out of the way.")
            wait()
            go()
          elif x=="cheese":
            print("The monster is confused.")
            wait()
            print("The monster locks you in.")
            wait()
            print("You lose one chance.")
            wait()
            lives=lives-1
          else:
            error()
      elif (px==2 and py==0) or (px==0 and py==1):
        if puzzle==0:
          print("You find a note.")
          wait()
          print("The note states:")
          wait()
          print(" There is a tunnel to something interesting right here. -Anonymous")
          wait()
          puzzle=1
        elif puzzle==1:
          x=input("Do you go into the tunnel? ")
          x=x.lower()
          if x=="y" or x=="yes":
            print('You find a button with the word "frustrate" on it.')
            wait()
            x=input('To push the button, type "push"')
            puzzle=2
          elif x=="n" or x=="no":
            go()
          else:
            error()
        elif puzzle==2:
          times=0
          while True:
            sayings={0:"Nothing happens. Type 'push' to try again.",
              1:"Still nothing happens. Type 'push' to try again.",
              2:"You get the picture.",
              3:"You realize why 'frustrate' is on the button and don't type 'push' again.",
              4:"You realize why 'frustrate' is on the button and don't type 'push' again.",
              5:"You realize why 'frustrate' is on the button and don't type 'push' again.",
              6:"Sigh. You clearly are not frustrated easily. You foolishly persist in pushing the button.",
              7:"You are so foolish that you do not realize that you're a fool.",
              8:"The dictionary is rewritten. The definition of 'idiot' is now you.",
              9:"I've got nothing to say.",
              10:"Look, I won't sustain this forever. Push that button again and it's game over.",
              11:"I mean it. Push that button again and the game ends. If you want to continue, type anything other than push."
            }
            x=input(sayings[times]+" ")
            if x!="push":
              break
            times+=1
            if times>11:
              print("GAME OVER.")
              while True:
                pass
          print("You don't push the button.")
          go()
      elif px==2 and py==1:
        if puzzle==0:
          print("You see a robot about to push a button.")
          wait()
          print("The button says: \"remove a chance\".")
          wait()
          puzzle=1
        elif puzzle==1:
          ask()
          if x=="laptop":
            print("You program the robot not to push the button.")
            go()
          elif x=="steam":
            print("You successfully push the robot away.")
            go()
          elif x=="cheese":
            print("The robot is confused.")
            wait()
            print("Believing you unworthy of passing through the maze, it pushes the button.")
            wait()
            wait()
            lives=lives-1
          else:
            error()
      elif px==2 and py==2:
        print("Congratulations! You obtained the (useless) 'M'!")
        wait()
        wait()
        print("You win!")
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
  elif escaped==2:
    break
  else:
    print("You ran out of chances.")
    wait()
    print("You are placed in the start of the maze.")
    wait()
    maze=[["P",0,0],[0,0,0],[0,0,'M']]
    px=0
    py=0
    e=0
    p=0
    print("You get 3 chances to try again.")
    wait()
    lives=3
    puzzle=0
