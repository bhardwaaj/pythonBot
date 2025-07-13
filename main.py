import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /start command"""
    # Create the keyboard markup
    keyboard = [
        [
            InlineKeyboardButton("👨‍💻 Developer Info", callback_data='dev_info'),
            InlineKeyboardButton("🔍 Search", callback_data='search')
        ],
        [
            InlineKeyboardButton("📢 Share Bot", callback_data='share'),
            InlineKeyboardButton("ℹ️ About", callback_data='about')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Welcome message with ASCII art
    welcome_message = """
🔰 *Welcome to Instagram/Social Media Hacker Bot* 🔰
by Shadow

Created by:
*Abhay Singh*
_Developed by Testing Phase_

Use /help to see available commands
    """
    
    # Set up commands if they haven't been set
    commands = [
        BotCommand("start", "Start the bot and see main menu"),
        BotCommand("help", "Show help information"),
        BotCommand("search", "Search for specific features or information"),
        BotCommand("about", "About this bot"),
        BotCommand("share", "Share this bot with friends")
    ]
    await context.bot.set_my_commands(commands)
    
    await update.message.reply_text(
        welcome_message,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command"""
    help_text = """
*Available Commands:*
/start - Start the bot
/help - Show this help message
/search - Search for specific features
/about - About this bot
/share - Share this bot with friends

*Quick Tips:*
• Use the menu button (/) to see all commands
• Click on inline buttons for quick access
• Share the bot using the share button
    """
    await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /search command"""
    search_text = """
*🔍 Search Features*

You can find this bot by searching:
• @YourBotUsername
• "Instagram/Social Media Hacker Bot"

*Quick Access Links:*
• [Open Bot in Telegram](https://t.me/YourBotUsername)
• [Share Bot](https://t.me/share/url?url=https://t.me/YourBotUsername)
    """
    if update.callback_query:
        await update.callback_query.message.reply_text(search_text, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(search_text, parse_mode=ParseMode.MARKDOWN)

async def share(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /share command"""
    share_text = """
*📢 Share This Bot*

Share this bot with your friends:
• Forward this message
• Use this link: https://t.me/YourBotUsername
• Or click the button below
    """
    keyboard = [[InlineKeyboardButton(
        "Share Bot",
        url="https://t.me/share/url?url=https://t.me/YourBotUsername"
    )]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.message.reply_text(
            share_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            share_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_markup
        )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /about command"""
    about_text = """
*About This Bot* ℹ️

This bot helps you with social media automation and features.

*Features:*
• Quick access to tools
• Easy sharing
• Automated responses
• And more...

*Developer:* Abhay Singh
*Version:* 1.0.0
    """
    if update.callback_query:
        await update.callback_query.message.reply_text(about_text, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(about_text, parse_mode=ParseMode.MARKDOWN)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()

    if query.data == 'dev_info':
        dev_info = """
*Developer Information*
Name: Abhay Singh
Role: Testing Phase
Project: Social Media Hacker Bot
        """
        await query.message.reply_text(dev_info, parse_mode=ParseMode.MARKDOWN)
    elif query.data == 'search':
        await search(update, context)
    elif query.data == 'share':
        await share(update, context)
    elif query.data == 'about':
        await about(update, context)

def main():
    """Main function to run the bot"""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("search", search))
    application.add_handler(CommandHandler("share", share))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot
    print("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main() 