import turtle as trtl
import random as rand
 
# Defining and setting our Background_Setting
wn = trtl.Screen()
wn.bgpic("TheBeginning.gif")
 
# Creating our player controlled character
Joah = trtl.Turtle()
Joah.penup()
 
# Creating an enemy for later
CursedArmor = trtl.Turtle()
CursedArmor.ht()
CursedArmor.penup()

death_bolt = trtl.Turtle()
death_bolt.ht()
death_bolt.penup()
death_bolt.goto(-200,-192)
 
# Adding a turtle specifically for guiding the player
Questionare = trtl.Turtle()
Questionare.ht()
Questionare.pensize(10)
Questionare.penup()
Questionare.goto(-220,200)

 
# Adding some sprites to Joah
wizard_sprite_right = "wizardright.gif"
wizard_sprite_left = "wizardleft.gif"
wn.addshape(wizard_sprite_right)
wn.addshape(wizard_sprite_left)
Joah.shape("wizardright.gif")
 
# Adding a sprite for Enemy Units
cursed_armor_sprite = "CursedArmor.gif"
wn.addshape(cursed_armor_sprite)
 
# Adding sprites for Spells
fireball_sprite = "opfireball.gif"
wn.addshape(fireball_sprite)
fireball_selection_sprite = "FireBallSpell.gif"
wn.addshape(fireball_selection_sprite)
 
tornado_sprite = "tornado.gif"
wn.addshape(tornado_sprite)
tornado_selection_sprite = "TornadoSpell.gif"
wn.addshape(tornado_selection_sprite)
 
mighty_meatball_sprite = "MightyMeatball.gif"
wn.addshape(mighty_meatball_sprite)
mighty_meatball_selection_sprite = "MightyMeatballSpell.gif"
wn.addshape(mighty_meatball_selection_sprite)

Battle_Menu_sprite = "BattleMenu.gif"
wn.addshape(Battle_Menu_sprite)

death_bolt_sprite = "death_bolt.gif"
wn.addshape(death_bolt_sprite)

cursed_armor_attack_box_sprite = "cursed_armor_attack_box.gif"
wn.addshape(cursed_armor_attack_box_sprite)

# Adding some turtles for combat and assigning them skins
battle_box = trtl.Turtle()
battle_box.penup()
battle_box.ht()
battle_box.goto(0,250)
battle_box.shape("BattleMenu.gif")

# Now we have to make sure the combat options show up in the right spots on the battle menu
cursed_armor_attack_box_1 = trtl.Turtle()
cursed_armor_attack_box_1.penup()
cursed_armor_attack_box_1.ht()
cursed_armor_attack_box_1.goto(-150,250)
cursed_armor_attack_box_1.shape("cursed_armor_attack_box.gif")

cursed_armor_attack_box_2 = trtl.Turtle()
cursed_armor_attack_box_2.penup()
cursed_armor_attack_box_2.ht()
cursed_armor_attack_box_2.goto(0,250)
cursed_armor_attack_box_2.shape("cursed_armor_attack_box.gif")

cursed_armor_attack_box_3 = trtl.Turtle()
cursed_armor_attack_box_3.penup()
cursed_armor_attack_box_3.ht()
cursed_armor_attack_box_3.goto(150,250)
cursed_armor_attack_box_3.shape("cursed_armor_attack_box.gif")

fireball = trtl.Turtle()
fireball.penup()
fireball.ht()
fireball.goto(520,-192)
fireball.shape("opfireball.gif")
fireball_box = trtl.Turtle()
fireball_box.penup()
fireball_box.ht()
fireball_box.goto(0,250)
fireball_box.shape("FireBallSpell.gif")

tornado = trtl.Turtle()
tornado.penup()
tornado.ht()
tornado.goto(500,-192)
tornado.shape("tornado.gif")
tornado_box = trtl.Turtle()
tornado_box.penup()
tornado_box.ht()
tornado_box.goto(-150,250)
tornado_box.shape("TornadoSpell.gif")

MightMeatball = trtl.Turtle()
MightMeatball.penup()
MightMeatball.ht()
MightMeatball.goto(300,-100)
MightMeatball.shape("MightyMeatball.gif")
MightyMeatball_Box = trtl.Turtle()
MightyMeatball_Box.penup()
MightyMeatball_Box.ht()
MightyMeatball_Box.goto(150,250)
MightyMeatball_Box.shape("MightyMeatballSpell.gif")


# Setting position value and initial position value for Joah as well as some positional values which will aid with 
# telling us when Joah has traveled to a different setting
Joah.goto(0, -192)
JoahDistanceLeft = 0
JoahDistanceRight = 0
Background_Setting = 0

# Code for Joah's movement and combat related displays
Enemies = 0 # setting code to tell the game how many enemies are on screen

def move_left():
    global JoahDistanceLeft
    global Background_Setting
    global Enemies
    Joah.shape("wizardleft.gif")
    Joah.setheading(180)
    Joah.forward(10)
    JoahDistanceLeft = (JoahDistanceLeft - 10)
    # This if statement changes the background when Joah goes off the screen on the left side
    if JoahDistanceLeft < (-650):
        wn.bgpic("DarkForest.gif")
        Background_Setting = (Background_Setting + 1)
    if JoahDistanceLeft < (-650):
        Joah.ht()
        Joah.speed(10)
        Joah.goto(600,-192)
        Joah.st()
        Joah.speed()
    if JoahDistanceLeft < (-650):  #setting up code for the cursed armor to appear when in the dark forest 
        CursedArmor.goto(-200,-192)
        CursedArmor.shape("CursedArmor.gif")
        CursedArmor.st()
        Enemies = (Enemies + 1)
    if Background_Setting == 1: # telling the game to display the battle menu if there is an enemy on the screen
        if Enemies > 0:
            battle_box.st()
            fireball_box.st()
            tornado_box.st()
            MightyMeatball_Box.st()
            hp_control_Joah.st()
            mp_control_Joah.st()
            hp_control_CursedArmor.st()
            Questionare.write("Click a move, kill the Cursed Armor!",  font = ('Candara', 20, 'bold'))
      
def move_right():
    global JoahDistanceRight
    global JoahDistanceLeft
    global Background_Setting
    global Enemies
    Joah.shape("wizardright.gif")
    Joah.setheading(0)
    Joah.forward(10)
    JoahDistanceRight = (JoahDistanceRight + 10)
    JoahDistanceLeft = (JoahDistanceLeft + 10)
    if Background_Setting > 0:         # Changes the background if Joah goes off the left side of the screen in the dark forest and positions Joah
        if JoahDistanceRight > (JoahDistanceLeft + 659):
            Joah.ht()
            Joah.goto(-600,-192)
            Joah.st()
            wn.bgpic("TheBeginning.gif")
            CursedArmor.ht()
            Enemies = (Enemies - 1)
            Background_Setting = (Background_Setting - 1)
            battle_box.ht()
            fireball_box.ht()
            tornado_box.ht()
            MightyMeatball_Box.ht()
            hp_control_Joah.ht()
            mp_control_Joah.ht()
            hp_control_CursedArmor.ht()
            Questionare.clear()

# This code stops Joah from "skidding" (as much)
def stop_right():
   Joah.undobufferentries()
 
def stop_left():
   Joah.undobufferentries()
 
# Setting what keys will move Joah what way
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeyrelease(stop_left, "a")
wn.onkeyrelease(stop_right, "d")

# Code for combat

Joah_hp = 8 # Setting hp/mp values for combat
CursedArmor_hp = 8
Joah_mp = 8

# Making turtles and sprites for combat features
hp_sprite = "HP.gif"
wn.addshape(hp_sprite)
damage_sprite_1 = "HP-1.gif"
wn.addshape(damage_sprite_1)
damage_sprite_2 = "HP-2.gif"
wn.addshape(damage_sprite_2)
damage_sprite_3 = "HP-3.gif"
wn.addshape(damage_sprite_3)
damage_sprite_4 = "HP-4.gif"
wn.addshape(damage_sprite_4)
damage_sprite_5 = "HP-5.gif"
wn.addshape(damage_sprite_5)
damage_sprite_6 = "HP-6.gif"
wn.addshape(damage_sprite_6)
damage_sprite_7 = "HP-7.gif"
wn.addshape(damage_sprite_7)
damage_sprite_0 = "HP0.gif"
wn.addshape(damage_sprite_0)

mp_sprite = "MP.gif"
wn.addshape(mp_sprite)
mp_loss_1 = "MP-1.gif"
wn.addshape(mp_loss_1)
mp_loss_2 = "MP-2.gif"
wn.addshape(mp_loss_2)
mp_loss_3 = "MP-3.gif"
wn.addshape(mp_loss_3)
mp_loss_4 = "MP-4.gif"
wn.addshape(mp_loss_4)
mp_loss_5 = "MP-5.gif"
wn.addshape(mp_loss_5)
mp_loss_6 = "MP-6.gif"
wn.addshape(mp_loss_6)
mp_loss_7 = "MP-7.gif"
wn.addshape(mp_loss_7)
mp_loss_8 = "MP0.gif"
wn.addshape(mp_loss_8)

hp_control_Joah = trtl.Turtle()
hp_control_Joah.penup()
hp_control_Joah.ht()
hp_control_Joah.shape("HP.gif")

hp_control_CursedArmor = trtl.Turtle()
hp_control_CursedArmor.penup()
hp_control_CursedArmor.ht()
hp_control_CursedArmor.shape("HP.gif")

mp_control_Joah = trtl.Turtle()
mp_control_Joah.penup()
mp_control_Joah.ht()
mp_control_Joah.shape(mp_sprite)

# Setting the location for the mana and health bars
hp_control_Joah.goto(-75,300)
mp_control_Joah.goto(75,300)
hp_control_CursedArmor.goto(-200, -100)

# Making the spells useable
tornado_distance = 0
fireball_distance = 0
MightyMeatballDistance = 0
death_bolt_distance = 0
Cursed_armor_attack_count = 0

# Setting movement pattern for when the tornado spell is clicked
def use_tornado(x,y):
   global tornado_distance
   global CursedArmor_hp
   global Joah_mp
   tornado.st()
   if Joah_mp >= (1):
      tornado.st()
      while tornado_distance < (220):
         tornado.backward(50)
         tornado.forward(20)
         tornado_distance = (tornado_distance + 10)
      tornado.ht()
      tornado_distance = (tornado_distance - 220)
      tornado.goto((500,-192))
      Joah_mp = (Joah_mp - 1) # the spell costs 1 mana point
      CursedArmor_hp = (CursedArmor_hp - 1) # the cursed armor takes 1 hitpoint of damage
      if Joah_mp == (0):
         mp_control_Joah.shape("MP0.gif")
      if Joah_mp == (1):
         mp_control_Joah.shape("MP-7.gif")
      if Joah_mp == (2):
         mp_control_Joah.shape("MP-6.gif")
      if Joah_mp == (3):
         mp_control_Joah.shape("MP-5.gif")
      if Joah_mp == (4):
         mp_control_Joah.shape("MP-4.gif")
      if Joah_mp == (5):
         mp_control_Joah.shape("MP-3.gif")
      if Joah_mp == (6):
         mp_control_Joah.shape("MP-2.gif")
      if Joah_mp == (7):
         mp_control_Joah.shape("MP-1.gif")
      if Joah_mp == (8):
         mp_control_Joah.shape("MP.gif")
      if CursedArmor_hp == (0):
         CursedArmor.ht()
         Questionare.clear()
         Questionare.write("Congratulations! You saved the city!",  font = ('Candara', 20, 'bold'))
         hp_control_CursedArmor.shape("HP0.gif")
      if CursedArmor_hp == (1):
         hp_control_CursedArmor.shape("HP-7.gif")
      if CursedArmor_hp == (2):
         hp_control_CursedArmor.shape("HP-6.gif")
      if CursedArmor_hp == (3):
         hp_control_CursedArmor.shape("HP-5.gif")
      if CursedArmor_hp == (4):
         hp_control_CursedArmor.shape("HP-4.gif")
      if CursedArmor_hp == (5):
         hp_control_CursedArmor.shape("HP-3.gif")
      if CursedArmor_hp == (6):
         hp_control_CursedArmor.shape("HP-2.gif") 
      if CursedArmor_hp == (7):
         hp_control_CursedArmor.shape("HP-1.gif")
      if CursedArmor_hp == (8):
         hp_control_CursedArmor.shape("HP.gif")

def use_fireball(x,y):
   global Joah_mp
   global CursedArmor_hp
   global fireball_distance
   if Joah_mp >= (2):
      fireball.st()
      while fireball_distance < (650):
         fireball.backward(30)
         fireball_distance = (fireball_distance + 30)
      fireball.ht()
      fireball_distance = (fireball_distance - 650)
      fireball.goto(520,-192)
      Joah_mp = (Joah_mp - 2) # the spell costs 2 mp
      CursedArmor_hp = (CursedArmor_hp - 2) # the cursed armor takes 2 hit points of damage
      if Joah_mp == (0):
         mp_control_Joah.shape("MP0.gif")
      if Joah_mp == (1):
         mp_control_Joah.shape("MP-7.gif")
      if Joah_mp == (2):
         mp_control_Joah.shape("MP-6.gif")
      if Joah_mp == (3):
         mp_control_Joah.shape("MP-5.gif")
      if Joah_mp == (4):
         mp_control_Joah.shape("MP-4.gif")
      if Joah_mp == (5):
         mp_control_Joah.shape("MP-3.gif")
      if Joah_mp == (6):
         mp_control_Joah.shape("MP-2.gif")
      if Joah_mp == (7):
         mp_control_Joah.shape("MP-1.gif")
      if Joah_mp == (8):
         mp_control_Joah.shape("MP.gif")
      if CursedArmor_hp == (0):
         CursedArmor.ht()
         Questionare.clear()
         Questionare.write("Congratulations! You saved the city!",  font = ('Candara', 20, 'bold'))
         hp_control_CursedArmor.shape("HP0.gif")
      if CursedArmor_hp == (1):
         hp_control_CursedArmor.shape("HP-7.gif")
      if CursedArmor_hp == (2):
         hp_control_CursedArmor.shape("HP-6.gif")
      if CursedArmor_hp == (3):
         hp_control_CursedArmor.shape("HP-5.gif")
      if CursedArmor_hp == (4):
         hp_control_CursedArmor.shape("HP-4.gif")
      if CursedArmor_hp == (5):
         hp_control_CursedArmor.shape("HP-3.gif")
      if CursedArmor_hp == (6):
         hp_control_CursedArmor.shape("HP-2.gif") 
      if CursedArmor_hp == (7):
         hp_control_CursedArmor.shape("HP-1.gif")
      if CursedArmor_hp == (8):
         hp_control_CursedArmor.shape("HP.gif")

def use_MightyMeatball(x,y):
   global Joah_mp
   global CursedArmor_hp
   global MightyMeatballDistance
   global Cursed_armor_attack_count
   global Joah_hp
   global death_bolt_distance
   if Joah_mp >= (3):
      MightMeatball.st()
      while MightyMeatballDistance < (650):
         MightMeatball.backward(30)
         MightyMeatballDistance = (MightyMeatballDistance + 30)
      MightMeatball.ht()
      MightyMeatballDistance = (MightyMeatballDistance - 650)
      MightMeatball.goto(300,-100)
      Joah_mp = (Joah_mp - 3) # The spell costs 3 mana points
      CursedArmor_hp = (CursedArmor_hp - 3) # The cursed armor takes 3 hit points of damage
      if Joah_mp == (0):
         mp_control_Joah.shape("MP0.gif")
      if Joah_mp == (1):
         mp_control_Joah.shape("MP-7.gif")
      if Joah_mp == (2):
         mp_control_Joah.shape("MP-6.gif")
      if Joah_mp == (3):
         mp_control_Joah.shape("MP-5.gif")
      if Joah_mp == (4):
         mp_control_Joah.shape("MP-4.gif")
      if Joah_mp == (5):
         mp_control_Joah.shape("MP-3.gif")
      if Joah_mp == (6):
         mp_control_Joah.shape("MP-2.gif")
      if Joah_mp == (7):
         mp_control_Joah.shape("MP-1.gif")
      if Joah_mp == (8):
         mp_control_Joah.shape("MP.gif")
      if CursedArmor_hp == (0):
         CursedArmor.ht()
         Questionare.clear()
         Questionare.write("Congratulations! You saved the city!",  font = ('Candara', 20, 'bold'))
         hp_control_CursedArmor.shape("HP0.gif")
      if CursedArmor_hp == (1):
         hp_control_CursedArmor.shape("HP-7.gif")
      if CursedArmor_hp == (2):
         hp_control_CursedArmor.shape("HP-6.gif")
      if CursedArmor_hp == (3):
         hp_control_CursedArmor.shape("HP-5.gif")
      if CursedArmor_hp == (4):
         hp_control_CursedArmor.shape("HP-4.gif")
      if CursedArmor_hp == (5):
         hp_control_CursedArmor.shape("HP-3.gif")
      if CursedArmor_hp == (6):
         hp_control_CursedArmor.shape("HP-2.gif") 
      if CursedArmor_hp == (7):
         hp_control_CursedArmor.shape("HP-1.gif")
      if CursedArmor_hp == (8):
         hp_control_CursedArmor.shape("HP.gif")


# Making it so if you click a spell you will cast it
fireball_box.onclick(use_fireball)
tornado_box.onclick(use_tornado)
MightyMeatball_Box.onclick(use_MightyMeatball)

wn.listen()
trtl.mainloop()