# SOURCE https://github.com/Team-ProjectCodeX
# MODULE BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/ProjectCodeX


import requests
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from REPO import dispatcher

API_URL = "https://sugoi-api.vercel.app/search"


def bing_search(update: Update, context: CallbackContext):
    try:
        if len(context.args) == 0:
            update.message.reply_text("Please provide a keyword to search.")
            return

        keyword = " ".join(context.args)  # Assuming the keyword is passed as arguments
        params = {"keyword": keyword}
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                update.message.reply_text("No results found.")
            else:
                message = ""
                for result in results[:7]:
                    title = result.get("title", "")
                    link = result.get("link", "")
                    message += f"{title}\n{link}\n\n"
                update.message.reply_text(message.strip())
        else:
            update.message.reply_text("Sorry, something went wrong with the search.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")


# Add the command handler
dispatcher.add_handler(CommandHandler("bingsearch", bing_search))
