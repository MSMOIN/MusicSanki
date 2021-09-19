from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🎌𝗦𝗺𝗼𝗸𝗲𝗿 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗛𝗲𝗿𝗲\n🔈𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽 𝗛𝗲𝗹𝗽 - @Prayagraj_OP\n🌴𝗛𝗲𝘅𝗼𝗿𝘅𝗗 | 𝗦𝗺𝗼𝗸𝗲𝗿'𝘅𝗗")
  return                        
