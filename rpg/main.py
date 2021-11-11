import random
from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item

# TODO: Refactor all the code and use SOLID principles and good coding practices

# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 999)
hi_elixir = Item("Hi-Elixir", "elixir", "Fully restores party's HP/MP", 999)

grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [
    {"item": potion, "quantity": 15},
    {"item": hi_potion, "quantity": 5},
    {"item": super_potion, "quantity": 5},
    {"item": elixir, "quantity": 5},
    {"item": hi_elixir, "quantity": 2},
    {"item": grenade, "quantity": 5}]

# Instantiate people
player1 = Person("Valos", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Corey", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Roy  ", 3009, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("BBEG ", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
enemy_attack_text = BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.END_C


def main():
    global running

    while running:
        defeated_enemies = 0

        print("================================")

        print("\n")
        print("NAME                 HP                                      MP")
        for player in players:
            player.get_stats()

        for enemy in enemies:
            enemy.get_enemy_stats()

        for player in players:
            if player.get_hp() <= 0:
                continue

            player.choose_action()
            choice = input("Choose action: ")
            index = int(choice) - 1

            # 0 Attack, 1 Magic, 2 Item
            if index == 0:
                dmg = player.generate_damage()
                choice = player.choose_target(enemies)

                enemies[choice].take_damage(dmg)
                colored_damage = BColors.OK_GREEN + str(dmg) + BColors.END_C
                print("\n" + player.name, "attacked", enemies[choice].name.replace(" ", ""),
                      "for", colored_damage, "points of damage.")
            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("     Choose magic: ")) - 1

                if magic_choice == -1:
                    continue

                spell = player.magic[magic_choice]
                magic_dmg = spell.generate_damage()
                current_mp = player.get_mp()

                if spell.cost > current_mp:
                    print(BColors.FAIL + "\nNot enough MP" + BColors.END_C)
                    continue

                player.reduce_mp(spell.cost)

                if spell.spell_type == "black":
                    choice = player.choose_target(enemies)

                    enemies[choice].take_damage(magic_dmg)
                    colored_damage = BColors.OK_GREEN + str(magic_dmg) + BColors.END_C
                    print(BColors.OK_BLUE + "\n" + spell.name + BColors.END_C + " deals",
                          enemies[choice].name.replace(" ", ""),
                          colored_damage, "points of damage.")
                else:
                    player.heal(magic_dmg)
                    print(BColors.OK_BLUE + "\n" + spell.name + " heals for",
                          str(magic_dmg), "HP" + BColors.END_C)
            elif index == 2:
                player.choose_item()
                item_choice = int(input("     Choose item: ")) - 1

                if item_choice == -1:
                    continue

                item = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] == 0:
                    print(BColors.FAIL + "\n" + "None left..." + BColors.END_C)
                    continue

                player.items[item_choice]["quantity"] -= 1

                if item.item_type == "potion":
                    player.heal(item.prop)
                    print(BColors.OK_GREEN + "\n" + item.name + " heals for",
                          str(item.prop), "HP" + BColors.END_C)
                elif item.item_type == "elixir":
                    if item.name == "Hi-Elixir":
                        for i in players:
                            i.hp = i.max_hp
                            i.mp = i.max_mp
                    else:
                        player.hp = player.max_hp
                        player.mp = player.max_mp
                    print(BColors.OK_GREEN + "\n" + item.name + " fully restores HP/MP"
                          + BColors.END_C)
                elif item.item_type == "attack":
                    choice = player.choose_target(enemies)

                    enemies[choice].take_damage(item.prop)
                    print(BColors.FAIL + "\n" + item.name + " deals",
                          enemies[choice].name.replace(" ", ""), str(item.prop),
                          "points of damage" + BColors.END_C)

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemies += 1
                print(BColors.FAIL + BColors.BOLD + enemy.name.replace(" ", "") +
                      BColors.END_C, "has died.")
                enemies.remove(enemy)
                del enemy

        print("\n")
        for enemy in enemies:
            # enemy still attacks dead players...
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:
                # chose target
                target = random.randrange(0, 3)
                enemy_dmg = enemies[0].generate_damage()
                players[target].take_damage(enemy_dmg)
                print(enemy.name.replace(" ", ""), "attacks",
                      players[target].name.replace(" ", ""),
                      "for", BColors.FAIL + str(enemy_dmg) + BColors.END_C)
            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)

                if spell.spell_type == "black":
                    choice = random.randrange(0, len(players))

                    players[choice].take_damage(magic_dmg)
                    colored_damage = BColors.OK_GREEN + str(magic_dmg) + BColors.END_C
                    print(BColors.FAIL + enemy.name.replace(" ", "") +
                          " " + spell.name + BColors.END_C + " deals",
                          players[choice].name.replace(" ", ""),
                          colored_damage, "points of damage.")
                else:
                    enemy.heal(magic_dmg)
                    print(BColors.OK_BLUE + "\n" + spell.name + " heals for",
                          str(magic_dmg), "HP" + BColors.END_C)

        # calculates defeated players
        defeated_players = 0
        for player in players:
            if player.get_hp() == 0:
                defeated_players += 1

        # Check who won
        if defeated_enemies > len(enemies):
            print(BColors.OK_GREEN + "You win!" + BColors.END_C)
            running = False
        elif defeated_players > len(players):
            print(BColors.FAIL + "Your enemies have defeated you!" + BColors.END_C)
            running = False


if __name__ == "__main__":
    main()
