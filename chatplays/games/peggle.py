from chatplays.commandsets.command_set import VIPCommandSet, CommandSet
from chatplays.commandsets.mouse_commands import UP, DOWN, LEFT, RIGHT, LIGHT_RIGHT, LIGHT_LEFT, SHOOT, SHOOT_NOW


BASIC_COMMANDS = {
    "left": LEFT,
    "right": RIGHT,
    "up": UP,
    "down": DOWN,
    "light right": LIGHT_RIGHT,
    "light left": LIGHT_LEFT,
    "shoot": SHOOT_NOW
}

VIP_SHOOT = {
    "shoot!": SHOOT_NOW
}


class Peggle(CommandSet):
    """
    Peggle commands, moves the mouse around and shoot commands have a chance to shoot
    """

    @classmethod
    def command_list(cls):
        return BASIC_COMMANDS


class VipPeggle(VIPCommandSet):
    """
    Just like peggle, except vips can shoot right now
    """
    @classmethod
    def vip_list(cls):
        return ["squizgard"]

    @classmethod
    def general_commands(cls):
        return BASIC_COMMANDS | VIP_SHOOT

    @classmethod
    def vip_commands(cls):
        return BASIC_COMMANDS | VIP_SHOOT

