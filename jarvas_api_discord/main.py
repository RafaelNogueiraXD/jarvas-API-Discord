import discord
from jarvas_api_discord.settings import load_config_general_id_channel, load_config_bot_token
from fastapi import FastAPI, HTTPException
import asyncio


intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = int(load_config_general_id_channel())  # Carrega o ID do canal
        self.message_task = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def send_message(self, message: str):
        """Envia uma mensagem para o canal especificado."""
        await self.wait_until_ready()
        channel = self.get_channel(self.channel_id)
        if channel is None:
            print("Canal não encontrado. Verifique o ID.")
            return False
        await channel.send(message)
        return True


client = MyClient(intents=intents)
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """Inicia o bot Discord junto com a API."""
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(load_config_bot_token()))

@app.get("/")
async def send_discord_message():
    """Rota que envia uma mensagem para o canal Discord."""
    message = "Mensagem enviada via API HTTP!"
    success = await client.send_message(message)
    if not success:
        raise HTTPException(status_code=500, detail="Falha ao enviar mensagem.")
    return {"detail": "Mensagem enviada com sucesso!"}
