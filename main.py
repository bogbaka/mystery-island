"""Command-line interface for The Lost Lighthouse."""

from game import (
    new_game,
    available_destinations,
    move_player,
    pick_up_item,
    show_inventory,
    light_beacon,
    quit_game,
)


def show_intro():
    """Display the game introduction."""
    print("\n" + "=" * 40)
    print("          THE LOST LIGHTHOUSE")
    print("=" * 40)
    print("\nA terrible storm has left you stranded on Mystery Island.")
    print("The lighthouse is dark, and a rescue boat is coming.")
    print("Find the necessary objects and restore the beacon.")
    print("\nYou start with 5 energy points.")
    print("Every successful move costs 1 energy point.")
    print("Collect a rope and a lantern to escape!")


def show_status(player):
    """Display the player's current status."""
    print("\n" + "-" * 40)
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print("-" * 40)


def show_menu():
    """Display the available game actions."""
    print("\nWhat would you like to do?")
    print("1. Move to another location")
    print("2. Collect an item")
    print("3. Check inventory")
    print("4. Light the lighthouse beacon")
    print("5. Quit game")


def play_game(name):
    """Run one complete game."""
    player = new_game(name)

    print(f"\nWelcome, {name}! Your adventure begins at the Beach.")

    while not player["game_over"]:
        show_status(player)
        show_menu()

        choice = input("\nEnter your choice: ").strip().lower()

        if choice in ("1", "move"):
            destinations = available_destinations(player)

            print("\nAvailable destinations:")
            for destination in destinations:
                print(f"- {destination}")

            destination = input("Where would you like to go? ").strip().title()

            success, message = move_player(player, destination)
            print(message)

        elif choice in ("2", "collect", "pickup"):
            success, message = pick_up_item(player)
            print(message)

        elif choice in ("3", "inventory"):
            print(show_inventory(player))

        elif choice in ("4", "light"):
            success, message = light_beacon(player)
            print(message)

        elif choice in ("5", "q", "quit", "exit"):
            success, message = quit_game(player)
            print(message)

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    if player["won"]:
        print("\n" + "=" * 40)
        print(f"CONGRATULATIONS, {name.upper()}!")
        print("YOU RESTORED THE LIGHTHOUSE AND ESCAPED!")
        print("=" * 40)

    elif not player["quit"]:
        print("\nGAME OVER! You did not escape Mystery Island.")

    return player


def main():
    """Start the game and handle replay."""
    show_intro()

    name = input("\nWhat is your name? ").strip()

    if not name:
        name = "Explorer"

    while True:
        play_game(name)

        while True:
            replay = input("\nWould you like to play again? (yes/no): ")
            replay = replay.strip().lower()

            if replay in ("yes", "y"):
                print("\nStarting a new adventure!")
                break

            if replay in ("no", "n"):
                print("\nThank you for playing The Lost Lighthouse!")
                return

            print("Please enter yes or no.")


if __name__ == "__main__":
    main()
