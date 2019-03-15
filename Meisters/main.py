#!/bin/python3

import re
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
name="default"

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
  global name
  filename=input("What file do you want to save to? ")
  filename=check_txt(filename)
  with open(filename,"w") as f:
    f.write("%s %s %s %s\n"%(px,py,lives,name))
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
        name=t[3]
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
  else:
    error()

# Game Loop

while(True):
  while(lives>0):
    if False:
      # Rooms go here
      pass
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
    lives=3
