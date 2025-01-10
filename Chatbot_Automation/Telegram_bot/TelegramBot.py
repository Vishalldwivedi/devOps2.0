from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import json

# Replace TOKEN with your actual bot token
TOKEN = '7884899105:AAEVQD_bLzpp4gEieZcTHWRAsrEItVsa0_g'

# Create the bot instance
bot = Bot(token=TOKEN)

# Initialize the application
application = ApplicationBuilder().token(TOKEN).build()


# Command: /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, This is a telegram bot')


# Command: /summary (Fetch COVID-19 data)
async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get('https://api.covid19api.com/summary')
    if response.status_code == 200:
        data = response.json()
        global_data = data['Global']
        message = f"COVID-19 Summary:\nNew Confirmed: {global_data['NewConfirmed']}\nTotal Confirmed: {global_data['TotalConfirmed']}\nNew Deaths: {global_data['NewDeaths']}\nTotal Deaths: {global_data['TotalDeaths']}\nNew Recovered: {global_data['NewRecovered']}\nTotal Recovered: {global_data['TotalRecovered']}"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


# Command: /electronic (Fetch laptop data)
async def electronic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get('https://dummyjson.com/products/search?q=Laptop')
    if response.status_code == 200:
        data = response.json()
        products = data['products'][:3]  # Fetch top 3 products
        message = "Electronics (Laptops):\n"
        for product in products:
            message += f"- {product['title']} (Price: {product['price']}$)\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


# Command: /start
async def fnc1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the vishal github")


# Command: /github
async def fnc2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="tutorial link: https://github.com/Vishalldwivedi")


# Registering commands
application.add_handler(CommandHandler('hello', hello))
application.add_handler(CommandHandler('summary', summary))
application.add_handler(CommandHandler('electronic', electronic))
application.add_handler(CommandHandler('start', fnc1))
application.add_handler(CommandHandler('github', fnc2))


# Start the bot
if __name__ == '__main__':
    application.run_polling()
