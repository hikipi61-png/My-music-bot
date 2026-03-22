from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

# --- TERI DETAILS ---
API_ID = 36921502
API_HASH = "e10ffdde65e2b860ff30596606c36987"
BOT_TOKEN = "8338511426:AAGwRNUSQBMs_YbMEh8wjNlls_V7ZA0A81o"
ADMIN_ID = 8154922225 
# --------------------

app = Client("raj_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🔥 @RAJBOTSx Music Bot Live on Render!")

@app.on_message(filters.command("play") & filters.user(ADMIN_ID))
async def play(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply("Audio pe reply kar bhai!")
    path = await message.reply_to_message.download()
    try:
        await call_py.play(message.chat.id, AudioPiped(path))
        await message.reply(f"🎶 Playing: {message.reply_to_message.audio.title}")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

app.run()
