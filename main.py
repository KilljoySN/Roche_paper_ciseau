"""
Nom: Kaize
Groupe: 401
Description: Jeu roche papier ciseau
"""
import turtle

import arcade
import random
from game_state import GameState


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class MyGame(arcade.Window):
    def __init__(self, longueur, largeur, titre):
        super().__init__(longueur, largeur, titre)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player_attack = -1
        self.choix_ordinateur = None
        self.game_state = GameState.NOT_STARTED
        self.joueur = arcade.Sprite("assets/faceBeard.png", 0.25, 250, 350)
        self.ordinateur = arcade.Sprite("assets/compy.png", 1.25, 750, 350)
        self.joueurs_list = arcade.SpriteList()
        self.joueurs_list.append(self.joueur)
        self.joueurs_list.append(self.ordinateur)

        self.rock = arcade.Sprite("assets/srock.png", 0.85, 140, 245)
        self.roche_list = arcade.SpriteList()
        self.roche_list.append(self.rock)

        self.paper = arcade.Sprite("assets/spaper.png", 0.85, 260, 235)
        self.papier_list = arcade.SpriteList()
        self.papier_list.append(self.paper)

        self.cissors = arcade.Sprite("assets/scissors.png", 0.75, 370, 235)
        self.ciseau_list = arcade.SpriteList()
        self.ciseau_list.append(self.cissors)

        self.joueur_score = 0
        self.ordinateur_score = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_state == GameState.ROUND_ACTIVE:
            print("Round active")
            if self.rock.collides_with_point((x, y)):
                self.player_attack = 0
                print("roche")
            elif self.paper.collides_with_point((x, y)):
                self.player_attack = 1
                print("papier")
            elif self.cissors.collides_with_point((x, y)):
                self.player_attack = 2
                print("ciseau")

    def on_key_press(self, symbol: int, modifiers: int):
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

    def on_update(self, delta_time: float):
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack in [0, 1, 2]:
            print(f"round active and player attack = {self.player_attack}")
            self.choix_ordinateur = random.choice([self.rock, self.paper, self.cissors])

            if self.choix_ordinateur == self.rock:
                print("ordinateur: rock")
                self.rock = arcade.Sprite("assets/srock.png", 0.85, 760, 245)
                self.roche_list.append(self.rock)

            elif self.choix_ordinateur == self.paper:
                print("ordinateur: paper")
                self.paper = arcade.Sprite("assets/spaper.png", 0.85, 760, 233)
                self.papier_list.append(self.paper)

            elif self.choix_ordinateur == self.cissors:
                print("ordinateur: cissors")
                self.cissors = arcade.Sprite("assets/scissors.png", 0.75, 750, 235)
                self.ciseau_list.append(self.cissors)

            if self.choix_ordinateur == self.rock and self.player_attack == 0:
                pass
                print("tie")
            elif self.choix_ordinateur == self.rock and self.player_attack == 1:
                self.joueur_score += 1
                print("loss")
            elif self.choix_ordinateur == self.rock and self.player_attack == 2:
                self.ordinateur_score += 1
                print("win")
            elif self.choix_ordinateur == self.paper and self.player_attack == 0:
                self.ordinateur_score += 1
                print("win")
            elif self.choix_ordinateur == self.paper and self.player_attack == 1:
                print("tie")
            elif self.choix_ordinateur == self.paper and self.player_attack == 2:
                self.joueur_score += 1
                print("loss")
            elif self.choix_ordinateur == self.cissors and self.player_attack == 0:
                self.joueur_score += 1
                print("")
            elif self.choix_ordinateur == self.cissors and self.player_attack == 1:
                self.ordinateur_score += 1
                print("")
            elif self.choix_ordinateur == self.cissors and self.player_attack == 2:
                print("tie")
            self.game_state = GameState.ROUND_DONE
            print("round done")
            if self.joueur_score == 3:
                self.winning_text = arcade.Text("Le joueur a gagner!", 75, 810, arcade.color.BLACK, 50)
                self.game_state = GameState.GAME_OVER
            elif self.ordinateur_score == 3:
                self.winning_text = arcade.Text("L'ordinateur a gagner!", 75, 810, arcade.color.BLACK, 50)
                self.game_state = GameState.GAME_OVER

    def on_draw(self):
        self.clear()
        self.carree()
        self.joueurs_list.draw()
        self.roche_list.draw()
        self.papier_list.draw()
        self.ciseau_list.draw()
        if self.game_state == GameState.GAME_OVER:
            self.winning_text.draw()

        titre = arcade.Text("Roche Papier Ciseau", 75, 900, arcade.color.BLACK, 80)
        if self.game_state == GameState.NOT_STARTED:
            sous_titre = arcade.Text("Appuyer sur un icone pour jouer", 75, 810, arcade.color.BLACK, 50)
            sous_titre.draw()
        if self.game_state == GameState.ROUND_ACTIVE:
            sous_titre = arcade.Text("Le jeu commence!", 75, 810, arcade.color.BLACK, 50)
            sous_titre.draw()

        pointage_joueur = arcade.Text(f"Points du joueur: {self.joueur_score}", 75,  100, arcade.color.BLACK, 30)
        pointage_ordinateur = \
            (arcade.Text(f"Points de l'ordinateur: {self.ordinateur_score}", 550, 100, arcade.color.BLACK, 30))
        titre.draw()
        pointage_joueur.draw()
        pointage_ordinateur.draw()

    def carree(self):
        arcade.draw_lrbt_rectangle_outline(200, 300, 300, 400, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(80, 180, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(200, 300, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(320, 420, 180, 280, arcade.color.BLACK, 5)

        arcade.draw_lrbt_rectangle_outline(700, 800, 300, 400, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(700, 800, 180, 280, arcade.color.BLACK, 5)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Jeu roche papier ciseau")

    arcade.run()


main()















































