import random



print("Carrot in a Box")

input("Press Enter  to begin...")

p1Name = "Player_1"
p2Name = "Player_2"

playerNames = p1Name[:11].center(11) +"   "+p2Name[:11].center(11)

print("""HERE ARE TWO BOXES:
   _________    _________
  /        /|  /        /|
 +--------+ | +--------+ |
 |  RED   | | |  GOLD  | |
 |  BOX   | / |  BOX   | /
 +--------+/  +--------+/""")
print()
print(playerNames)
print()
print(f"{p1Name}, you have a RED box in front of you.")
print(f"{p2Name}, you have a GOLD box in front of you.")
print()
print(f"{p1Name}, you will get to look into your box.")
print(f"{p2Name.upper()}, close your eyes and don't look!!!")
print(f"When {p2Name} has closed their eyes, press Enter...")
print()
print(f"{p1Name} here is the inside of your box:")

if random.randint(1,2) == 1:
    carrtInFirstBox = True
else:
    carrtInFirstBox = False

if carrtInFirstBox:

    print("""
        ___VV___    
       |   VV   |   
       |   VV   |   
       |___||___|   _________
      /    ||  /|  /        /|
     +--------+ | +--------+ |
     |  RED   | | |  GOLD  | |
     |  BOX   | / |  BOX   | /
     +--------+/  +--------+/
      (carrot!)""")
    print(playerNames)
else:
    print("""
        ________    
       |        |   
       |        |   
       |________|   _________
      /        /|  /        /|
     +--------+ | +--------+ |
     |  RED   | | |  GOLD  | |
     |  BOX   | / |  BOX   | /
     +--------+/  +--------+/
     (no carrot!)""")
    print(playerNames)

input("Press Enter to continue....")

print("\n"*100)
print(f"{p1Name}, tell {p2Name} to open their eyes.")
input("Press Enter to continue....")

print()
print(f"{p1Name}, say one of the following sentences to {p2Name}.")
print(" 1) There is a carrot in my box.")
print(" 2) There is not a carrot in my box.")
print()
input("Press Enter to continue....")

print()
print(f"{p2Name}, do you want to swap boxes with {p1Name}? YES/NO")
while True:
    response = input("> ").upper()
    if not (response.startswith("Y")) or (response.startswith("N")):
        print(f"{p2Name}, please enter 'YES' or 'NO'")
    else:
        break
firstBox = "RED "
secondBox = "GOLD"
if response.startswith("Y"):
    carrtInFirstBox = not carrtInFirstBox
    firstBox, secondBox = secondBox, firstBox
print("""
   _________    _________
  /        /|  /        /|
 +--------+ | +--------+ |
 |  {}  | | |  {}  | |
 |  BOX   | / |  BOX   | /
 +--------+/  +--------+/""".format(firstBox,secondBox))
print(playerNames)

input("Press Enter to reveal the winner...")
print()

if carrtInFirstBox:
    print("""
        ___VV___    
       |   VV   |   
       |   VV   |   
       |___||___|   _________
      /    ||  /|  /        /|
     +--------+ | +--------+ |
     |  {}  | | |  {}  | |
     |  BOX   | / |  BOX   | /
     +--------+/  +--------+/""".format(firstBox,secondBox))

else:
    print("""
                     ___VV___    
                    |   VV   |   
                    |   VV   |   
       _________    |___||___|
      /        /|  /    ||  /|
     +--------+ | +--------+ |
     |  {}  | | |  {}  | |
     |  BOX   | / |  BOX   | /
     +--------+/  +--------+/""".format(firstBox,secondBox))

print(playerNames)

if carrtInFirstBox:
    print(f"{p1Name} is the winner!")
else:
    print(f"{p2Name} is the winner!")

print('Thanks for playing!')


