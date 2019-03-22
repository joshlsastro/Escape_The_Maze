#!/bin/python3

import time

#Defining Variables

lives_orig=5
lives=lives_orig
maze=[["P",0,0],[0,0,0],[0,0,"E"]]
escaped=0
px=0
py=0
size=3
puzzle=0
x="music"

#Defining Functions

def exists(x):
  """Checks if a string can be converted into a coordinate."""
  global size
  l=[]
  for i in range(0,size):
    l.append(str(i))
  if x in l:
    return True
  else:
    return False

def f(x):
  """Helper function for map."""
  global maze
  global size
  thing=[]
  for n in range(0,size):
    thing.append(maze[n][x])
  print(thing)

def map():
  """Prints a map of the maze."""
  global size
  print("Map:")
  for i in range(0,size):
    f((size-1)-i)

def error():
  """Prints error message."""
  print("That's not an option.")

def go_north():
  """Makes the player go north."""
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
  """Makes the player go east."""
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
  """Makes the player go south."""
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
  """Makes the player go west."""
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
  """Waits three seconds."""
  time.sleep(3)
  
def check_txt(filename):
  """If filename ends with .txt, it returns the filename.
  Otherwise, it appends .txt."""
  if filename.endswith(".txt"):
    return filename
  else:
    return filename+".txt"
  
def save():
  """Saves the game to a file specified by player."""
  global px
  global py
  global lives
  filename=input("What file do you want to save to? ")
  filename=check_txt(filename)
  with open(filename,"w") as f:
    f.write(str(px)+" "+str(py)+" "+str(lives)+"\n")
  with open("main.py","a") as f: #Fixes Trinket Not Saving Files
    f.write("")

def go():
  """Called when player beats a room."""
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
  """Asks standard question and sets x equal to answer."""
  global x
  x=input("Would you like to use your music(\"music\"), the laptop(\"laptop\"), or cheese(\"cheese\")? ")
  x=x.rstrip()
  x=x.lower()
  time.sleep(1)

#Start Screen

print("Welcome to the Meistersinger Consolation Game!")
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
    print("You have your music, a laptop, and cheese.")
    wait()
    break
  elif start.lower()=="save":
    filename=input("What save file do you want to open? ")
    filename=check_txt(filename)
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
  #Easter Eggs
  elif start=="3435":
    print("We are your monkey overlords and we approve this Python code.")
    wait()
    escaped=1
    lives=0
    break
  elif "tour" in start:
    print("Hey, don\'t look back.")
    wait()
    print("Right now, you\'re playing this game and having fun.")
    wait()
    wait()
    print("Hopefully.")
    wait()
  else:
    error()

#Game Loop

while(True):
  while(lives>0):
    if px==0 and py==0:
      if puzzle==0:
        print("You find yourself in a room with locked doors.")
        wait()
        print("A sign states: say the passcode.")
        wait()
        puzzle=1
      ask()
      if x=="music":
        print("You sing one of your songs.")
        wait()
        print("The door doesn\'t open.")
        wait()
        print("You sing all of the songs you know.")
        wait()
        print("The door still doesn\'t open.")
        wait()
      elif x=="laptop":
        print("You build a program to guess the passcode.")
        wait()
        print("The program doesn\'t work.")
        wait()
        print("You punch the door in frustration.")
        wait()
        print("The door opens!")
        wait()
        print("The exit is at the \'E\'.")
        go()
      elif x=="cheese":
        print("You eat some cheese.")
        wait()
        print("Your monkey overlords realize you\'re as bad as Troubadours.")
        wait()
        wait()
        print("Your monkey overlords get some popcorn.")
        wait()
      else:
        error()
    elif px==1 and py==0:
      if puzzle==0:
        print("You find yourself on stage.")
        wait()
        print("You are told that you have to perform.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="music":
          print("You sing the best song you can think of.")
          wait()
          print("Your monkey overlords hate it for some reason.")
          wait()
          wait()
          print("Your monkey overlords get you out of the room in exchange for you not singing for 1 minute.")
          wait()
          wait()
          go()
        elif x=="laptop":
          print("You take out your laptop.")
          wait()
          print("The audience has no idea what\'s going on.")
          wait()
          print("They have a debate over whether you are being rude.")
          wait()
          print("Your monkey overlords get bored.")
          wait()
          print("Your monkey overlords drop a 16-ton weight on you to alleviate boredom.")
          wait()
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("You take out some cheese.")
          wait()
          print("The very hungry audience goes after the cheese.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          error()
    elif (px==0 and py==1) or (px==2 and py==0):
      if puzzle==0:
        print("Your monkey overlords challenge you to a video game match.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="music":
          print("How is music going to beat a game?")
          wait()
        elif x=="laptop":
          print("You try to program the laptop to play for you.")
          wait()
          wait()
          print("The laptop can\'t see the game, so it makes very poor moves.")
          wait()
          wait()
          print("You fail the challenge.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("Your monkey overlords are confused.")
          wait()
          print("Your monkey overlords decide you\'re too dumb to play.")
          wait()
          go()
    elif (px==0 and py==2) or (px==2 and py==1):
      if puzzle==0:
        print("You find yourself in a dark room.")
        wait()
        print("Suddenly, a spotlight turns on directed on you.")
        wait()
        wait()
        print("An announcer says:")
        wait()
        print(" Welcome to Count to 1 Trillion!")
        wait()
        print(" Here, our contestant will count to 1 trillion!")
        wait()
        puzzle=1
      else:
        x=input("Do you want to count(\"count\"), use your music(\"music\"), use the laptop(\"laptop\"), or use cheese(\"cheese\")? ")
        time.sleep(1)
        if x=="count":
          print("You begin to count to 1 trillion.")
          wait()
          wait()
          wait()
          print("The audience gets bored once you reach 162.") #162 was picked randomly
          wait()
          wait()
          print("The announcer lets you leave.")
          go()
        elif x=="music":
          print("You sing the best song you can think of.")
          wait()
          wait()
          print("Your monkey overlords are annoyed.")
          wait()
          print("Your monkey overlords blow up the room.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="laptop":
          print("You take out your laptop.")
          wait()
          print("You send the announcer a funny video.")
          wait()
          print("While the announcer is distracted, you leave.")
          wait()
          go()
        elif x=="cheese":
          print("You take out some cheese.")
          wait()
          print("The announcer says:")
          wait()
          print(" OK, well this was a waste of time.")
          wait()
          print("The announcer opens a trap door below you.")
          wait()
          wait()
          print("You fall into a black hole.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          error()
    elif px==1 and py==1:
      if puzzle==0:
        print("Someone stands in front of the door.")
        wait()
        print("This person won\'t move without coffee.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="music":
          print("The person says:")
          wait()
          print(" I want coffee, not music.")
          wait()
        elif x=="laptop":
          print("You take out your laptop.")
          wait()
          print("You try to connect to the coffee machine.")
          wait()
          print("Error: 418 I'm a teapot") #This is real: https:/google.com/teapot
          wait()
        elif x=="cheese":
          print("The person decides that cheese is good enough.")
          wait()
          wait()
          print("The person leaves.")
          go()
        else:
          error()
    elif px==1 and py==2:
      if puzzle==0:
        print("You hear an announcement.")
        wait()
        print("It states:\"This room will completely fill with water in 10 seconds.\"")
        wait()
        puzzle=1
      else:
        ask()
        if x=="music":
          print("You take out your music.")
          wait()
          print("You use it to jam the water pipe.")
          wait()
          print("You open the door and take your music.")
          go()
        elif x=="laptop":
          print("You open your favorite text editor.")
          wait()
          print("Just then, the room fills with water.")
          wait()
          print("You drown and lose one life.")
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
    elif px==2 and py==2:
      print("Congratulations! You win...")
      wait()
      print("... this cow: ")
      #Generated using cowsay by Tony Munroe
      print(" ________________________________________")
      print("/ 42 is the answer. I don't remember the \\")
      print("\\ question. -Deep Thought(paraphrased)   /")
      print(" ----------------------------------------")
      print("        \\   ^__^")
      print("         \\  (oo)\\_______")
      print("            (__)\\       )\\/\\")
      print("                ||----w |")
      print("                ||     ||")
      print("")
      wait()
      wait()
      print("Thank you for playing.")
      wait()
      lives=0
      escaped=1
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
    maze=[["P",0,0],[0,0,0],[0,0,"E"]]
    px=0
    py=0
    e=0
    p=0
    print("Your monkey overlords have given you 3 lives.")
    wait()
    lives=lives_orig
