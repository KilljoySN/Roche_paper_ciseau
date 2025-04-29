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
        self.point_loss = None
        self.point_won = None
        self.lead = None
        self.egale = None
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
        self.rock_joueur.center_x = 133
        self.rock_joueur.center_y = 233
        self.roche_list = arcade.SpriteList()
        self.roche_list.append(self.rock_joueur)

        self.paper_joueur = AttackAnimation(AttackType.PAPER)
        self.paper_joueur.center_x = 260
        self.paper_joueur.center_y = 235
        self.papier_list = arcade.SpriteList()
        self.papier_list.append(self.paper_joueur)

        self.cissors_joueur = AttackAnimation(AttackType.SCISSORS)
        self.cissors_joueur.center_x = 369
        self.cissors_joueur.center_y = 235
        self.ciseau_list = arcade.SpriteList()
        self.ciseau_list.append(self.cissors_joueur)

        self.rock_pc = AttackAnimation(AttackType.ROCK)
        self.rock_pc.center_x = 750
        self.rock_pc.center_y = 230
        self.pc_roche_list = arcade.SpriteList()
        self.pc_roche_list.append(self.rock_pc)

        self.paper_pc = AttackAnimation(AttackType.PAPER)
        self.paper_pc.center_x = 750
        self.paper_pc.center_y = 230
        self.pc_papier_list = arcade.SpriteList()
        self.pc_papier_list.append(self.paper_pc)

        self.cissors_pc = AttackAnimation(AttackType.SCISSORS)
        self.cissors_pc.center_x = 750
        self.cissors_pc.center_y = 230
        self.pc_ciseau_list = arcade.SpriteList()
        self.pc_ciseau_list.append(self.cissors_pc)

        self.joueur_score = 0
        self.ordinateur_score = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.rock_joueur.collides_with_point((x, y)):
                self.player_attack = 0

            elif self.paper_joueur.collides_with_point((x, y)):
                self.player_attack = 1

            elif self.cissors_joueur.collides_with_point((x, y)):
                self.player_attack = 2

    def on_key_press(self, symbol: int, modifiers: int):
        if self.game_state == GameState.NOT_STARTED:
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE

        if self.game_state == GameState.ROUND_DONE:
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
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
        self.point_loss = arcade.Text("Tu as perdu le point!", 220, 750, arcade.color.RED, 50)
        self.point_won = arcade.Text("Tu as gagner le point!", 210, 750, arcade.color.GREEN, 50)
        self.egale = arcade.Text("Égalité!", 400, 750, arcade.color.WHITE, 50)

        self.rock_joueur.on_update(delta_time)
        self.paper_joueur.on_update(delta_time)
        self.cissors_joueur.on_update(delta_time)
        self.rock_pc.on_update(delta_time)
        self.paper_pc.on_update(delta_time)
        self.cissors_pc.on_update(delta_time)

        self.pointage_joueur = arcade.Text(f"Points du joueur: {self.joueur_score}", 75, 100, arcade.color.GOLD, 30)
        self.pointage_ordinateur = \
            (arcade.Text(f"Points de l'ordinateur: {self.ordinateur_score}", 550, 100, arcade.color.GOLD, 30))

        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack in [0, 1, 2]:
            self.choix_ordinateur = random.randint(0, 2)

            if self.choix_ordinateur == 0 and self.player_attack == 0:
                self.lead = 2

            elif self.choix_ordinateur == 0 and self.player_attack == 1:
                self.joueur_score += 1
                self.lead = 0

            elif self.choix_ordinateur == 0 and self.player_attack == 2:
                self.ordinateur_score += 1
                self.lead = 1

            elif self.choix_ordinateur == 1 and self.player_attack == 0:
                self.lead = 1
                self.ordinateur_score += 1

            elif self.choix_ordinateur == 1 and self.player_attack == 1:
                self.lead = 2

            elif self.choix_ordinateur == 1 and self.player_attack == 2:
                self.lead = 0
                self.joueur_score += 1

            elif self.choix_ordinateur == 2 and self.player_attack == 0:
                self.lead = 0
                self.joueur_score += 1

            elif self.choix_ordinateur == 2 and self.player_attack == 1:
                self.lead = 1
                self.ordinateur_score += 1

            elif self.choix_ordinateur == 2 and self.player_attack == 2:
                self.lead = 2

            self.game_state = GameState.ROUND_DONE

            if self.joueur_score == 3:
                self.winning_text = arcade.Text("Le joueur a gagner!", 155, 600, arcade.color.WHITE, 60)
                self.game_state = GameState.GAME_OVER

            elif self.ordinateur_score == 3:
                self.winning_text = arcade.Text("L'ordinateur a gagner!", 155, 600, arcade.color.WHITE, 60)
                self.game_state = GameState.GAME_OVER

    def on_draw(self):
        self.clear()

        arcade.draw_lrbt_rectangle_outline(75, 185, 175, 285, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(195, 305, 175, 285, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(315, 425, 175, 285, arcade.color.BLACK, 5)

        arcade.draw_lrbt_rectangle_outline(695, 805, 175, 285, arcade.color.BLACK, 5)

        self.joueurs_list.draw()
        self.titre.draw()
        self.pointage_joueur.draw()
        self.pointage_ordinateur.draw()

        if self.game_state == GameState.NOT_STARTED:
            self.sous_titre.draw()
            self.choix_ordinateur = -1
            self.player_attack = -1
            self.ordinateur_score = 0
            self.joueur_score = 0

        if self.game_state == GameState.ROUND_ACTIVE:
            self.roche_list.draw()
            self.papier_list.draw()
            self.ciseau_list.draw()
            if self.lead == 0:
                self.point_won.draw()
            elif self.lead == 1:
                self.point_loss.draw()
            elif self.lead == 2:
                self.egale.draw()

        if self.game_state == GameState.ROUND_DONE:
            if self.choix_ordinateur == 0:
                self.pc_roche_list.draw()

            elif self.choix_ordinateur == 1:
                self.pc_papier_list.draw()

            elif self.choix_ordinateur == 2:
                self.pc_ciseau_list.draw()

            if self.player_attack == 0:
                self.roche_list.draw()

            elif self.player_attack == 1:
                self.papier_list.draw()

            elif self.player_attack == 2:
                self.ciseau_list.draw()

        if self.game_state == GameState.GAME_OVER:
            self.winning_text.draw()

def de             if self.choix_ordinateur == 0:
                self.pc_roche_list.draw()

            elif self.choix_ordinateur == 1:
                self.pc_papier_list.draw()

            elif self.choix_ordinateur == 2:
                self.pc_ciseau_list.draw()

            if self.player_attack == 0:
                self.roche_list.draw()

            elif self.player_attack == 1:
                self.papier_list.draw()

            elif self.player_attack == 2:
                self.ciseau_list.draw()

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Jeu roche papier ciseau")

    arcade.run()


main()
