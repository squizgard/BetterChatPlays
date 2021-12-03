import logging
from random import randint
from typing import Callable

LOGGER = logging.getLogger('chat_plays')


class Command:
    """
    Simple command structure to be stuffed into a command info entry. No name of the command is stored here for
    space/speed efficiency

    NEAT STUFF:
    Literally accepts any function and arguments for that function to be called when the user wants to run this command

    Create a basic version of a command like:

        Command(press_and_hold_key, [W, 0.1])
               ^                     ^
               function name         function arguments in a tuple

    Presses the W key for 0.1 Second.

    If you want to do more cool stuff after that just append it! Keep appending
    as many additional functions as you want

        Command(press_and_hold_key, [D, 0.1]).append(press_and_hold_key, [O, 0.1])\
                      .append(press_and_hold_key, [U, 0.1]).append(press_and_hold_key, [G, 0.1])

    Presses the D, O, U, G each for 0.1 seconds in the order they were appended.

    You aren't restricted to inputs either. You can call ANY function with ANY args

    """

    def __init__(self, f: Callable, f_args):
        """
        Initializes the command with the first command to run and the args for it
        :param f: function to call
        :param f_args: args for the function
        """
        self.funcs = [[f, f_args]]

    def append(self, f: Callable, f_args):
        """
        Appends a new function to call to the end of the list of functions to run
        :param f: function to append
        :param f_args: args for this function
        :return: itself so you can keep appending
        """
        self.funcs.append([f, f_args])
        return self

    def execute(self):
        """
        Executes the command(s) that were provided
        """
        for f, args in self.funcs:
            LOGGER.debug(f"Running command {f.__name__} with args {str(args)}")
            f(*args)


class ChanceCommand(Command):
    def __init__(self, chance: int, f: Callable, f_args):
        """
        Initializes the command with the first command to run and the args for it
        :param chance: int to set "one in X" chance to do this command. set to 25 for 1 in 25 chance to do it
        :param f: function to call
        :param f_args: args for the function
        """
        super().__init__(f, f_args)
        self.chance = chance

    def execute(self):
        """
        Executes the command(s) that were provided
        """
        if randint(1, self.chance) == 1:
            super().execute()
