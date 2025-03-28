from game_play import (
    create_player,
    display_menu,
    ask_question,
    continue_game,
    display_scoreboard,
    award_badges,
)
from classes import Player

player = Player(create_player())
menu = display_menu()
category_points = {}
badge_list = []

while True:
    player.questions_asked += 1

    game_mode = menu
    if ask_question(game_mode):
        player.score += 1
        award_badges(game_mode, category_points, badge_list)
    display_scoreboard(player, badge_list)

    continueGame = continue_game(menu)
    if continueGame is False:
        display_scoreboard(player, badge_list)
        break
    else:
        menu = continueGame
