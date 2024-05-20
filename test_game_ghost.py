import unittest

from Nyemil_Naga import Ghost

class TestGhostClass(unittest.TestCase):
    def test_ghost_initialization(self):
        ghost = Ghost(100, 100, (200, 200), 2, "blinky_img.png", 0, False, False, 0)
        self.assertEqual(ghost.x, 100)
        self.assertEqual(ghost.y, 100)
        self.assertEqual(ghost.target, (200, 200))
        self.assertEqual(ghost.speed, 2)
        self.assertEqual(ghost.img, "blinky_img.png")
        self.assertEqual(ghost.direction, 0)
        self.assertFalse(ghost.dead)
        self.assertFalse(ghost.in_box)
        self.assertEqual(ghost.id, 0)

    def test_ghost_move(self):
        ghost = Ghost(100, 100, (200, 200), 2, "blinky_img.png", 0, False, False, 0)
        ghost.x, ghost.y = ghost.move()
        self.assertEqual(ghost.x, 102)  # Assuming move increments x by speed
        self.assertEqual(ghost.y, 100)  # Assuming y remains the same

if __name__ == '__main__':
    unittest.main()
