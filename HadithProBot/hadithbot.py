from bukhari import *
from abuDaud import *
from ibnemajah import *
from muslim import *
from nasai import *
from tirmidhi import *
import requests
from telegram import *
from telegram.ext import *
# Bukhari = bukharihadith  # dictionary
# Abudaud = abudaudhadith  # dictionary
# Ibnemajah = ibnemajahhadith  # dictionary
# Muslim = muslimhadith  # dictionary
# Nasai = nasaihadith  # dictionary
# Tirmidhi = tirmidhihadith  # dictionary
token = "5758442510:AAF7VsxBY6I_QOrdpT4IlvlsHla09OydL7U"  # token of hadithPro bot
updater = Updater(token, use_context=True)
# global main_api_link


def start(update, context):
    update.message.reply_text('''
    press /help to show all commands
    ''')


def help(update, context):
    update.message.reply_text('''
    /custom --> to custom ur own hadith
    /start --> to know about things
    /contact --> minhazrahman1010@gmail.com
    /abudaud 
    /bukhari
    /muslim
    /nasai
    /ibnemajah
    /tirmidhi
    ''')


# def abudawud(update, context):
#     update.message.reply_text(abudaudhadith1)
#     update.message.reply_text(abudaudhadith2)
#     update.message.reply_text(f'''
#         Total chapter is 1 to 43,
# Please choose any of them
#     ''')
#     text = update.message.text
#     text = text.replace('/', '')
#     print(text)
#     Return = selecthadith(text)
#     update.message.reply_text(f"{Return}")

def abudawud(update, context):
    update.message.reply_text(abudaudhadith1)
    update.message.reply_text(abudaudhadith2)
    update.message.reply_text(f'''
        Total chapter is 1 to 43,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    Return = selecthadith(update, text)
    update.message.reply_text(f"{Return}")


def bukhari(update, context):
    update.message.reply_text(bukharihadith2)
    update.message.reply_text(bukharihadith3)
    update.message.reply_text(f'''
        Total chapter is 1 to 97,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    Return = selecthadith(text)
    update.message.reply_text(f"{Return}")


def muslim(update, context):
    update.message.reply_text(muslimhadith1)
    update.message.reply_text(muslimhadith2)
    update.message.reply_text(f'''
        Total chapter is 1 to 56,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    Return = selecthadith(text)
    update.message.reply_text(Return)


def ibnemajah(update, context):
    update.message.reply_text(ibnemajahhadith1)
    update.message.reply_text(ibnemajahhadith2)
    update.message.reply_text(f'''
        Total chapter is 1 to 37,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    Return = selecthadith(text)
    update.message.reply_text(Return)


def nasai(update, context):
    update.message.reply_text(nasaihadith1)
    update.message.reply_text(nasaihadith2)
    update.message.reply_text(f'''
        Total chapter is 1 to 51,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    Return = selecthadith(text)
    update.message.reply_text(Return)


# def tirmidhi(update, context):
#     update.message.reply_text(tirmidhihadith1)
#     update.message.reply_text(tirmidhihadith2)
#     update.message.reply_text(f'''
#         Total chapter is 1 to 49,
# Please choose any of them
#     ''')
#     text = update.message.text
#     text = text.replace('/', '')
#     print(text)
#     text2 = str(text)
#     Return = selecthadith(text2)
#     tirmidhi2(Return)
i = int(0)


def tirmidhi(update, context):
    update.message.reply_text(tirmidhihadith1)
    update.message.reply_text(tirmidhihadith2)
    update.message.reply_text(f'''
        Total chapter is 1 to 49,
Please choose any of them
    ''')
    text = update.message.text
    text = text.replace('/', '')
    print(text)
    text2 = str(text)
    Return = selecthadith(text2)


list2 = []


def tirmidhi2(x):
    list2.append(x)
    print(list2)

# def proxy1(text):
#     x = ''.join(text)
#     # selecthadith(x)


def reply(update, context):
    text = update.message.text
    text2 = str(text)
    Return = selecthadith(text2)

    # print(text)
    # proxy1(text)


list1 = []


async def selecthadith(update, x):
    link = x
    list1.append(link)
    # print(list1)

    # # ben-{book}/{hadith_No}
    # main_api_link_boss = f"https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/ben-bukhari/39.json"
    if len(list1) == 1:
        vejal = str(list1[0])
        global main_api_link
        main_api_link = f"https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/ben-{vejal}/"
    #   print(main_api_link)
    if len(list1) == 2:
        vejal = str(list1[1])
        main_link = f"{main_api_link}{vejal}.json"
        # print(main_link)
        # print(main_link==main_api_link_boss)
        api_link = requests.get(main_link)
        api_data = api_link.json()
        # return api_data['hadiths'][0]['text']
        x = api_data['hadiths'][0]['text']


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('abudaud', abudawud))
updater.dispatcher.add_handler(CommandHandler('bukhari', bukhari))
updater.dispatcher.add_handler(CommandHandler('ibnemajah', ibnemajah))
updater.dispatcher.add_handler(CommandHandler('muslim', muslim))
updater.dispatcher.add_handler(CommandHandler('nasai', nasai))
updater.dispatcher.add_handler(CommandHandler('tirmidhi', tirmidhi))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()
