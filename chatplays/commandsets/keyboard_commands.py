from command import Command, ChanceCommand
from chatplays.inputs.directx import *


class Tap(Command):
    """
    Taps a single button for a provided duration, default duration is 0.1 seconds
    """
    def __init__(self, keycode: int, duration: float = 0.1):
        super().__init__(press_and_hold_key, [keycode, duration])


class Rump(Command):
    """
    "Right Jump" Useful for platformer games where you need to be moving and jumping at the same time.
    Holds down the right key and jumps, after the jump releases the right key
    """
    def __init__(self):
        super().__init__(press_key_pynput, [RIGHT_ARROW])
        self.append(press_key_pynput, [A, 0.2])
        self.append(release_key_pynput, [RIGHT_ARROW])


class Lump(Command):
    """
    "Right Jump" Useful for platformer games where you need to be moving and jumping at the same time.
    Holds down the left key and jumps, after the jump releases the left key
    """
    def __init__(self):
        super().__init__(press_key_pynput, [LEFT_ARROW])
        self.append(press_key_pynput, [A, 0.2])
        self.append(release_key_pynput, [LEFT_ARROW])

