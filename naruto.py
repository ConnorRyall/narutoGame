import random
random_list = ["box1", "box2", "box3", "box4"]

class Ninja:
  def __init__(self, name, special_move, health, special_move_power):
    self.punch = 15
    self.kick = 10
    self.name = name
    self.special_move = special_move 
    self.health = health
    self.special_move_power = special_move_power

  def __repr__(self):
    return ("You have chosen {name}! {name} has {health} health points and his special move is {special_move}!".format(name = self.name, special_move = self.special_move, health = self.health))
 
  def attack_punch(self, other_ninja):
    other_ninja.health = other_ninja.health - self.punch
    return "{name} punched {other_ninja}! {other_ninja}'s health has lowered to {new_health}!".format(name = self.name, other_ninja = other_ninja.name, new_health = other_ninja.health)

  def attack_kick(self, other_ninja):
    other_ninja.health = other_ninja.health - self.kick
    return "{name} kicked {other_ninja}! {other_ninja}'s health has lowered to {new_health}!".format(name = self.name, other_ninja = other_ninja.name, new_health = other_ninja.health)

  def attack_special_move(self, other_ninja):
    other_ninja.health = other_ninja.health - self.special_move_power
    return "{name} used {special_move} on {other_ninja}! {other_ninja}'s health has lowered to {new_health}!".format(name = self.name, special_move = self.special_move, other_ninja = other_ninja.name, new_health = other_ninja.health)

  def use_box(self, Box):
    self.health = self.health + Box.points
    return "You used {box_name}! Your health changed to {health}!".format(box_name = Box.name, health = self.health) 

Naruto = Ninja("Naruto", "Rasengan", 200, 50)
Sasuke = Ninja("Sasuke", "Chidori", 190, 45)
Kakashi = Ninja("Kakashi", "Raikiri", 180, 40)

class Box:
  def __init__(self, name, points):
    self.name = name
    self.points = points 

  def __repr__(self):
    return ("You have chosen to use {name}!".format(name = self.name))

box1 = Box("Box 1", 50)
box2 = Box("Box 2", -75)
box3 = Box("Box 3", -100)
box4 = Box("Box 4", 150)

counter = 2
player_1 = input("Welcome to the Hidden Leaf Village! Please enter your name to begin! ")

choice = input("Welcome " + str(player_1) + "!" + " Now, please choose your Ninja! You can choose between Naruto, Sasuke, or Kakashi. ")

if choice == "Naruto":
  print(Naruto)
elif choice == "Kakashi":
  print(Kakashi)
elif choice == "Sasuke":
  print(Sasuke)
else:
  print("Please type your choice exactly how it is presented.")
  choice = input("Welcome " + str(player_1) + "!" + " Now, please choose your Ninja! You can choose between Naruto, Sasuke, or Kakashi. ")

opponent = input("Now choose your opponent! ")

if opponent == "Naruto" or opponent == "Kakashi" or opponent == "Sasuke":
  enter0 = input("Confirmed! Press ENTER to continue!")

else:
  print("Please type your choice exactly how it is presented.")
  opponent = input("Now choose your opponent! ")

if choice == "Naruto" and opponent == "Kakashi":
  print(Kakashi)
  print("Time for battle! Naruto vs. Kakashi!")

if choice == "Naruto" and opponent == "Sasuke":
  print(Sasuke)
  print("Time for battle! Naruto vs. Sasuke!")

if choice == "Kakashi" and opponent == "Naruto":
  print(Naruto)
  print("Time for battle! Kakashi vs. Naruto!")

if choice == "Kakashi" and opponent == "Sasuke":
  print(Sasuke)
  print("Time for battle! Kakashi vs. Sasuke!")

if choice == "Sasuke" and opponent == "Naruto":
  print(Naruto)
  print("Time for battle! Sasuke vs. Naruto!")

if choice == "Sasuke" and opponent == "Kakashi":
  print(Kakashi)
  print("Time for battle! Sasuke vs. Kakashi!")

first_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if first_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if first_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if first_move == "SPECIAL":
  print(eval(choice).attack_special_move(eval(opponent)))
  counter -= 1

if first_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if first_move != "KICK" and first_move != "PUNCH" and first_move != "SPECIAL" and first_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  first_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")
  if first_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if first_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if first_move == "SPECIAL":
    print(eval(choice).attack_special_move(eval(opponent)))
    counter -= 1

  if first_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter1 = input("Press ENTER to continue!")

if enter1 == "":
  print(eval(opponent).attack_punch(eval(choice)))

second_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if second_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if second_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if second_move == "SPECIAL":
  print(eval(choice).attack_special_move(eval(opponent)))
  counter -= 1
  if counter == 0:
    print("You have run out of chakara! You won't be able to use {special_move} again!".format(special_move = eval(choice).special_move))

if second_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if second_move != "KICK" and second_move != "PUNCH" and second_move != "SPECIAL" and second_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  second_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if second_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if second_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if second_move == "SPECIAL":
    print(eval(choice).attack_special_move(eval(opponent)))
    counter -= 1
    if counter == 0:
      print("You have run out of chakara! You won't be able to use {special_move} again!".format(special_move = eval(choice).special_move))

  if second_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter2 = input("Press ENTER to continue!")

if enter2 == "":
  random_box = random.choice(random_list)
  eval(opponent).use_box(eval(random_box))
  if random_box == "box1":
    print("{opponent} used Box 1! It was a potion! {opponent}'s health has increased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box2":
    print("{opponent} used Box 2! It was poison! {opponent}'s health has decreased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box3":
    print("{opponent} used Box 3! It was poison! {opponent}'s health has decreased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box4":
    print("{opponent} used Box 4! It was a potion! {opponent}'s health has increased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

third_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if third_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if third_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if third_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if third_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if third_move != "KICK" and third_move != "PUNCH" and third_move != "SPECIAL" and third_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  third_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if third_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if third_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if third_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
        exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if third_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter3 = input("Press ENTER to continue!")

if enter3 == "":
  print(eval(opponent).attack_special_move(eval(choice)))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

fourth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if fourth_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if fourth_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if fourth_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if fourth_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if fourth_move != "KICK" and fourth_move != "PUNCH" and fourth_move != "SPECIAL" and fourth_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  fourth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if fourth_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if fourth_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if fourth_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
          exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if fourth_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter4 = input("Press ENTER to continue!")

if enter4 == "":
  print(eval(opponent).attack_kick(eval(choice)))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

fifth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if fifth_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if fifth_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if fifth_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if fifth_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if fifth_move != "KICK" and fifth_move != "PUNCH" and fifth_move != "SPECIAL" and fifth_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  fifth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if fifth_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if fifth_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if fifth_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
          exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if fifth_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter5 = input("Press ENTER to continue!")

if enter5 == "":
  print(eval(opponent).attack_special_move(eval(choice)))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

sixth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if sixth_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if sixth_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if sixth_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if sixth_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if sixth_move != "KICK" and sixth_move != "PUNCH" and sixth_move != "SPECIAL" and sixth_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  sixth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if sixth_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if sixth_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if sixth_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
          exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if sixth_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter6 = input("Press ENTER to continue!")

if enter6 == "":
  random_box = random.choice(random_list)
  eval(opponent).use_box(eval(random_box))
  if random_box == "box1":
    print("{opponent} used Box 1! It was a potion! {opponent}'s health has increased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box2":
    print("{opponent} used Box 2! It was poison! {opponent}'s health has decreased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box3":
    print("{opponent} used Box 3! It was poison! {opponent}'s health has decreased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))
  if random_box == "box4":
    print("{opponent} used Box 4! It was a potion! {opponent}'s health has increased to {health}!".format(opponent = eval(opponent).name, health = eval(opponent).health))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

seventh_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if seventh_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if seventh_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if seventh_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if seventh_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if seventh_move != "KICK" and seventh_move != "PUNCH" and seventh_move != "SPECIAL" and seventh_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  seventh_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if seventh_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if seventh_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if seventh_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
          exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if seventh_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

enter7 = input("Press ENTER to continue!")

if enter7 == "":
  print(eval(opponent).attack_kick(eval(choice)))

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

eighth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

if eighth_move == "KICK":
  print(eval(choice).attack_kick(eval(opponent)))

if eighth_move == "PUNCH":
  print(eval(choice).attack_punch(eval(opponent)))

if eighth_move == "SPECIAL":
  if counter == 0:
    print("You don't have enough chakara for this move! Choose another!")
    sub_move = input("KICK, PUNCH, or BOX? ")
    if sub_move == "KICK":
      print(eval(choice).attack_kick(eval(opponent)))
    if sub_move == "PUNCH":
      print(eval(choice).attack_punch(eval(opponent)))
    if sub_move == "BOX":
      box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
      if box_choice == "1":
        print("It was a potion!")
        print(eval(choice).use_box(box1))
      if box_choice == "2":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box2))
      if box_choice == "3":
        print("Oh no! It was poison!")
        print(eval(choice).use_box(box3))
      if box_choice == "4":
        print("It was a potion!")
        print(eval(choice).use_box(box4))
      if eval(choice).health <= 0:
        print("You have been defeated! GAME OVER! :(")
        exit()
  else:
    print(eval(choice).attack_special_move(eval(opponent)))

if eighth_move == "BOX":
  box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
  if box_choice == "1":
    print("It was a potion!")
    print(eval(choice).use_box(box1))
  if box_choice == "2":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box2))
  if box_choice == "3":
    print("Oh no! It was poison!")
    print(eval(choice).use_box(box3))
  if box_choice == "4":
    print("It was a potion!")
    print(eval(choice).use_box(box4))

if eighth_move != "KICK" and eighth_move != "PUNCH" and eighth_move != "SPECIAL" and eighth_move != "BOX":
  print("You haven't entered a valid command! Type the command in ALL CAPS!")
  eighth_move = input("What would you like to do? KICK, PUNCH, SPECIAL, or use a BOX? ")

  if eighth_move == "KICK":
    print(eval(choice).attack_kick(eval(opponent)))

  if eighth_move == "PUNCH":
    print(eval(choice).attack_punch(eval(opponent)))

  if eighth_move == "SPECIAL":
    if counter == 0:
      print("You don't have enough chakara for this move! Choose another!")
      sub_move = input("KICK, PUNCH, or BOX? ")
      if sub_move == "KICK":
        print(eval(choice).attack_kick(eval(opponent)))
      if sub_move == "PUNCH":
        print(eval(choice).attack_punch(eval(opponent)))
      if sub_move == "BOX":
        box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
        if box_choice == "1":
          print("It was a potion!")
          print(eval(choice).use_box(box1))
        if box_choice == "2":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box2))
        if box_choice == "3":
          print("Oh no! It was poison!")
          print(eval(choice).use_box(box3))
        if box_choice == "4":
          print("It was a potion!")
          print(eval(choice).use_box(box4))
        if eval(choice).health <= 0:
          print("You have been defeated! GAME OVER! :(")
          exit()
    else:
      print(eval(choice).attack_special_move(eval(opponent)))

  if eighth_move == "BOX":
    box_choice = input("Which box will you choose? 1, 2, 3 or 4? Careful! Some of them are dangerous! ")
    if box_choice == "1":
      print("It was a potion!")
      print(eval(choice).use_box(box1))
    if box_choice == "2":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box2))
    if box_choice == "3":
      print("Oh no! It was poison!")
      print(eval(choice).use_box(box3))
    if box_choice == "4":
      print("It was a potion!")
      print(eval(choice).use_box(box4))

if eval(opponent).health <= 0:
  print("You have defeated {opponent}!".format(opponent = eval(opponent).name))
  exit()

if eval(choice).health <= 0:
  print("You have been defeated! GAME OVER! :(")
  exit()