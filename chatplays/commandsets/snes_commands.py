from enum import Enum, unique

from chatplays.commandsets.command import Command, ChanceCommand
from chatplays.inputs.snes import *


@unique
class SimpleSNESButtons(Enum):
    SNES_P1_UP = V
    SNES_P1_DOWN = B
    SNES_P1_LEFT = N
    SNES_P1_RIGHT = M
    SNES_P1_A = X
    SNES_P1_B = Z
    SNES_P1_L = Q
    SNES_P1_R = E
    SNES_P1_X = C
    SNES_P1_Y = R
    SNES_P1_START = ENTER
    SNES_P1_SELECT = RIGHT_SHIFT
    SNES_P2_UP = I
    SNES_P2_DOWN = K
    SNES_P2_LEFT = J
    SNES_P2_RIGHT = L
    SNES_P2_A = G
    SNES_P2_B = F
    SNES_P2_L = O
    SNES_P2_R = P
    SNES_P2_X = T
    SNES_P2_Y = H
    SNES_P2_START = SEMICOLON

    def press(self):
        Command(press_and_hold_key, [self.value, 0.1]).execute()


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

