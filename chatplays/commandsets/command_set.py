from abc import ABCMeta, abstractmethod
from typing import TypedDict
from chatplays.commandsets.command import Command
import logging

import string
FIRST_HALF_ALPHABET = list(string.ascii_lowercase)[:14]  # includes M, can't remember if it should or not
LAST_HALF_ALPHABET = list(string.ascii_lowercase)[14:]  # does not include M, change as needed

LOGGER = logging.getLogger("chat_plays")


class CommandInfo(TypedDict):
    """
    Helper class to enforce return types
    """
    name: str
    command: Command


class CommandSet(metaclass=ABCMeta):
    """
    Basic command set where all users are equal
    """

    def __init__(self):
        """
        Force init commands when you create this
        """
        self.commands = self.command_list()

    @classmethod
    @abstractmethod
    def command_list(cls):
        """
        This abstract method should return a dict of commands
        :rtype: CommandInfo
        """
        ...

    def process_message(self, msg: str, user: str):
        """
        Does the main work of running a users command
        :param msg: message to run
        :param user: the intelligent being that tried to run this
        """
        if msg in self.commands.keys():
            LOGGER.debug(f"{user} executed {msg}")
            self.commands[msg].execute()
        else:
            LOGGER.debug(f"command not found! {msg}")


class CrewCommandSet(metaclass=ABCMeta):
    """
    A simple a-crew, z-crew command set. Builds a set of commands for a-crew
    and z-crew separately if that's what you want
    """

    def __init__(self):
        """
        Force init some commands for each crew
        """
        self.a_crew = self.a_crew_list()
        self.z_crew = self.z_crew_list()

    def process_message(self, msg: str, user: str):
        """
        Runs the command for a given user based on crew
        :param msg: command to run
        :param user: user name
        """
        if user[0] in FIRST_HALF_ALPHABET:
            if msg in self.a_crew.keys():
                LOGGER.debug(f"{user} executed {msg}")
                self.a_crew[msg].execute()
            else:
                LOGGER.debug(f"command not found! {msg}")
        else:
            if msg in self.z_crew.keys():
                LOGGER.debug(f"{user} executed {msg}")
                self.z_crew[msg].execute()
            else:
                LOGGER.debug(f"command not found! {msg}")

    @classmethod
    @abstractmethod
    def a_crew_list(cls):
        """
        This abstract method should return a dict of commands
        :rtype: CommandInfo
        """
        ...

    @classmethod
    @abstractmethod
    def z_crew_list(cls):
        """
        This abstract method should return a dict of commands
        :rtype: CommandInfo
        """
        ...


class VIPCommandSet(metaclass=ABCMeta):
    """
    A simple command set where some users get different sets of commands based on vip status, VIPs dont automatically get
    non-vip role commands
    """

    def __init__(self):
        """
        Force init some commands for each crew
        """
        self.vips = self.vip_list()
        self.vip_command_set = self.vip_commands()
        self.general_command_set = self.general_commands()

    def process_message(self, msg: str, user: str):
        """
        Runs the command for a given user based on role
        :param msg: command to run
        :param user: user name
        """
        if user in self.vips:
            if msg in self.vip_command_set.keys():
                LOGGER.debug(f"{user} executed {msg}")
                self.vip_command_set[msg].execute()
            else:
                LOGGER.debug(f"command not found! {msg}")
        else:
            if msg in self.general_command_set.keys():
                LOGGER.debug(f"{user} executed {msg}")
                self.general_command_set[msg].execute()
            else:
                LOGGER.debug(f"command not found! {msg}")

    @classmethod
    @abstractmethod
    def vip_list(cls):
        """
        This abstract method should return a dict of commands
        :rtype: list [str]
        """
        ...

    @classmethod
    @abstractmethod
    def general_commands(cls):
        """
        This abstract method should return a dict of commands
        :rtype: CommandInfo
        """
        ...

    @classmethod
    @abstractmethod
    def vip_commands(cls):
        """
        This abstract method should return a dict of commands
        :rtype: CommandInfo
        """
        ...
