import time

class player:
    def __init__(self, attack, HP, speed):
        self.attack = attack
        self.HP = HP
        self.speed = speed

    def statshow(self):
        print('Your current stats are:')
        print('Attack:', self.attack, '\nHP:', self.HP, '\nSpeed:', self.speed)

    def weapon(self, newattack):
        self.newattack = newattack
        self.attack = self.newattack + self.attack

    def armour(self, defense):
        self.defense = defense
        self.HP = self.HP + self.defense

    def sped(self, fst):
        self.fst = fst
        self.speed = self.speed + self.fst

    a = False
    d = False

class room:
    def __init__(self, left, right, front):
        self.left = left
        self.right = right
        self.front = front

    def desc(self):
        print('To your left is ' + self.left)
        print('To your right is ' + self.right)
        print('In font of you is ' + self.front)

class enemy:

    def __init__(self, attack, HP, speed):
        self.attack = attack
        self.HP = HP
        self.speed = speed

    def statshow(self):
        print('Enemy stats:')
        print('Attack:', self.attack, '\nHP:', self.HP, '\nSpeed:', self.speed)

def pick(th):
    print('You picked up ' + th)

def next(dor):
    p1.statshow()
    print('You entered room ', end = '')
    print(dor)

def wrng():
    print('WRONG CHOICE!!!')

def fight(at1, hp1, sp1, at2, hp2, sp2):
    if sp1 >= sp2:
        hp2 = hp2 - at1
        if hp2 > 0:
            hp1 = hp1 - at2
            if hp1 > 0:
                return fight(at1, hp1, sp1, at2, hp2, sp2)
            else:
                return False
        else:
            return True
    else:
        hp1 = hp1 - at2
        if hp1 > 0:
            hp2 = hp2 - at1
            if hp2 > 0:
                return fight(at1, hp1, sp1, at2, hp2, sp2)
            else:
                return True
        else:
            return False

def dead(num):
    print('YOU DIED!\nGAME OVER')
    print('You reached room', num)
    exit()

def fchoice():
    return int(input('What will you do?\n1:Fight\n2:Run left\n3:Run right'))


print('---------------------Welcome to Dungeons and  The Creatures--------------------')
print('The rules are simple. You will be presented with a several options throughout the dungeon. For selecting the option of your choice, enter the number corresponding to your choice.')
print('Your objective is to exit the dungeon. Initially, you will be given a total of 15 points, which you may distribute among your 3 stats, attack, HP, and speed, according to your will.')
print('While you are in the dungeon, you may find certain items to increase your stats, and providing you with additional defence.')
print("When in a fight, the first turn will be given to whomever has higher speed stat. The defender will lose HP equal to attack points of the attacker. if you obtain armour, additional defense will increase your HP.")


def getstat():
    print('Enter your...')
    attack = int(input("Attack:"))
    HP = int(input("HP:"))
    speed = int(input("Speed:"))
    totstat=attack + speed + HP
    if totstat > 15 or attack == 0 or HP == 0 or speed == 0:
        print('Your total exceeds 15, or one of the stats is 0, which is forbidden. Enter again.')
        getstat()
    return attack, HP, speed

attack, HP, speed = getstat()
p1 = player(attack, HP, speed)
time.sleep(2)
print('Let the game')
for i in range(5):
    time.sleep(0.4)
    print('.')
time.sleep(0.4)
print('BEGIN')
for i in range(15):
    print('.', end = '')
time.sleep(2)

def roomone():
    print('\nYou wake up in a dark room, where the only light is coming from a dim lantern to your right.')
    time.sleep(3)
    r1=room('a wall that seems old but sturdy', 'the lantern', 'A door that seems to be unlocked.')
    r1.desc()
    time.sleep(3)
    ch1=int(input(print('What do you do?\n1:Pick up the lantern, then go through the door.\n2:Go through the door without lantern.')))
    time.sleep(3)
    if ch1 == 1:
        pick('Lantern')
        next(2)
    elif ch1 == 2:
        p1.sped(-1)
        print('YOU LOST 1 SPEED POINT DUE TO LACK OF VISIBILITY')
        next(2)
    else:
        wrng()
        roomone()

def roomtwo():
    time.sleep(6)
    print('There is a strong stench in the room, and you hear a faint groan.\nSuddenly, a creature with green and rotting flesh appeared.')
    time.sleep(3)
    print("IT'S A ZOMBIE!")
    e1 = enemy(2, 3, 1)
    time.sleep(1)
    e1.statshow()
    time.sleep(3)
    ch2 = fchoice()
    if ch2 == 1:
       res = fight(p1.attack, p1.HP, p1.speed, e1.attack, e1.HP, e1.speed)
    elif ch2 == 2:
        print('A wall is all you find. You turn around to see that the zombie has caught up to you. now you must fight.')
        res = fight(p1.attack, p1.HP, p1.speed, e1.attack, e1.HP, e1.speed)
    elif ch2 == 3:
        print('You see something shine on the floor.\nIT IS A SWORD!')
        time.sleep(2)
        pick('sword')
        time.sleep(1)
        print('Your attack has been increased by 3 points.')
        p1.weapon(3)
        time.sleep(2)
        print('You turn around,ready to fight.')
        res = fight(p1.attack, p1.HP, p1.speed, e1.attack, e1.HP, e1.speed)
        p1.a =True
    else:
        wrng()
        roomtwo()

    if res == True:
        time.sleep(3)
        print('YOU WON!\nYour HP is restored.')
        time.sleep(2)
        p1.statshow()
        time.sleep(3)
        print('With the zombie dead, you look around the room.')
        time.sleep(3)
        if ch2 == 1 or ch2 == 2:
            r2 = room('a wall', 'a sword', 'a door')
            r2.desc()
            time.sleep(3)
            ch3 = int(input(print('What do you do?\n1:Go through door after picking up sword.\n2:Go through door without picking up sword.')))
            if ch3 == 1:
                pick('sword')
                print('Your attack has been increased by 3 points.')
                p1.weapon(3)
                time.sleep(3)
                next(3)
                p1.a = True
            elif ch3 == 2:
                time.sleep(3)
                next(3)
            else:
                wrng()
                roomtwo()
        else:
            time.sleep(3)
            print('You see the door leading to the next room. You go through.')
            time.sleep(2)
            next(3)
    else:
        time.sleep(3)
        dead(2)

def roomthree():
    time.sleep(5)
    print('You hear the sounds of stones hitting each other as a gigantic figure appears before you.')
    time.sleep(3)
    print('IT IS A GOLEM!')
    e2=enemy(8, 9, 2)
    time.sleep(1)
    e2.statshow()
    time.sleep(3)
    ch4 = fchoice()
    time.sleep(2)
    if ch4 == 1:
        res = fight(p1.attack, p1.HP, p1.speed, e2.attack, e2.HP, e2.speed)
    elif ch4 == 2:
        print("Something hit your leg as you run. You look down to see what it is. It is an armour!\nDue to the Golem's slow speed, you have enough time to put on the armour.")
        time.sleep(5)
        pick('armour')
        time.sleep(2)
        print('Your HP has been increased by 5 points.')
        p1.armour(5)
        time.sleep(2)
        print('You turn around,ready to fight.')
        res = fight(p1.attack, p1.HP, p1.speed, e2.attack, e2.HP, e2.speed)
        p1.d = True
    elif ch4 == 3:
        print('A wall is all you find. You turn around to see that the Golem has caught up to you. now you must fight.')
        res = fight(p1.attack, p1.HP, p1.speed, e2.attack, e2.HP, e2.speed)
    else:
        wrng()
        roomthree()

    time.sleep(3)
    if res == True:
        print('YOU WON!\nYour HP is restored.')
        time.sleep(3)
        print('With the Golem dead, you look around the room.')
        time.sleep(3)
        if ch4 == 1 or ch4 == 3:
            r2 = room('a armour', 'a wall', 'a door')
            r2.desc()
            time.sleep(5)
            ch3 = int(input(print('What do you do?\n1:Go through door after picking up armour.\n2:Go through door without picking up armour.')))
            if ch3 == 1:
                time.sleep(1)
                pick('armour')
                time.sleep(1)
                print('Your HP has been increased by 5 points.')
                p1.armour(5)
                time.sleep(3)
                next(4)
                p1.d = True
            elif ch3 == 2:
                time.sleep(3)
                next(4)
            else:
                wrng()
                roomtwo()
        else:
            print('You see the door leading to the next room. You go through.')
            time.sleep(3)
            next(4)
    else:
        dead(3)

def roomfour():
    time.sleep(3)
    print('You feel a immense heat as sson as you step into the room. The source is in front of you.')
    time.sleep(3)
    print('It is a huge DRAGON!')
    time.sleep(2)
    e3 = enemy(12,11,10)
    e3.statshow()
    time.sleep(3)
    print('The dragon is too fast to outrun, you must prepare to fight.')
    time.sleep(3)
    if p1.a == False or p1.d == False:
        print('Without weapons and armour, you stood no chance. The dragonfire engulfs you.')
        dead(4)
        exit()
    print('As you raise your sword, the dragon opens its jaw, but instead of the fire you were expecting, words came out.')
    time.sleep(5)
    print("'I do not wish to fight you human, lower your weapon. I am stronger than you are, if i wanted, you would be dead already.'")
    time.sleep(7)
    ch5 = int(input('What do you do?\n1:Attack\n2:Lower sword'))
    time.sleep(5)
    if ch5 == 1:
        print('As you swing your sword towards the dragon, a light is emitted from the tip.')
        time.sleep(3)
        print("The light pierces the dragon's chest, as it speaks its final words")
        time.sleep(3)
        print("'YOU SAW THROUGH MY DECEPTION, AND USED THE CURSED BLADE....HOW?")
        time.sleep(3)
        print('The dragon falls to the ground and its body turns to ash.')
        time.sleep(3)
        print('You see the final door as the ash blows away., and start walking towards it')
        for i in range(5):
            time.sleep(0.5)
            print('.')
        print('You made it, you get to feel the delicate warmth of sunlight on your face', end='')
        for i in range(3):
            time.sleep(0.5)
            print('.', end='')
        print('You win.')
    elif ch5 == 2:
        print('A smile appears on the dragons scaly face as you lower your sword. He starts speaking again')
        time.sleep(3)
        print("'Many-a-men have stood where you stand, and they have betrayed me. And here I stay trapped.'")
        time.sleep(3)
        print("'Together, we can escape, but how can I trust you when you still don't trust me?'")
        time.sleep(3)
        print("'Drop your weapon and armour, and seal our alliance. Refuse, and to be enemies is our fate.'")
        time.sleep(3)
        ch6 = int(input('What will you do?\n1:Agree\n2:Fight'))
        time.sleep(3)
        if ch6 == 1:
            print('You take off your armour and drop your sword. As you smile, the dragon laughs.')
            time.sleep(5)
            print('The dragon speaks')
            time.sleep(1)
            print("'Thank you, my dear ally, for being just as foolish as those before you.'")
            time.sleep(3)
            print("'Without the cursed sword, you cannot harm me, and without the devil's armour, my flame will reach you.'")
            time.sleep(7)
            print('As you realise your fault, you know it is already too late. The dragon has already opened its jaws.')
            time.sleep(3)
            print('You see a bright flash, and the last thing you feel is hellfire.')
            time.sleep(7)
            print('Nice try. But you are dead now. GAME OVER.')
        elif ch6 == 2:
            print('As you swing your sword towards the dragon, a light is emitted from the tip.')
            time.sleep(3)
            print("The light pierces the dragon's chest, as it speaks its final words")
            time.sleep(3)
            print("'YOU SAW THROUGH MY DECEPTION, AND USED THE CURSED BLADE....HOW?")
            time.sleep(3)
            print('The dragon falls to the ground and its body turns to ash.')
            time.sleep(3)
            print('You see the final door as the ash blows away., and start walking towards it')
            for i in range(5):
                time.sleep(0.5)
                print('.')
            print('You made it, you get to feel the delicate warmth of sunlight on your face', end='')
            for i in range(3):
                time.sleep(0.5)
                print('.', end='')
            print('You win.')
        else:
            wrng()
            roomfour()
    else:
        wrng()
        roomfour()


roomone()
roomtwo()
roomthree()
roomfour()