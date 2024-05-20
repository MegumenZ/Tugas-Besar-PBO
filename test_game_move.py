import unittest

# Misalnya, kita memiliki fungsi move_player dalam file game.py
from Nyemil_Naga import move_player

class TestGameFunctions(unittest.TestCase):
    def test_move_player_right(self):
        play_x, play_y = 100, 100
        player_speed = 5
        direction = 0
        turns_allowed = [True, False, False, False]
        new_x, new_y = move_player(play_x, play_y, direction, turns_allowed, player_speed)
        self.assertEqual(new_x, 105)
        self.assertEqual(new_y, 100)

    def test_move_player_left(self):
        play_x, play_y = 100, 100
        player_speed = 5
        direction = 1
        turns_allowed = [False, True, False, False]
        new_x, new_y = move_player(play_x, play_y, direction, turns_allowed, player_speed)
        self.assertEqual(new_x, 95)
        self.assertEqual(new_y, 100)

    def test_move_player_up(self):
        play_x, play_y = 100, 100
        player_speed = 5
        direction = 2
        turns_allowed = [False, False, True, False]
        new_x, new_y = move_player(play_x, play_y, direction, turns_allowed, player_speed)
        self.assertEqual(new_x, 100)
        self.assertEqual(new_y, 95)

    def test_move_player_down(self):
        play_x, play_y = 100, 100
        player_speed = 5
        direction = 3
        turns_allowed = [False, False, False, True]
        new_x, new_y = move_player(play_x, play_y, direction, turns_allowed, player_speed)
        self.assertEqual(new_x, 100)
        self.assertEqual(new_y, 105)

if __name__ == '__main__':
    unittest.main()
