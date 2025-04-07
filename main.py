"""
Nom: Kaize
Groupe: 401
Description: Jeu roche papier ciseau
"""

import arcade
import random
from game_state import GameState
from attack_animation import AttackAnimation, AttackType
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class MyGame(arcade.Window):
    def __init__(self, longueur, largeur, titre):
        super().__init__(longueur, largeur, titre)
        self.titre = None
        self.sous_titre = None
        self.winning_text = None
        self.pointage_joueur = None
        self.pointage_ordinateur = None
        self.game_on = None
        arcade.set_background_color(arcade.color.ONYX)
        self.player_attack = -1
        self.choix_ordinateur = None
        self.game_state = GameState.NOT_STARTED
        self.joueur = arcade.Sprite("assets/faceBeard.png", 0.25, 250, 350)
        self.ordinateur = arcade.Sprite("assets/compy.png", 1.25, 750, 350)
        self.joueurs_list = arcade.SpriteList()
        self.joueurs_list.append(self.joueur)
        self.joueurs_list.append(self.ordinateur)

        self.rock_joueur = AttackAnimation(AttackType.ROCK)
        self.roche_list = arcade.SpriteList()
        self.roche_list.append(self.rock_joueur)

        self.paper_joueur = AttackAnimation(AttackType.PAPER)
        self.papier_list = arcade.SpriteList()
        self.papier_list.append(self.paper_joueur)

        self.cissors_joueur = AttackAnimation(AttackType.SCISSORS)
        self.ciseau_list = arcade.SpriteList()
        self.ciseau_list.append(self.cissors_joueur)

        self.rock_pc = AttackAnimation(AttackType.ROCK)
        self.roche_list = arcade.SpriteList()
        self.roche_list.append(self.rock_pc)

        self.paper_pc = AttackAnimation(AttackType.PAPER)
        self.papier_list = arcade.SpriteList()
        self.papier_list.append(self.paper_pc)

        self.cissors_pc = AttackAnimation(AttackType.SCISSORS)
        self.ciseau_list = arcade.SpriteList()
        self.ciseau_list.append(self.cissors_pc)

        self.joueur_score = 0
        self.ordinateur_score = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_state == GameState.ROUND_ACTIVE:
            print(f"On_mouse_press {self.game_state}")
            if self.rock_joueur.collides_with_point((x, y)):
                self.player_attack = 0
                print("joueur: roche")
            elif self.paper_joueur.collides_with_point((x, y)):
                self.player_attack = 1
                print("joueur: papier")
            elif self.cissors_joueur.collides_with_point((x, y)):
                self.player_attack = 2
                print("joueur: ciseau")

    def on_key_press(self, symbol: int, modifiers: int):
        print(f"On_key_press {self.game_state}")
        if self.game_state == GameState.NOT_STARTED:
            print("round not started")
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
                print("round active")
        if self.game_state == GameState.ROUND_DONE:
            print("round done")
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
                print("round active")
                self.choix_ordinateur = None
                self.player_attack = -1
        if self.game_state == GameState.GAME_OVER:
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.NOT_STARTED
                self.ordinateur_score = 0
                self.joueur_score = 0

    def on_update(self, delta_time: float):
        self.titre = arcade.Text("Roche Papier Ciseau", 75, 900, arcade.color.GOLD, 80)
        self.sous_titre = arcade.Text("Appuyer sur 'ESPACE' pour jouer", 75, 810, arcade.color.GOLD, 50)
        self.game_on = arcade.Text("Le jeu commence!", 75, 810, arcade.color.GOLD, 50)

        self.pointage_joueur = arcade.Text(f"Points du joueur: {self.joueur_score}", 75, 100, arcade.color.GOLD, 30)
        self.pointage_ordinateur = \
            (arcade.Text(f"Points de l'ordinateur: {self.ordinateur_score}", 550, 100, arcade.color.GOLD, 30))

        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack in [0, 1, 2]:
            self.choix_ordinateur = random.randint(0, 2)

            """if self.choix_ordinateur == 0:
                print("ordinateur: rock")
                self.rock_pc.center_x = 760        # a rcade.Sprite("assets/srock.png", 0.85, 760, 245)
                self.rock_pc.center_y = 245
                #if self.game_state == GameState.ROUND_DONE:
                    #self.roche_list.remove(self.rock)

            elif self.choix_ordinateur == 1:
                print("ordinateur: paper")
                self.paper_pc.center_x = 760
                self.paper_pc.center_y = 233  # = arcade.Sprite("assets/spaper.png", 0.85, 760, 233)
                #if self.game_state == GameState.ROUND_DONE:
                    #self.papier_list.remove(self.paper)

            elif self.choix_ordinateur == 2:
                print("ordinateur: cissors")
                self.cissors_pc.center_x = 750
                self.cissors_pc.center_y = 235        # = arcade.Sprite("assets/scissors.png", 0.75, 750, 235)
                #if self.game_state == GameState.ROUND_DONE:
                    #self.ciseau_list.remove(self.cissors)"""

            if self.choix_ordinateur == 0 and self.player_attack == 0:
                pass
                print("tie")

            elif self.choix_ordinateur == 0 and self.player_attack == 1:
                self.joueur_score += 1
                print("win")

            elif self.choix_ordinateur == 0 and self.player_attack == 2:
                self.ordinateur_score += 1
                print("loss")

            elif self.choix_ordinateur == 1 and self.player_attack == 0:
                self.ordinateur_score += 1
                print("loss")

            elif self.choix_ordinateur == 1 and self.player_attack == 1:
                pass
                print("tie")

            elif self.choix_ordinateur == 1 and self.player_attack == 2:
                self.joueur_score += 1
                print("win")

            elif self.choix_ordinateur == 2 and self.player_attack == 0:
                self.joueur_score += 1
                print("win")

            elif self.choix_ordinateur == 2 and self.player_attack == 1:
                self.ordinateur_score += 1
                print("loss")

            elif self.choix_ordinateur == 2 and self.player_attack == 2:
                pass
                print("tie")

            self.game_state = GameState.ROUND_DONE
            print("round done")
            print(self.joueur_score)
            print(self.ordinateur_score)

            if self.joueur_score == 3:
                self.winning_text = arcade.Text("Le joueur a gagner!", 75, 810, arcade.color.GOLD, 50)
                self.game_state = GameState.GAME_OVER

            elif self.ordinateur_score == 3:
                self.winning_text = arcade.Text("L'ordinateur a gagner!", 75, 810, arcade.color.GOLD, 50)
                self.game_state = GameState.GAME_OVER

    def on_draw(self):
        self.clear()
        self.carree()
        self.joueurs_list.draw()
        self.roche_list.draw()
        self.papier_list.draw()
        self.ciseau_list.draw()

        self.titre.draw()
        if self.game_state == GameState.NOT_STARTED:
            self.sous_titre.draw()
        if self.game_state == GameState.ROUND_ACTIVE:
            self.game_on.draw()
        if self.game_state == GameState.ROUND_DONE:
            # changer position sprite choix ordi et afficher.
            if self.choix_ordinateur == 0:
                self.rock_pc.center_x = 760
                self.rock_pc.center_y = 245
                self.roche_list.draw()

            elif self.choix_ordinateur == 1:
                self.paper_pc.center_x = 760
                self.paper_pc.center_x = 245
                self.papier_list.draw()

            elif self.choix_ordinateur == 2:
                self.paper_pc.center_x = 750
                self.paper_pc.center_x = 245
                self.papier_list.draw()

            # changer position sprite choix joueur et afficher
            if self.player_attack == 0:
                self.rock_joueur.center_x = 140
                self.rock_joueur.center_y = 245
                self.roche_list.draw()
                if self.rock_joueur in self.roche_list:
                    self.roche_list.remove(self.rock_joueur)
            elif self.player_attack == 1:
                self.paper_joueur.center_x = 260
                self.paper_joueur.center_y = 235
                self.papier_list.draw()
                if self.paper_joueur in self.papier_list:
                    self.papier_list.remove(self.paper_joueur)
            elif self.player_attack == 2:
                self.cissors_joueur.center_x = 369
                self.cissors_joueur.center_y = 235
                self.ciseau_list.draw()
                if self.cissors_joueur in self.ciseau_list:
                    self.ciseau_list.remove(self.cissors_joueur)

        self.pointage_joueur.draw()
        self.pointage_ordinateur.draw()
        if self.game_state == GameState.GAME_OVER:
            self.winning_text.draw()

    def carree(self):
        arcade.draw_lrbt_rectangle_outline(75, 185, 175, 285, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(195, 305, 175, 285, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(315, 425, 175, 285, arcade.color.BLACK, 5)

        arcade.draw_lrbt_rectangle_outline(695, 805, 175, 285, arcade.color.BLACK, 5)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Jeu roche papier ciseau")

    arcade.run()


main()















































