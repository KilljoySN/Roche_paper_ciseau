"""if state == STATE_PAUSED:
    draw_paused_screen()
elsif state == STATE_PLAYING:
    draw_playing_stuff()
elsif state == STATE_GAMEOVER:
    you_get_the_idea()"""

from enum import Enum


class GameState(Enum):
    NOT_STARTED = 0
    ROUND_ACTIVE = 1
    ROUND_DONE = 2
    GAME_OVER = 3
