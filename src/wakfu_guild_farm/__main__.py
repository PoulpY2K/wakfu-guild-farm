import asyncio
import json
import logging
import time
from datetime import datetime

import keyboard
import pyautogui
from wakfu_guild_farm.actions import focus_wakfu, interact, press_key, finish_battle, interact_button, Click
from wakfu_guild_farm.constants import RIGHT_CLICK_HOLE_X, RIGHT_CLICK_HOLE_Y, LEFT_CLICK_HOLE_X, LEFT_CLICK_HOLE_Y, \
    RIGHT_CLICK_LARVAE_X, RIGHT_CLICK_LARVAE_Y, LEFT_CLICK_LARVAE_X, LEFT_CLICK_LARVAE_Y, \
    LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, \
    LEFT_CLICK_BATTLE_FIRST_LARVAE_X, LEFT_CLICK_BATTLE_FIRST_LARVAE_Y, \
    LEFT_CLICK_BATTLE_SECOND_LARVAE_X, LEFT_CLICK_BATTLE_SECOND_LARVAE_Y, \
    LEFT_CLICK_OUT_X, LEFT_CLICK_OUT_Y

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('main')

class WakfuGuildClient:
    def __init__(self):
        self.running = False

    def start(self):
        logger.info("Starting WakfuGuildClient...")
        focus_wakfu()
        self.running = True
        while self.running:
            logger.info("WakfuGuildClient is running...")
            interact_button(RIGHT_CLICK_HOLE_X, RIGHT_CLICK_HOLE_Y, LEFT_CLICK_HOLE_X, LEFT_CLICK_HOLE_Y, 2)
            interact_button(RIGHT_CLICK_LARVAE_X, RIGHT_CLICK_LARVAE_Y, LEFT_CLICK_LARVAE_X, LEFT_CLICK_LARVAE_Y, 3.5)
            press_key("space", 1)
            interact(Click.LEFT_CLICK, LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, 0.1)
            interact(Click.LEFT_CLICK, LEFT_CLICK_BATTLE_FIRST_LARVAE_X, LEFT_CLICK_BATTLE_FIRST_LARVAE_Y, 0.1)
            interact(Click.LEFT_CLICK, LEFT_CLICK_SPELL_X, LEFT_CLICK_SPELL_Y, 0.1)
            interact(Click.LEFT_CLICK, LEFT_CLICK_BATTLE_SECOND_LARVAE_X, LEFT_CLICK_BATTLE_SECOND_LARVAE_Y, 2)
            finish_battle(LEFT_CLICK_OUT_X, LEFT_CLICK_OUT_Y, 3)

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