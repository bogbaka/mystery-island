# The Lost Lighthouse — Mystery Island

A beginner-friendly Python command-line adventure game.

## Project Description

The player is stranded on Mystery Island after a terrible storm. The goal is to collect the necessary items, reach the lighthouse, and light its beacon before running out of energy.

## Requirements

- Python 3.8 or newer
- No external Python packages required

## How to Run

Open a terminal in the project directory and run:

```bash
python3 main.py
```

## How to Play

You start at the Beach with 5 energy points.

Choose from the following actions:

1. Move to another location.
2. Collect an item.
3. Check your inventory.
4. Light the lighthouse beacon.
5. Quit the game.

## Locations and Items

| Location | Description |
|---|---|
| Beach | Starting location |
| Jungle | Contains the rope |
| Cave | Contains the lantern |
| Old Bridge | Requires the rope |
| Lighthouse | Final destination |

## Game Rules

- Every successful movement costs 1 energy point.
- Invalid movements do not consume energy.
- Collecting items does not consume energy.
- Each item can only be collected once.
- The rope is required to cross the Old Bridge.
- The lantern is required to light the beacon.
- The player wins by lighting the beacon with energy remaining.
- The player loses when energy reaches zero.
- The player can quit or start a new adventure.

## Example Winning Route

1. Beach to Jungle.
2. Collect the rope.
3. Jungle to Cave.
4. Collect the lantern.
5. Cave to Old Bridge.
6. Old Bridge to Lighthouse.
7. Light the beacon.

The player wins with 1 energy point remaining.

## Running Tests

Run the automated tests using:

```bash
python3 -m unittest discover -s tests -v
```

The test suite checks game initialization, movement, inventory, item requirements, energy exhaustion, winning and game-over behaviour.

## Project Structure

```text
mystery-island/
├── main.py
├── game.py
├── README.md
├── .gitignore
└── tests/
    ├── __init__.py
    └── test_game.py
```

## Known Limitations

- The game uses a text-based terminal interface.
- There is no graphical interface or sound.
- Game progress is not saved after exiting.
- The game uses fixed locations and rules.
