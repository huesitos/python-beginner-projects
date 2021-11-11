import math
import random


class BColors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.df = atk
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost
        return self.mp

    def choose_action(self):
        i = 1
        print("\n" + "     " + BColors.BOLD + self.name + BColors.END_C)
        print(BColors.OK_BLUE + BColors.BOLD + "     ACTIONS:" + BColors.END_C)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + BColors.OK_BLUE + BColors.BOLD + "     MAGIC:" + BColors.END_C)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + BColors.OK_GREEN + BColors.BOLD + "     ITEMS:" + BColors.END_C)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1

        print("\n" + BColors.FAIL + BColors.BOLD + "     TARGET:" + BColors.END_C)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = ((self.hp / self.max_hp) * 100) / 2
        for i in range(math.ceil(bar_ticks)):
            hp_bar += "█"

        if len(hp_bar) < 50:
            hp_bar += " " * (50 - len(hp_bar))

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                     __________________________________________________")
        print(BColors.BOLD + self.name + ":  " + current_hp + " |" +
              BColors.FAIL + hp_bar + BColors.END_C +
              BColors.BOLD + "|" + BColors.END_C)

    def get_stats(self):

        # self.hp = self.max_hp * .75
        hp_bar = ""
        bar_ticks = ((self.hp / self.max_hp)*100)/4
        for i in range(math.ceil(bar_ticks)):
            hp_bar += "█"

        if len(hp_bar) < 25:
            hp_bar += " " * (25 - len(hp_bar))

        mp_bar = ""
        mp_ticks = ((self.mp/self.max_mp)*100)/10

        for i in range(math.ceil(mp_ticks)):
            mp_bar += "█"

        if len(mp_bar) < 10:
            mp_bar += " " * (10 - len(mp_bar))

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                     _________________________               __________")
        print(BColors.BOLD + self.name + ":    "+current_hp+" |" +
              BColors.OK_GREEN + hp_bar + BColors.END_C +
              BColors.BOLD + "|     "+current_mp+" |" +
              BColors.OK_BLUE + mp_bar + BColors.END_C +
              BColors.BOLD + "|" + BColors.END_C)

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = (self.hp / self.max_hp) * 100

        if self.mp < spell.cost or (spell.spell_type == "white" and pct > 50):
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
