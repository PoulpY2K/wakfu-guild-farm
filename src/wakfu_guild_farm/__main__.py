import logging

from wakfu_guild_farm.actions import focus_wakfu, interact, press_key, finish_battle, interact_button, Click
from wakfu_guild_farm.constants import RIGHT_CLICK_HOLE_X, RIGHT_CLICK_HOLE_Y, LEFT_CLICK_HOLE_X, LEFT_CLICK_HOLE_Y, \
    RIGHT_CLICK_LARVAE_X, RIGHT_CLICK_LARVAE_Y, LEFT_CLICK_LARVAE_X, LEFT_CLICK_LARVAE_Y, \
    LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, \
    LEFT_CLICK_BATTLE_FIRST_LARVAE_X, LEFT_CLICK_BATTLE_FIRST_LARVAE_Y, \
    LEFT_CLICK_BATTLE_SECOND_LARVAE_X, LEFT_CLICK_BATTLE_SECOND_LARVAE_Y, \
    LEFT_CLICK_OUT_X, LEFT_CLICK_OUT_Y

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('main')


def enter_and_fight():
    interact_button(RIGHT_CLICK_HOLE_X, RIGHT_CLICK_HOLE_Y, LEFT_CLICK_HOLE_X, LEFT_CLICK_HOLE_Y, 2)
    interact_button(RIGHT_CLICK_LARVAE_X, RIGHT_CLICK_LARVAE_Y, LEFT_CLICK_LARVAE_X, LEFT_CLICK_LARVAE_Y, 3.5)


def fight_larvae():
    interact(Click.LEFT_CLICK, LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, 0.1)
    interact(Click.LEFT_CLICK, LEFT_CLICK_BATTLE_FIRST_LARVAE_X, LEFT_CLICK_BATTLE_FIRST_LARVAE_Y, 0.1)
    interact(Click.LEFT_CLICK, LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, 0.1)
    interact(Click.LEFT_CLICK, LEFT_CLICK_BATTLE_SECOND_LARVAE_X, LEFT_CLICK_BATTLE_SECOND_LARVAE_Y, 2.5)


class WakfuGuildClient:
    def __init__(self):
        self.running = False
        self.count = 0

    def start(self):
        logger.info("Starting WakfuGuildClient...")
        focus_wakfu()
        self.running = True
        while self.running:
            self.count += 1
            logger.info("WakfuGuildClient is running iteration %d", self.count)
            enter_and_fight()
            logger.info("Entered hole and entered combat")
            press_key("space", 1)
            logger.info("Pressed space to start combat")
            fight_larvae()
            logger.info("Successfully fought larvaes")
            finish_battle(LEFT_CLICK_OUT_X, LEFT_CLICK_OUT_Y, 3)
            logger.info("Left the hole after battle and starting again")

    def stop(self):
        logger.info("Wakfu server is stopping...")
        self.running = False

def run():
    wakfu_guild_client = WakfuGuildClient()
    try:
        wakfu_guild_client.start()
    except KeyboardInterrupt:
        wakfu_guild_client.stop()
        logger.info("Client stopped by user")
    except Exception as e:
        wakfu_guild_client.stop()
        logger.error(f"Unexpected error: {e}")