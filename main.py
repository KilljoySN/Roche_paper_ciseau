"""
Nom: Kaize
Groupe: 401
Description: Jeu roche papier ciseau
"""
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class MyGame(arcade.Window):
    def __init__(self, longueur, largeur, titre):
        super().__init__(longueur, largeur, titre)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.clear()
        self.list = arcade.SpriteList()
        self.visage = arcade.Sprite("assets/faceBeard.png", 1, 100, 200)

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if symbol == arcade.key.SPACE:
            pass

    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_draw(self):
        self.statique()
        self.list.draw()
        titre = arcade.Text("Roche Papier Ciseau", 75, 900, arcade.color.BLACK, 80)
        sous_titre = arcade.Text("Appuyer sur un icone pour jouer", 75, 810, arcade.color.BLACK, 50)
        pointage_joueur = arcade.Text("Points du joueur:", 75, 100, arcade.color.BLACK, 30)
        pointage_ordinateur = arcade.Text("Points de l'ordinateur:", 550, 100, arcade.color.BLACK, 30)
        titre.draw()
        sous_titre.draw()
        pointage_joueur.draw()
        pointage_ordinateur.draw()



    def statique(self):
        arcade.draw_lrbt_rectangle_outline(200, 300, 300, 400, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(80, 180, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(200, 300, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(320, 420, 180, 280, arcade.color.BLACK, 5)

        arcade.draw_lrbt_rectangle_outline(700, 800, 300, 400, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(580, 680, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(700, 800, 180, 280, arcade.color.BLACK, 5)
        arcade.draw_lrbt_rectangle_outline(820, 920, 180, 280, arcade.color.BLACK, 5)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Jeu roche papier ciseau")

    arcade.run()


main()















































