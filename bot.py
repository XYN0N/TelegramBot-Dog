#!/usr/bin/python
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
def bau(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
def main():
    updater = Updater('YOUR-TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bau',bau))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
