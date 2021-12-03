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
command that will be ran. 

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

### Combining Multiple Sets of Commands
Lets say that you have a small set of really command commands named `COMMON_COMMNDS`, and you have a set of game specific commands you want combine with them.
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

## TODO Building your own game command set
Need to add this, but there is are working examples in `chatplays/games/`
