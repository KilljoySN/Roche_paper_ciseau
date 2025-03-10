"""
Nom: Kaize
Groupe: 401
Description: Jeu roche papier ciseau
"""
import arcade
from game_state import GameState


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class MyGame(arcade.Window):
    def __init__(self, longueur, largeur, titre):
        super().__init__(longueur, largeur, titre)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.joueur = arcade.Sprite("assets/faceBeard.png", 0.25, 250, 350)
        self.ordinateur = arcade.Sprite("assets/compy.png", 1.25, 750, 350)
        self.joueurs_list = arcade.SpriteList()
        self.joueurs_list.append(self.joueur)
        self.joueurs_list.append(self.ordinateur)

        self.roche = arcade.Sprite("assets/srock.png", 0.85, 140, 245)
        self.roche_list = arcade.SpriteList()
        self.roche_list.append(self.roche)

        self.papier = arcade.Sprite("assets/spaper.png", 0.85, 260, 235)
        self.papier_list = arcade.SpriteList()
        self.papier_list.append(self.papier)

        self.ciseau = arcade.Sprite("assets/scissors.png", 0.75, 370, 235)
        self.ciseau_list = arcade.SpriteList()
        self.ciseau_list.append(self.ciseau)

        self.joueur_score = 0
        x = 2000
        y = 2000
        a = 2000
        b = 2000
        self.winning_text = (arcade.Text("Le joueur a gagner!", x, y, arcade.color.BLACK))
        self.losing_text = (arcade.Text("L'ordinateur a gagner!", a, b, arcade.color.BLACK))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        nb_points = 0
        if nb_points < 3:
            self.game_state = GameState.ROUND_ACTIVE
            if button == arcade. MOUSE_BUTTON_LEFT:
                self.game_state = GameState.ROUND_DONE

    def on_key_press(self, symbol: int, modifiers: int):
        nb_points = 0
        if nb_points < 3:
            self.game_state = GameState.NOT_STARTED
            if symbol == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
                if symbol == arcade.key.SPACE:
                    self.game_state = GameState.ROUND_ACTIVE

        else:
            self.game_state = GameState.GAME_OVER
            if self.joueur_score == 3:
                x = 300
                y = 600
            else:
                a = 300
                b = 600

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        self.clear()
        self.carree()
        self.joueurs_list.draw()
        self.roche_list.draw()
        self.papier_list.draw()
        self.ciseau_list.draw()
        self.winning_text.draw()
        self.losing_text.draw()
        titre = arcade.Text("Roche Papier Ciseau", 75, 900, arcade.color.BLACK, 80)
        sous_titre = arcade.Text("Appuyer sur un icone pour jouer", 75, 810, arcade.color.BLACK, 50)
        pointage_joueur = arcade.Text("Points du joueur:", 75, 100, arcade.color.BLACK, 30)
        pointage_ordinateur = arcade.Text("Points de l'ordinateur:", 550, 100, arcade.color.BLACK, 30)
        titre.draw()
        sous_titre.draw()
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















































