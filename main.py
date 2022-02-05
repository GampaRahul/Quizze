from player_entry import player_entry_gui
from controller_display import *

teams, questions = player_entry_gui()

if len(teams) > 0:
    game(teams, questions)
