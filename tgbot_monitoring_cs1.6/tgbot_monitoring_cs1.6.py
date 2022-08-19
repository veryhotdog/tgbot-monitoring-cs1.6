import telebot
import time
import a2s

#configurations-----------------------------------------------------------------------------------------------------------------------------------

BOT_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" # Your bot's token
SERVER_IP = "127.0.0.1" #IP of your game server
SERVER_PORT = 27015 # Port of your game server
ERROR_REPLY = "Технические неполадки. Попробуй. Ещё. Раз." #Reply in case of an unexpected error
IMAGE_ID = "AgACAgIAAxkBAAIGjWL_4mQSvzxjAXQ5bd_ZPM1_rqiMAALIvjEbycHZSvNZ6nnYZNfaAQADAgADeAADKQQ"    #Image which will be attached to the message.

#------------------------------------------------------------------------------------------------------------------------------------------------

bot = telebot.TeleBot(BOT_TOKEN, parse_mode = None, threaded=False)

@bot.message_handler(commands=['start'])
def command_start(message):
    reply = "Hello."
    bot.send_message(message.from_user.id, reply, parse_mode="HTML")
    return

@bot.message_handler(commands=['mon'])
def command_mon(message):
    try:
        Players = a2s.players((SERVER_IP, SERVER_PORT))
        Info = a2s.info((SERVER_IP, SERVER_PORT))
        
        serverAddress = SERVER_IP + ":" + str(SERVER_PORT)
        mapName = Info.map_name
        playersNum = Info.player_count
        playersMax = Info.max_players
        
        reply = "<b>" + serverAddress + "</b>\nИгроков: " + str(playersNum) + "/" + str(playersMax) + "\nКарта: " + mapName + "\n\n<b>Игроки:\n\n"
        for Player in Players:
            playerId = Player.index + 1
            playerName = escape_string(Player.name)
            reply = reply + str(playerId) + ". " + playerName + "\n"
        reply = reply + "</b>"
        bot.send_photo(message.from_user.id, IMAGE_ID, reply, parse_mode="HTML")
        
        return
    except Exception as e:
        bot.send_message(message.from_user.id, ERROR_REPLY, parse_mode="HTML")
        print("[TGBOT] def_command_mon error: {}".format(e))
        return
        
def escape_string(str):
    str = str.replace("<","&lt;")
    str = str.replace(">","&gt;")

    return str

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("[TGBOT] bot.polling error: {}".format(e))
        time.sleep(15)