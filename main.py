import time
import random


class Character():

    def __init__(self, name="none", hp=100, ap=50):

        self.name = name
        self.hp = hp
        self.ap = ap
        self.items = ["Cane", "Felt Hat"]

    def take_dmg(self, dmg):

        self.hp = self.hp - dmg

    def is_dead(self):

        if self.hp < 1:
            return True
        else:
            return False

    def get_atk(self):

        atk = random.randint(0, self.ap)
        return atk

    def sneak(self):

        rnd = random.randint(0, 1)

        if rnd == 0:
            return True
        else:
            return False

    def rnd_attack(self):

        atk = random.choice(["attack", "defend"])

        return atk

class Combat_manager():

    def check_attack(self, pc, npc):

        while not pc.is_dead() and not npc.is_dead():

            atk = self.check_answer("attack or defend", ["attack", "defend"])
            print("player " + str(atk))
            npc_atk = npc.rnd_attack()
            print("npc " + npc_atk)
            if atk == "attack":

                if npc_atk == "attack":

                    pc.take_dmg(npc.get_atk())
                    npc.take_dmg(pc.get_atk())

                else:

                    pc.take_dmg(npc.get_atk()/2)
                    npc.take_dmg(pc.get_atk()/3)

            else:

                if npc_atk == "attack":

                    npc.take_dmg(pc.get_atk() / 2)
                    pc.take_dmg(npc.get_atk() / 3)

                else:

                    print("no damage")

            print("player has " + str(pc.hp) + " hit points")
            print("NPC has " + str(npc.hp) + " hit points")

    def check_answer(self, question, answers):

        answer = " "

        while answer not in answers:
            answer = input(question).lower()

class Story():

    def __init__(self):

        self.cm = Combat_manager()
        print("""
                          ,===:'.,            `-._
                                        `:.`---.__         `-._
                                         `:.     `--.         `.
                                            \.        `.         `.
                                    (,,(,    \.         `.   ____,-`.,
                                 (,'     `/   \.   ,--.___`.'
                             ,  ,'  ,--.  `,   \.;'         `
                              `{T, {    \  :    \;
                                d,,'    /  /    //
                                m;;    /  ,' ,-//.    ,---.      ,
                                \;'   /  ,' /  _  \  /  _  \   ,'/
                                      \   `'  / \  `'  / \  `.' /
                                       `.___,'   `.__,'   `.__,'

                """)
        print("Welcome to:")
        time.sleep(2)
        print("The Return of Sleep Hollow: Ichabob's Revenge")
        time.sleep(2)
        self.new_game()

    def check_answer(self, question, answers):

        answer = " "

        while answer not in answers:
            answer = input(question).lower()

        return answer

    def new_game(self):
        self.create_char()
        self.outside()

    def create_char(self):

        name = input("Please enter a name for your character: ")
        self.pc = Character(name)

    def dead(self):
        print("You are dead.")
        answer = self.check_answer("Do you want to start again?", ["yes", "no"])

        if answer == "yes":
            self.new_game()
        else:
            print("Game Over")

    def outside(self):

        f = open("intro.text", 'r')

        print(f.readline())
        print(f.readline())
        # print("You are a slave. Your master has brought you to the dark cave.")
        # print("Many people have died here before.")
        # print("Your master commands that you enter the cave to collect the Evil book of spells")

        answer = self.check_answer("Do you enter the cave?", ["yes", "no"])

        if answer == "yes":
            self.cave()
        else:
            print("When you say no, your master draws his sword and kills you.")
            self.dead()

    def cave(self):

        skel = Character(hp=50, ap=25)

        print("You enter the cave. Inside there is a skeleton with a key on it's neck on an alter. Across the room there is a chest.")
        options = ["leave the cave", "take the key", "sneak to the chest", "walk to the chest"]
        print("You can:")

        for item in options:
            print(item)

        answer = self.check_answer("What will you do?", options)

        if answer == "leave the cave":
            print("You don't have the book, so your master kills you")
            self.dead()

        elif answer == "take the key":

            print("you take the key, but the skeleton wakes up and attacks you")

            self.cm.check_attack(self.pc, skel)

            if self.pc.is_dead():
                print("The skeleton wins the fight, you are dead.")
                self.dead()
            else:
                print("you win the fight and get the key")
                self.pc.items.append("key")
                self.chest()

        elif answer == "sneak to the chest":
            print("you attempt to sneak to the chest")
            if self.pc.sneak():
                print("You manage to sneak to the chest")
            else:
                print("When you try to sneak the skeleton wakes up.. and attacks you.")

        else:
            print("You walk to the chest but the skeleton wakes and attacks you.")

    def chest(self):

        print("You got to the chest!")

new_game = Story()
