from chatplays.commandsets.command_set import CommandSet, CrewCommandSet, VIPCommandSet
from chatplays.commandsets.command import Command as cmd, ChanceCommand as chance
from chatplays.inputs.directx import * # TODO don't import *, but its late and im lazy

# TODO: Make GTA more playable, this barely lets users do anything
BASIC_COMMANDS = {
    "left": cmd(press_and_hold_key, [A, 0.2]),
    "right": cmd(press_and_hold_key, [D, 0.2]),
    "drive": cmd(release_key_pynput, [S]).append(press_key_pynput, [W]),
    "stop": cmd(release_key_pynput, [W]).append(press_key_pynput, [S]),
    "chance": chance(2, press_and_hold_key, [SPACE, 0.2])  # 1 in 2 chance to press space
}


MENU_COMMANDS = {
    # TODO import Function keys
    "menu 1": cmd(press_and_hold_key, [NUMPAD_0, 0.2]),
    "menu 2": cmd(press_and_hold_key, [NUMPAD_1, 0.2]),
}


class GTASimple(CommandSet):
    """
    Basic command set, build a list of commands and the base class (CommandSet) will run them
    """

    @classmethod
    def command_list(cls):
        # No more if-else statements to write, just the name and the inputs you want to run.
        # try not to run any thread sleeps here...code is currently single-threaded.
        # See command.py for a detailed explanation of how this works
        return BASIC_COMMANDS


class GTACrewed(CrewCommandSet):
    """
    Basic a-crew, z-crew command set, build a list of commands for each crew
    and the base class (CrewCommandSet) will run them
    """

    # DEVNOTE, completely unbiased opinion, A-crew smells like old cabbage
    @classmethod
    def a_crew_list(cls):
        return BASIC_COMMANDS

    # DEVNOTE GO Z-CREW!
    @classmethod
    def z_crew_list(cls):
        return MENU_COMMANDS


class GTAVIPMode(VIPCommandSet):
    @classmethod
    def general_commands(cls):
        return BASIC_COMMANDS

    @classmethod
    def vip_commands(cls):
        # How to merge command dictionaries easier (new in python 9)
        return BASIC_COMMANDS | MENU_COMMANDS

    @classmethod
    def vip_list(cls):
        return ["DougDougw", "VIP1"]
