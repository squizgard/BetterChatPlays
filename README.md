# BetterChatPlays
A Chat Plays Python Project

## Supported Streaming Services
As of right now we only support Twitch, but believe its possible to support Youtube / Facebook

## Getting Started - Twitch
You'll find a file in `chatplays/twitch/twitch_plays_account_info.py` update line `#6` with the channel from which you 
want this script to read chat input from. BetterChatPlays logs in annonymously to twitch and does not need a password
to read any of the chat inputs.

## Playing a Game with BetterChatPlays
Prebuilt game commands can be found in `chatplays/games`. In the initial release there's not a ton here, but more will
likely be added.

### Telling BetterChatPlays which game to run
`main.py` at the root of this project is where you'll set which game will be played. 

#### Importing the game into Main
There is a section near the top of the file with the comment `# game imports, keeps this file clean, create more command sets as you have twitch-chat play more stuff`
We'll add a new game here (if its already here, no need to do it).

For example if we want to play Peggle we'll add 
```python
# game imports, keeps this file clean, create more command sets as you have twitch-chat play more stuff
from chatplays.games.peggle import Peggle
```

#### Setting the Game to be ran
Now that we've imported the game into Main, we'll need the main file to load and run it. This is as simple as
changing `line 40` to point at the game you just imported.

```python
# Set the game you want to play here, one line change once you have made a command set
self.game = Peggle()
```

#### Running BetterChatPlays
You will need to have python 3.9 or newer installed. Get it from https://www.python.org/downloads/. Currently this project has not 
been built/tested for non IDE (such as PyCharm) users. However you can run `main.py` from command line or directly in your IDE

TODO Add a tutorial on how to run / add new games / add custom commands

## Building your own commands
Commands for each game are defined in a map of `Command` objects with keys. These keys are the command words/phrases chat will
need to enter to use the command. For example:

```python
BASIC_COMMANDS = {
    "left": LEFT,
    "right": RIGHT,
    "up": UP,
    "down": DOWN,
    "light right": LIGHT_RIGHT,
    "light left": LIGHT_LEFT,
    "shoot": SHOOT_NOW
}
```
The phrases in `"quotation marks"` are the commands chat needs to enter, every thing left of the colon `:` is the python 'macro'
command that will be ran. The command definitions of the right are lifted directly from `mouse_commands.py` 

### Super Basic Custom Command
```python
import pyautogui # Mouse Commands
from chatplays.commandsets.keyboard_commands import * # imports ALL keyboard inputs

from chatplays.commandsets.command import Command

class CustomClick(Command):
    """
    Clicks the mouse
    """
    def __init__(self):
        super().__init__(pyautogui.click, [])
```

### Command Types and in-depth usage
In the `command.py` file you can find all of the pre-defined command types. These are not pre-built helper commands, but
are essentially template commands. 

#### Command
All command objects have two functions that are of interest. 

* `execute()` which simply executes the command object.
* `append()` appends another command to this command. Allows for command such as hold left and jump

#### Chance Command
A command that has an 1 in X chance of actually running. Contains all functionality as Command.

### Combining Multiple Sets of Commands
Lets say that you have a small set of really common commands named `BASIC_COMMNDS`, and you have a set of game specific commands you want combine with them.
Here's how you can do without redefining each command.
```python
# BASIC_COMMANDS from above
BASIC_COMMANDS = {
    ...
}
GAME_SPECIFIC_COMMANDS = {
    "Custom Command" : CustomClick(), # CustomClick from above
    "Another one": AnotherCustomCommand()
}
# Combine them, this only works thanks to python 3.9+
COMBINED_COMMANDS = BASIC_COMMANDS | GAME_SPECIFIC_COMMANDS
```

## Building your own game command set
All 'Games' in BetterChatPlays are instances of `CommandSet`. CommandSet is the class that contains logic to process your 
users commands and check if the command exists in the Map of commands.

### Basic Game Command Set Foundation
```python
"""
Defining the Basic set of commands for your Game
"""
BASIC_COMMANDS = {
    "left": LEFT,
    "right": RIGHT,
    "up": UP,
    "down": DOWN,
    "light right": LIGHT_RIGHT,
    "light left": LIGHT_LEFT,
    "shoot": SHOOT_NOW
}

class GTASimple(CommandSet):
    """
    Basic command set, build a list of commands and the base class (CommandSet) will run them
    """

    @classmethod
    def command_list(cls):
        # No more if-else statements to write, just the name and the inputs you want to run.
        # See command.py for a detailed explanation of how this works
        return BASIC_COMMANDS

# If you play the same game a lot with different commands, you can create multiple CommandSets in the same file
class GTAModMenuControl(CommandSet):
    """
    Basic command set, build a list of commands and the base class (CommandSet) will run them
    """

    @classmethod
    def command_list(cls):
        # No more if-else statements to write, just the name and the inputs you want to run.
        # See command.py for a detailed explanation of how this works
        return MENU_COMMANDS
```

#### Command Set Types
These are the underlying structures to every game that will be ran. 

* `CommandSet` Basic CommandSet that all CommandSets extend from. Has a list to return the Commands to run, and functionality to process them
* `CrewCommandSet` Inspired from DougDoug's A-Crew and Z-Crew battles. Has a command set for users in the first half of the Alphabet, and another for the second half.
* `VIPCommandSet` Lets you define a specific set of users w/ their own set of commands