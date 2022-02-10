import time

# Twitch imports
import traceback
import logging
import logging.config
import concurrent.futures
import keyboard
import pyautogui

from chatplays.twitch.twitch_connection import Twitch
from chatplays.twitch.twitch_plays_account_info import TWITCH_USERNAME

# game imports, keeps this file clean, create more command sets as you have twitch-chat play more stuff
from chatplays.commandsets.command_set import CommandSet
from chatplays.games.gta import GTASimple, GTACrewed, GTAVIPMode  # one game three-profiles!
from chatplays.games.vampire_survivors import VampireSurvivors


from chatplays.inputs.directx import *
from chatplays.log.color_formatter import ColorFormatter

"""
Much of this code is based of the work DougDoug has done, except its been cleaned up a ton.

Load a game from chatplays.games.<yourgame> and set it in the init for ChatPlays
"""

MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20  # Note: setting to ~50 seems good for Mario Party. ~10 for platformers.
MAX_WORKERS = 1
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
pyautogui.FAILSAFE = False


class ChatPlays:
    def __init__(self):
        self.logger = self.setup_custom_logger("chat_plays")
        # Set the game you want to play here, one line change once you have made a command set
        self.game = VampireSurvivors()

    def main_loop(self):
        t = Twitch()
        t.twitch_connect(TWITCH_USERNAME)
        active_tasks = []
        message_queue = []
        last_time = time.time()

        while True:
            active_tasks = [t for t in active_tasks if not t.done()]

            # Check for new messages
            new_messages = t.twitch_receive_messages()
            if new_messages:
                message_queue += new_messages  # New messages are added to the back of the queue
                message_queue = message_queue[-MAX_QUEUE_LENGTH:]  # Shorten the queue to only the most recent X messages

            messages_to_handle = []
            if not message_queue:
                # No messages in the queue
                last_time = time.time()
            else:
                # Determine how many messages we should handle now
                r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                n = int(r * len(message_queue))
                if n > 0:
                    # Pop the messages we want off the front of the queue
                    messages_to_handle = message_queue[0:n]
                    del message_queue[0:n]
                    last_time = time.time()

            # If user presses Shift+Backspace, automatically end the program
            if keyboard.is_pressed('shift+backspace'):
                release_all_keys()  # Release all keys to prevent a key from being "stuck" held down
                exit()

            if not messages_to_handle:
                continue
            else:
                for message in messages_to_handle:
                    if len(active_tasks) <= MAX_WORKERS:
                        active_tasks.append(thread_pool.submit(self.handle_message, message))
                    else:
                        self.logger.warning(f'active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

    def handle_message(self, message):
        try:
            msg = message['message'].lower()
            username = message['username'].lower()
            self.logger.debug(f"USER: {username}, MSG: {msg}")
            self.game.process_message(msg, username)

        except Exception as e:
            traceback.print_tb()
            self.logger.exception("Encountered exception")

    @staticmethod
    def setup_custom_logger(name):
        formatter = ColorFormatter('%(levelname)s %(module)s %(message)s')

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger


def countdown(count: int = 5):
    """
    An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    TODO: Set the "countdown" variable to whatever countdown length you want.
    :param count: time in seconds to countdown, defaults to 5
    """
    while count > 0:
        print(count)
        count -= 1
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    countdown()
    ChatPlays().main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
