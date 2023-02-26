#basya54
import telebot
import random

bot = telebot.TeleBot('6080271213:AAEtsO6uWgkp5hCFOVgDfe8GGWAV_xPHbmY')

@bot.message_handler(commands = ['start'])
def start(message):
    Mess = 'Are you ready to test who are you?\nThen enter the command "/go"'
    bot.send_message(message.chat.id, Mess)
    
#Тут можна вписати людей яким напише що вони боти. Це кортеж, тому без квадратних і круглих дужок
Username = 'aFlowernamedYOU', 'l1stocek', 'mayjuline','Mak7_official','Agjhdudh'

@bot.message_handler(commands = ['go'])
def BotTest(message):
    #беру id особи перший раз, і перевіряю чи нема його в file
    person_id = str(message.from_user.id)
    file = open('liste.txt', 'r')
    person_id_list = file.read()
    file.close()
    Status = message.from_user.is_bot
    Username_this_person = message.from_user.username
    if person_id not in person_id_list:
        #тепер записую id в файл, щоб наступного разу особа не змогла виконати команду 
        file1 = open('liste.txt', 'a')
        file1.write(', ' + person_id)
        file1.close()
        #рандом щоб інколи писало що він бот, якщо він не бот
        Random_number = random.randint(1, 6)
        Mess = 'You are a bot, colleague :). And what is your role?'
        # Status показує чи є особа ботом. Від цього залежить відповідь
        if Status == True:
            bot.send_message(message.chat.id, Mess)
        elif ((Username_this_person in Username) or Random_number == 2) and Status == False:
            bot.send_message(message.chat.id, Mess)
        else:
            bot.send_message(message.chat.id, 'You are not a bot. Congratulations!')
    else:
        bot.send_message(message.chat.id, 'You had one try. Sorry')
        
bot.infinity_polling(none_stop = True)
