"""Core rules and state management for Mystery Island."""

LOCATIONS = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"],
}

ITEMS_AT_LOCATION = {
    "Jungle": "rope",
    "Cave": "lantern",
}


def new_game(name):
    """Create a fresh player state."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
        "quit": False,
    }


def available_destinations(player):
    """Return locations the player can move to."""
    return LOCATIONS.get(player["location"], []).copy()


def move_player(player, destination):
    """Move the player if the destination is legal."""
    if player["game_over"]:
        return False, "The game has already ended."

    if destination not in available_destinations(player):
        return False, "You cannot move there from here."

    if destination == "Old Bridge" and "rope" not in player["inventory"]:
        return False, "You need a rope to cross the old bridge."

    player["location"] = destination
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        return True, "You have run out of energy. Rescue never arrived!"

    return True, f"You moved to {destination}."


def pick_up_item(player):
    """Collect the item available at the current location."""
    if player["game_over"]:
        return False, "The game has already ended."

    item = ITEMS_AT_LOCATION.get(player["location"])

    if item is None:
        return False, "There is nothing useful to collect here."

    if item in player["inventory"]:
        return False, f"You already have the {item}."

    player["inventory"].append(item)
    return True, f"You collected the {item}!"


def show_inventory(player):
    """Return a readable inventory description."""
    if not player["inventory"]:
        return "Your inventory is empty."

    return "Your inventory: " + ", ".join(player["inventory"])


def light_beacon(player):
    """Light the lighthouse beacon when requirements are met."""
    if player["game_over"]:
        return False, "The game has already ended."

    if player["location"] != "Lighthouse":
        return False, "You must reach the Lighthouse first."

    if "lantern" not in player["inventory"]:
        return False, "You need a lantern to light the beacon."

    if player["energy"] <= 0:
        return False, "You have no energy left to light the beacon."

    player["won"] = True
    player["game_over"] = True

    return True, "The lighthouse beacon shines! The rescue boat sees you!"


def quit_game(player):
    """End the game when the player chooses to quit."""
    if player["game_over"]:
        return False, "The game has already ended."

    player["quit"] = True
    player["game_over"] = True
    return True, "You decided to leave the island adventure."


def is_win(player):
    """Check whether the player has won."""
    return player["won"]
