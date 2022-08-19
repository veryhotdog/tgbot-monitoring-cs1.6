# tgbot-monitoring-cs1.6
Simple Telegram Bot that sends Counter-Strike 1.6 server's monitoring
# REQUIREMENTS
You need to install python-a2s and pyTelegramBotAPI libraries:

https://github.com/Yepoleb/python-a2s<br />
https://pytba.readthedocs.io/en/latest/install.html
# USING
1. Change the block with configurations to your data in programm source:
    ```python
    #configurations----------------------------------------------------------------------------------------------------------------------------------

    BOT_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" # Your bot's token
    SERVER_IP = "127.0.0.1" #IP of your game server
    SERVER_PORT = 27015 # Port of your game server
    ERROR_REPLY = "Технические неполадки. Попробуй. Ещё. Раз." #Reply in case of an unexpected error
    IMAGE_ID = "AgACAgIAAxkBAAIGjWL_4mQSvzxjAXQ5bd_ZPM1_rqiMAALIvjEbycHZSvNZ6nnYZNfaAQADAgADeAADKQQ"    #Image which will be attached to the message.

    #------------------------------------------------------------------------------------------------------------------------------------------------
    ```
2. Add the /mon command for your bot with @BotFather
3. Run the programm. Bot should work :)
