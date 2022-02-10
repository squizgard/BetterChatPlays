from chatplays.commandsets.command import  Command, ChanceCommand
from chatplays.inputs.directx import *


class Tap(Command):
    """
    Taps a single button for a provided duration, default duration is 0.1 seconds
    """
    def __init__(self, keycode: int, duration: float = 0.1):
        super().__init__(press_and_hold_key, [keycode, duration])


class ChanceTap(ChanceCommand):
    """
    Taps a single button for a provided duration, default duration is 0.1 seconds
    """
    def __init__(self, chance: int, keycode: int, duration: float = 0.1):
        super().__init__(chance, press_and_hold_key, [keycode, duration])


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


class LightW(Tap):
    def __init__(self):
        super(LightW, self ).__init__(W)


class LightA(Tap):
    def __init__(self):
        super(LightA, self ).__init__(A)


class LightS(Tap):
    def __init__(self):
        super(LightS, self ).__init__(S)


class LightD(Tap):
    def __init__(self):
        super(LightD, self ).__init__(D)


class MediumW(Tap):
    def __init__(self):
        super(MediumW, self).__init__(W, 0.5)


class MediumA(Tap):
    def __init__(self):
        super(MediumA, self).__init__(A, 0.5)


class MediumS(Tap):
    def __init__(self):
        super(MediumS, self).__init__(S, 0.5)


class MediumD(Tap):
    def __init__(self):
        super(MediumD, self).__init__(D, 0.5)


class LongW(Tap):
    def __init__(self):
        super(LongW, self).__init__(W, 0.75)


class LongA(Tap):
    def __init__(self):
        super(LongA, self).__init__(A, 0.75)


class LongS(Tap):
    def __init__(self):
        super(LongS, self).__init__(S, 0.75)


class LongD(Tap):
    def __init__(self):
        super(LongD, self).__init__(D, 0.75)
