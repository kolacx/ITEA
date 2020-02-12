import global_settings

def start_bot():
    if global_settings.DEBUG == True:
        bot.poling()
    else:
        import time
        print('STARTED')
        bot.remove_webhook()
        time.sleep(1)
        bot.set_webhook(
            url=WEBHOOK_URL,
            certificate=open('nginx-selfsigned.crt', 'r')
            )
        app.run(host='127.0.0.1', port=5000, debug=True)