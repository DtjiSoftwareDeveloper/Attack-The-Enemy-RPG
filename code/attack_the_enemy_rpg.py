"""
This file contains source code of the game "Attack The Enemy RPG".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary libraries

import sys
import random
from mpmath import *

mp.pretty = True


# Creating necessary classes


class Player:
    """
    This class contains attributes of the player in this game.
    """

    def __init__(self, name, max_hp, attack_power, defense):
        # type: (str, mpf, mpf, mpf) -> None
        self.name: str = name
        self.level: int = 1
        self.curr_hp: mpf = max_hp
        self.max_hp: mpf = max_hp
        self.attack_power: mpf = attack_power
        self.defense: mpf = defense

    def is_alive(self):
        # type: () -> bool
        return self.curr_hp > 0

    def level_up(self):
        # type: () -> None
        self.level += 1
        self.max_hp *= 2
        self.curr_hp = self.max_hp
        self.attack_power *= 2
        self.defense *= 2

    def attack(self, other):
        # type: (Player) -> None
        other.curr_hp -= self.attack_power - other.defense

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "Name: " + str(self.name) + "\n"
        res += "Level: " + str(self.level) + "\n"
        res += "HP: " + str(self.curr_hp) + "/" + str(self.max_hp) + "\n"
        res += "Attack Power: " + str(self.attack_power) + "\n"
        res += "Defense: " + str(self.defense) + "\n"
        return res


class Enemy(Player):
    """
    This class contains attributes of the enemy in this game.
    """

    def __init__(self, name, max_hp, attack_power, defense):
        # type: (str, mpf, mpf, mpf) -> None
        Player.__init__(self, name, max_hp, attack_power, defense)


# Creating the main function to run the game


def main():
    """
    This main function is used to run the game.
    :return: None
    """

    print("Welcome to 'Attack The Enemy RPG' by 'DtjiSoftwareDeveloper'.")
    print("In this game, the player needs to attack the enemies to win battles and go as far as possible!")
    print("If you reach a higher round than the number shown in 'highscore.txt', the contents of the file ")
    print("'highscore.txt' will be updated with the highest round you reached.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_playing: str = input("Do you want to continue playing this game? ")
    while continue_playing == "Y":
        name: str = input("Please enter your name: ")
        player: Player = Player(name, mpf(125), mpf(40), mpf(25))
        enemy: Enemy = Enemy("CPU", mpf(100), mpf(50), mpf(20))
        curr_round: int = 1  # initial round number
        turn: int = 0  # initial value
        while player.is_alive() and enemy.is_alive():
            print(str("-" * 40) + "ROUND " + str(curr_round) + str("-" * 40))
            print("Your stats:\n" + str(player))
            print("Your enemy's stats:\n" + str(enemy))
            turn += 1
            if turn % 2 == 1:
                print("It is your turn to attack!")
                print("Enter 'ATTACK' to attack!")
                print("Enter anything else to quit this game.")
                action: str = input("What do you want to do? ")
                if action == "ATTACK":
                    player.attack(enemy)
                else:
                    sys.exit()

            else:
                print("It is your enemy's turn to attack!")
                enemy.attack(player)

            if player.is_alive() and not enemy.is_alive():
                print("YOU WIN!")

                # Levelling up the player and the enemy
                player_level_ups: int = random.randint(1, 100)
                enemy_level_ups: int = random.randint(1, 100)
                for i in range(player_level_ups):
                    player.level_up()

                for i in range(enemy_level_ups):
                    enemy.level_up()

                # Advance to next round and reset 'turn' to 0
                curr_round += 1
                turn = 0

            elif enemy.is_alive() and not player.is_alive():
                print("YOU LOSE!!!! " + str(player.name).upper() + " DIED!!!!")
                highscore_file = open("highscore.txt")
                curr_highscore: int = int(highscore_file.readline())
                if curr_round > curr_highscore:
                    # Update the high score
                    highscore_file = open("highscore.txt", "w+")
                    highscore_file.truncate()
                    highscore_file.write(str(curr_round))

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing this game? ")

    sys.exit()


if __name__ == '__main__':
    main()
