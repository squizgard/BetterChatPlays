import pyautogui

from chatplays.commandsets.command import Command, ChanceCommand


class MouseDown(Command):
    """
    Moves the mouse down 5 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [0, 5])


class MouseUp(Command):
    """
    Moves the mouse up 5 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [0, -5])


class MouseLeft(Command):
    """
    Moves the Mouse left 15 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [-15, 0])


class MouseRight(Command):
    """
    Moves the mouse right 15 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [15, 0])


class MouseLightLeft(Command):
    """
    Moves the mouse left 5 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [-5, 0])


class MouseLightRight(Command):
    """
    Moves the mouse right 5 units
    """
    def __init__(self):
        super().__init__(pyautogui.move, [5, 0])


class Click(Command):
    """
    Clicks the mouse
    """
    def __init__(self):
        super().__init__(pyautogui.click, [])


class ClickChance(ChanceCommand):
    """
    1 in 50 chance to click the mouse
    """
    def __init__(self):
        super().__init__(50, pyautogui.click, [])


DOWN = MouseDown()
UP = MouseUp()
LEFT = MouseLeft()
RIGHT = MouseRight()
LIGHT_LEFT = MouseLightLeft()
LIGHT_RIGHT = MouseLightRight()
SHOOT_NOW = Click()
SHOOT = ClickChance()
