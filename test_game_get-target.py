import unittest

from Nyemil_Naga import get_targets

class TestGetTargetsFunction(unittest.TestCase):
    def test_get_targets_with_powerup(self):
        player_x, player_y = 100, 100
        blinky_x, blinky_y = 50, 50
        inky_x, inky_y = 60, 60
        pinky_x, pinky_y = 70, 70
        clyde_x, clyde_y = 80, 80
        powerup = True
        eaten_ghost = [False, False, False, False]
        targets = get_targets(player_x, player_y, blinky_x, blinky_y, inky_x, inky_y, pinky_x, pinky_y, clyde_x, clyde_y, powerup, eaten_ghost)
        self.assertEqual(targets, [(900, 900), (900, 100), (100, 900), (450, 450)])  # Assuming player is at (100, 100) and powerup is True

    def test_get_targets_without_powerup(self):
        player_x, player_y = 100, 100
        blinky_x, blinky_y = 50, 50
        inky_x, inky_y = 60, 60
        pinky_x, pinky_y = 70, 70
        clyde_x, clyde_y = 80, 80
        powerup = False
        eaten_ghost = [False, False, False, False]
        targets = get_targets(player_x, player_y, blinky_x, blinky_y, inky_x, inky_y, pinky_x, pinky_y, clyde_x, clyde_y, powerup, eaten_ghost)
        self.assertEqual(targets, [(100, 100), (100, 100), (100, 100), (100, 100)])  # Assuming player is at (100, 100) and powerup is False

if __name__ == '__main__':
    unittest.main()
