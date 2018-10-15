#!/bin/python3

import re
import time

#Defining Variables

lives_orig=5
lives=lives_orig
maze=[["P",0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,'E']]
escaped=0
px=0
py=0
size=6
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
  x=input("Would you like to use graphene(\"graphene\"), the toothbrush(\"toothbrush\"), or cheese(\"cheese\")? ")
  x=x.rstrip()
  x=x.lower()
  time.sleep(1)


#Start Screen

print("Welcome to Escape the Maze 2.")
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
  elif start.lower()=="xyzzy":
    print("Nothing happens.")
    wait()
  elif start.lower()=="moo":
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
      if puzzle==0:
        print("You find a computer.")
        wait()
        name=input("It asks: What is your name(no spaces)? ")
        name=name.rstrip()
        wait()
        #Checking name
        regex="\\s"
        target=re.compile(regex)
        mo=target.search(name)
        if mo or name=="":
          print("Invalid name.")
          wait()
        else:
          puzzle=1
      else:
        print("The computer prints a note.")
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
        print("It states: \"This room will completely fill with water in 10 seconds.\"")
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
    elif (px==0 and py==3):
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
    elif px==3 and py==1:
      if puzzle==0:
        print("You hear an announcement.")
        wait()
        print("It states: \"A black hole will enter this room in 1 minute.\"")
        wait()
        print("You note the computer on the wall.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="graphene":
          print("You try to use the graphene to shield yourself.")
          wait()
          wait()
          print("Unfortunately, it doesn't save you from the black hole's gravity.")
          wait()
          print("You are spaghettified and lose one life.")
          wait()
          lives=lives-1
        elif x=="toothbrush":
          print("You use the toothbrush to type calculations on the wall computer.")
          wait()
          wait()
          print("You calculate a way to escape.")
          go()
        elif x=="cheese":
          print("Using the computer on the wall, you find out that you will likely be spaghettified.")
          wait()
          wait()
          print("As a result, you use cheese in hope of a good meal.")
          wait()
          wait()
          print("You are spaghettified and lose one life.")
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
    elif (px==4 and py==0):
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
    elif px==0 and py==4:
      if puzzle==0:
        print("You find yourself trapped in a box.")
        wait()
        print("There is an electronic door.")
        wait()
        print("You try to open it when it starts talking.")
        wait()
        print("The door says:")
        wait()
        print(" I am a door. I am in a program written by Josh.")
        wait()
        print(" If you want to escape, you must answer two questions.")
        wait()
        x=input("Do you accept the door's challenge(if so, say \"yes\")? ")
        x=x.rstrip()
        x=x.lower()
        if x=="yes":
          puzzle=1
        else:
          print("You never leave the box.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
      elif puzzle==1:
        print("The door says:")
        wait()
        print(" OK, here we go!")
        wait()
        print(" Question 1:")
        wait()
        print("  You own 3 animals, a wild animal, a tamed animal, and a bored reptile.")
        wait()
        print("  You take the animals to the zoo to see their animal friends.")
        wait()
        print("  They buy 9 equal stacks of notebooks, each costing $50.")
        wait()
        wait()
        print("  Those are the facts, now:")
        wait()
        print("\n" * 100)
        wait()
        x=input(" How many times did I just say the word \"animal\"(not counting this question)? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x in ["3", "three"]:
          print(" Correct!")
          wait()
          puzzle=2
        else:
          print(" Wrong! Challenge over!")
          wait()
          puzzle=0
      else:
        print(" Question 2(involves math):")
        wait()
        print("  A train leaves Denver at 8:00 AM going at 30 m/s.")
        wait()
        print(" Given that 1 AU is 149597870.7 km, here is the question:")
        wait()
        x=input(" Who programmed this game, %s(\"%s\"), Josh(\"josh\"), or Mr. Boring(\"boring\")? "%(name,name.lower()))
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="josh":
          print(" Correct! You may go!")
          go()
        else:
          print(" Wrong! Challenge rejected!")
          wait()
          puzzle=0
    elif px==1 and py==3:
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
    elif px==1 and py==4:
      if puzzle==0:
        print("You enter a room with a thunderstorm in it.")
        wait()
        print("A gust of wind blows away your stuff.")
        wait()
        puzzle=1
      elif puzzle==1:
        x=input("Do you run after the stuff(\"run\") or wait for the storm to pass(\"wait\")? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="run":
          print("You run after your stuff.")
          wait()
          print("You trip over your stuff and hit a self-destruct button.")
          wait()
          print("The room explodes.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="wait":
          print("You wait for the storm to pass.")
          time.sleep(20)
          print("After what feels like an eternity, the storm does not clear.")
          wait()
          wait()
          puzzle=2
        else:
          error()
      elif puzzle==2:
        x=input("Do you yell at your monkey overlords(\"curse\") or use a conveniently placed radar(\"deus\")? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="curse":
          print("You attempt to curse at your monkey overlords.")
          wait()
          print("Just then, you are struck by lightning and lose one life.")
          wait()
          wait()
          lives=lives-1
        elif x=="deus":
          print("Using the radar, you locate your things.")
          wait()
          print("Luckily, the doors are unlocked.")
          go()
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
    elif (px==1 and py==2):
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
    elif px==2 and py==3:
      if puzzle==0:
        print("You see a giant alien spaceship.")
        wait()
        puzzle=1
      else:
        x=input("Do you fight, talk, or flee(type as written)? ")
        x=x.rstrip()
        x=x.lower()
        time.sleep(1)
        if x=="fight":
          print("You punch an alien as hard as you can.")
          wait()
          print("Damage to Alien: 1 unit.") #Units of what? I'll never tell
          wait()
          print("The alien punches you back!")
          wait()
          print("Damage to You: A lot.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="talk":
          print("You greet the aliens.")
          wait()
          print("The aliens say hello.")
          wait()
          print("They tell you how long they\'ve been in the maze.")
          wait()
          print("They borrow your stuff and defeat your monkey overlords.")
          wait()
          wait()
          print("The aliens escape, but your monkey overlords quickly wake up.")
          wait()
          wait()
          print("Your monkey overlords teleport you back into the maze.")
          wait()
          wait()
          print("Thankfully, the doors are open.")
          go()
        elif x=="flee":
          print("You run away.")
          wait()
          print("You get a confused glance from the aliens before leaving.")
          wait()
          go()
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
          print("Your monkey overlords ask: \"Is the answer to this question \'no\'?\"")
          x=input("Answer \"yes\" or \"no\". ")
          wait()
          print("Realizing how dumb you are, your monkey overlords continue as before.")
          wait()
          go()
    elif px==2 and py==4:
      if puzzle==0:
        print("You fall through a trap door.")
        wait()
        print("You are trapped in a cage.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="graphene":
          print("It\'s not the answer to everything, you know.")
          wait()
          wait()
          wait()
        elif x=="toothbrush":
          print("You use your toothbrush to pick the lock and escape.")
          wait()
          wait()
          go()
        elif x=="cheese":
          print("You use cheese to lure over a rat.")
          wait()
          print("The rat picks the lock and you escape.")
          wait()
          go()
        else:
          error()
    elif px==3 and py==4:
      print("You see a phone with the number of HELP on it.")
      wait()
      wait()
      x=input("Do you call it(\"yes\" or \"no\")? ")
      x=x.rstrip()
      x=x.lower()
      time.sleep(1)
      if x=="yes":
        print("You call the number.")
        wait()
        print("The answering machine says:")
        wait()
        print(" Thank you for calling H.E.L.P.")
        wait()
        print(" Our agents will soon arrive and disintigrate you.")
        wait()
        wait()
        print("You are disintigrated and lose one life.")
        wait()
        lives=lives-1
      elif x=="no":
        print("You decide not to call Horrible Evil Lying People.")
        wait()
        go()
      else:
        error()
    elif px==3 and py==3:
      if puzzle==0:
        print("You see a lot of evil robots.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="graphene":
          print("Since graphene is transparent, the robots\' lasers destroy you.")
          wait()
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="toothbrush":
          print("The toothbrush reminds the robots of something.")
          wait()
          wait()
          print("The robots go to the dentist.")
          wait()
          go()
        elif x=="cheese":
          print("You take out cheese.")
          wait()
          print("The robots attempt to eat the cheese.")
          wait()
          print("Robots: Kernel Panic: Cannot eat cheese.")
          wait()
          go()
        else:
          error()
    elif px==4 and py==2:
      if puzzle==0:
        print("You see a giant steel wall.")
        wait()
        print("A computer is on it.")
        wait()
        puzzle=1
      else:
        x=input("Do you want to use graphene(\"graphene\"), the computer(\"computer\"), the toothbrush(\"toothbrush\"), or cheese(\"cheese\")? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="graphene":
          print("You charge into the wall with a graphene spear.")
          wait()
          wait()
          print("It works!")
          go()
        elif x=="computer":
          print("You go to the computer.")
          wait()
          print("It asks for the password.")
          wait()
          print("You guess \"password\".") #If you actually use this password, change it!
          wait()
          print("It works!")
          wait()
          go()
        elif x=="toothbrush":
          print("The computer scans the toothbrush.")
          wait()
          print("It tells you how to brush your teeth.")
          wait()
          wait()
        elif x=="cheese":
          print("The computer scans the cheese.")
          wait()
          print("It states: ")
          wait()
          print(" ERROR: Incompetent User.")
          wait()
          print(" Eliminating User.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          error()
    elif px==5 and py==0:
      if puzzle==0:
        print("You find yourself by a pool.")
        wait()
        print("You see a sign saying: \"No cheese\".")
        wait()
        puzzle=1
      else:
        ask()
        if x=="cheese":
          print("Your monkey overlords are enraged.")
          wait()
          print("Your monkey overlords tell the programmer to remove one life.")
          wait()
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          print("You realize that you can just leave.")
          go()
    elif px==5 and py==1:
      if puzzle==0:
        print("You find yourself surrounded by trees.")
        wait()
        print("They are blocking your way out.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="graphene":
          print("You build a graphene trampoline.")
          wait()
          print("You bounce off of it to the exit.")
          wait()
          go()
        elif x=="toothbrush":
          print("You attempt to brush the trees.")
          wait()
          print("The rangers kick you out for insanity.")
          wait()
          go()
        elif x=="cheese":
          print("You put cheese on the ground.")
          wait()
          print("The animals go for the cheese.")
          wait()
          print("They push you out if the way.")
          wait()
          print("Conveniently, you end up by the door.")
          wait()
          go()
        else:
          error()
    elif px==5 and py==2:
      print("You find a button with the word \"bad idea\" on it.")
      wait()
      wait()
      x=input("To push the button, type \"push\". ")
      wait()
      x=x.rstrip()
      x=x.lower()
      if x=="push":
        print("The air is replaced with antimatter.")
        wait()
        wait()
        lives=0
      else:
        go()
    elif px==0 and py==5:
      if puzzle==0:
        print("A troll blocks your way.")
        wait()
        print("The troll says the following: ")
        wait()
        print(" If you want to cross this bridge, you must answer 3 questions.")
        wait()
        wait()
        puzzle=1
      elif puzzle==1:
        x=input(" What is your name? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x==name.lower():
          puzzle=2
        else:
          print(" WRONG!")
          wait()
          print("The troll throws you off a cliff.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
      elif puzzle==2:
        x=input(" What planet is Denver on? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="earth":
          puzzle=3
        else:
          print(" WRONG!")
          wait()
          print("The troll throws you off a cliff.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
      elif puzzle==3:
        print(" OK. This one\'s a bit complex.")
        wait()
        print(" Mr. Liar always tells lies.")
        wait()
        print(" I asked Mr. Liar, \"If I asked you, \'Am I a troll?\', would you say \'yes\'? \"")
        wait()
        wait()
        wait()
        x=input(" What did Mr. Liar say(\"yes\" or \"no\")? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="yes":
          print(" Correct! You may go!")
          wait()
          print("Programmer: See explanation.txt if you\'re confused.")
          wait()
          go()
        else:
          print(" WRONG!")
          wait()
          print("The troll throws you off a cliff.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
    elif px==1 and py==5:
      if puzzle==0:
        print("You see a door with a note.")
        wait()
        print("The note says: ")
        wait()
        print(" Play computer song to open door.")
        wait()
        print("You see a computer.")
        wait()
        print("It has several buttons.")
        wait()
        puzzle=1
      else:
        x=input("Which button do you click? help, play, or nice(type as written)? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        print("Computer: ")
        wait()
        if x=="help":
          print(" Welcome to Song Player!")
          wait()
          print(" It can do all sorts of things.")
          wait()
          print(" For example it can do [technical thing] and [technical thing] and...")
          wait()
          wait()
          print("You realize the tutorial is an ad.")
          wait()
          wait()
          print("You lose one life out of frustration.")
          wait()
          wait()
          lives=lives-1
        elif x=="nice":
          print(" The start screen has super cow powers.")
          wait()
          print("Confused, you move on.")
          wait()
        elif x=="play":
          print(" Playing song...")
          wait()
          print("Beethoven\'s 9th Symphony plays.")
          wait()
          print("The door opens.")
          go()
        else:
          error()
    elif px==2 and py==5:
      if puzzle==0:
        print("You hear an invisible monster.")
        wait()
        puzzle=1
      else:
        ask()
        if x=="graphene":
          print("You put on graphene armor.")
          wait()
          print("You safely get to the door.")
          go()
        elif x=="toothbrush":
          print("You use your toothbrush to push a button.")
          wait()
          wait()
          print("A 16-ton weight falls on you.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("The monster thanks you for your cheese.")
          wait()
          wait()
          print("The monster helps you to the door.")
          go()
        else:
          error()
    #Finale Section
    elif px==4 and py==3:
      if puzzle==0:
        print("You enter a very large room.")
        wait()
        print("You see a large gathering of people and aliens.")
        wait()
        wait()
        print("They are near a pile of rubble.")
        wait()
        print("A person walks up to you and says:")
        wait()
        print(" Hi. We have been in this maze for a long time.")
        wait()
        wait()
        print(" Luckily, we have a spaceship to get us out.")
        wait()
        wait()
        print(" Unfortunately, it\'s under a pile of rubble.")
        wait()
        wait()
        puzzle=1
      elif puzzle==1:
        ask()
        if x=="graphene":
          print("You use the graphene to create a trampoline.")
          wait()
          wait()
          print("The trampoline bounces the rubble away.")
          wait()
          puzzle=2
        elif x=="toothbrush":
          print("You attempt to use your toothbrush as a lever.")
          wait()
          wait()
          print("Amazingly, you lift the rock.")
          wait()
          print("Less amazingly, the rock crushes you.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("You eat the cheese.")
          wait()
          print("Suddenly, the ship\'s cheese alarm goes off.")
          wait()
          wait()
          print("It blasts you off to Alpha Centauri.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          error()
      elif puzzle==2:
        print("Unfortunately, the electrical system is damaged.")
        wait()
        print("You need something to fill a gap.")
        wait()
        puzzle=3
      else:
        x=input("You can use the Glorious Invisible Lightbulb(\"gil\"), the Epic Small Engine(\"ese\"), or cheese(\"cheese\"). ")
        x=x.rstrip()
        x=x.lower()
        time.sleep(1)
        if x=="gil":
          print("The Invisible Lightbulb works perfectly!") #I once lived in a house with a switch that activated nothing
          wait()
          print("You board the now working spaceship.")
          wait()
          print("You blast out of the maze.")
          wait()
          print("Congratulations! You found the secret ending!")
          time.sleep(4)
          print("Thank you for playing.")
          wait()
          escaped=1
          lives=0
        elif x=="ese":
          print("You connect the ESE to the system.")
          wait()
          print("The engine immediately overheats and explodes.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("You place cheese into the system.")
          wait()
          print("The ship\'s cheese allergy system goes off.")
          wait()
          print("Your monkey overlords are annoyed at the noise.")
          wait()
          print("Your monkey overlords remove all air to stop the noise.")
          wait()
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        else:
          error()
    #Change Intro Room
    elif px+py==8:
      print("You hear a happy monster.")
      wait()
      print("The monster warns you:")
      wait()
      print(" There are horrible, horrible monsters ahead.")
      wait()
      print(" There is a spaceship nearby if you want to avoid them.")
      wait()
      wait()
      wait()
      print(" If you want to fight, here\'s what not to do:")
      wait()
      print(" Look, a distraction!")
      wait()
      print("When you look back, the monster is gone.")
      wait()
      go()
    elif px+py==9:
      if puzzle==0:
        print("You see a very large, very angry monster.")
        wait()
        puzzle=1
      elif puzzle==1:
        start=time.time()
        x=input("Do you fight or flee(type as written)? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="flee":
          print("You attempt to flee, but have nowhere to go.")
          wait()
          wait()
          print("The monster takes one life from your pocket.")
          wait()
          wait()
          lives=lives-1
        elif x=="fight":
          print("You use your new fighting skills.")
          wait()
          end=time.time()
          t=int(end-start)
          print("Since you got them in the last %s seconds, you\'re terrible."%t)
          wait()
          wait()
          print("The monster backs you into a corner.")
          wait()
          wait()
          puzzle=2
        else:
          error()
      elif puzzle==2:
        print("You find three buttons.")
        wait()
        print("One says \"time\".")
        wait()
        print("Another says \"bird\".")
        wait()
        print("Another says \"cheese\".")
        wait()
        puzzle=3
      elif puzzle==3:  
        x=input("Which one do you use, \"time\", \"bird\", or \"cheese\"? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="time":
          print("A time machine activates.")
          wait()
          print("You watch your previous self walk into the room.")
          wait()
          wait()
          puzzle=4
        elif x=="bird":
          print("A bird appears out of nowhere.")
          wait()
          print("The monster crushes you anyway.")
          wait()
          print("You lose one life.")
          wait()
          lives=lives-1
        elif x=="cheese":
          print("Why?")
          wait()
          print("You already have cheese.")
          wait()
        else:
          error()
      else:
        x=input("Do you distract or hide(type as written)? ")
        x=x.rstrip()
        x=x.lower()
        wait()
        if x=="distract":
          print("You bang one of the pillars.")
          wait()
          print("The roof collapses.")
          wait()
          print("You and your past self are crushed.")
          wait()
          print("You lose two lives.")
          wait()
          lives=lives-2
        elif x=="hide":
          print("You hide behind a pillar.")
          wait()
          print("You watch as your past self travels back in time.")
          wait()
          wait()
          print("You leave while the monster is confused.")
          go()
        else:
          error()
    elif px==5 and py==5:
      print("Congratulations! You Win...")
      wait()
      print("The ability to say you won this game.")
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
    maze=[["P",0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,'E']]
    px=0
    py=0
    print("Your monkey overlords have given you %s lives."%lives_orig)
    wait()
    lives=lives_orig
