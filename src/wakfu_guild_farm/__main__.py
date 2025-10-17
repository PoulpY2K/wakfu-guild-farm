import asyncio
import json
import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('main')

class WakfuGuildClient:
    def __init__(self):
        self.running = False

    async def start(self):
        logger.info("Starting WakfuGuildClient...")
        self.running = True
        while self.running:
            logger.info("WakfuGuildClient is running...")
            await asyncio.sleep(5)  # Simulate server activity

    def stop(self):
        self.running = False
        logger.info("Wakfu server is stopping...")

def run():
    wakfu_guild_client = WakfuGuildClient()
    try:
        asyncio.run(wakfu_guild_client.start())
    except KeyboardInterrupt:
        wakfu_guild_client.stop()
        logger.info("Server stopped by user")
    except Exception as e:
        wakfu_guild_client.stop()
        logger.error(f"Unexpected error: {e}")