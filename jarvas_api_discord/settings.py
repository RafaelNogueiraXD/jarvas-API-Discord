from dotenv import load_dotenv
import os
def load_config_bot_token():
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    return bot_token

def load_config_general_id_channel():
    load_dotenv()
    app_id = os.getenv('GENEREAL_CHANNEL_ID')
    return app_id
