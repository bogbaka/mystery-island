"""Automated tests for Mystery Island."""

import unittest

from game import (
    new_game,
    move_player,
    pick_up_item,
    light_beacon,
    is_win,
)


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Blessing")

    def test_new_game_starts_correctly(self):
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])

    def test_invalid_move_does_not_change_state(self):
        original = self.player.copy()
        success, message = move_player(self.player, "Lighthouse")

        self.assertFalse(success)
        self.assertEqual(self.player, original)

    def test_legal_move_consumes_one_energy(self):
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_wrong_direction_is_rejected(self):
        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_rope_can_only_be_collected_once(self):
        move_player(self.player, "Jungle")

        first_success, message = pick_up_item(self.player)
        second_success, message = pick_up_item(self.player)

        self.assertTrue(first_success)
        self.assertFalse(second_success)
        self.assertEqual(self.player["inventory"].count("rope"), 1)

    def test_bridge_requires_rope(self):
        move_player(self.player, "Jungle")
        move_player(self.player, "Cave")

        success, message = move_player(self.player, "Old Bridge")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Cave")
        self.assertEqual(self.player["energy"], 3)

    def test_lighthouse_requires_lantern(self):
        move_player(self.player, "Jungle")
        pick_up_item(self.player)
        move_player(self.player, "Cave")
        move_player(self.player, "Old Bridge")
        move_player(self.player, "Lighthouse")

        success, message = light_beacon(self.player)

        self.assertFalse(success)
        self.assertFalse(is_win(self.player))

    def test_correct_inventory_and_location_can_win(self):
        move_player(self.player, "Jungle")
        pick_up_item(self.player)
        move_player(self.player, "Cave")
        pick_up_item(self.player)
        move_player(self.player, "Old Bridge")
        move_player(self.player, "Lighthouse")

        success, message = light_beacon(self.player)

        self.assertTrue(success)
        self.assertTrue(is_win(self.player))
        self.assertTrue(self.player["game_over"])

    def test_energy_exhaustion_causes_loss(self):
        move_player(self.player, "Jungle")
        move_player(self.player, "Beach")
        move_player(self.player, "Jungle")
        move_player(self.player, "Beach")
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_new_game_resets_inventory_and_energy(self):
        move_player(self.player, "Jungle")
        pick_up_item(self.player)

        another_player = new_game("Blessing")

        self.assertEqual(another_player["energy"], 5)
        self.assertEqual(another_player["location"], "Beach")
        self.assertEqual(another_player["inventory"], [])
        self.assertIsNot(self.player["inventory"],
                         another_player["inventory"])

    def test_player_cannot_move_after_game_over(self):
        self.player["game_over"] = True

        success, message = move_player(self.player, "Jungle")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")


if __name__ == "__main__":
    unittest.main()
