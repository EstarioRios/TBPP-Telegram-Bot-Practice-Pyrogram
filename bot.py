from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from .config import bot_token  # فرض می‌کنیم فایل config در دایرکتوری جاری شما قرار دارد

app = Client("my_bot", bot_token=bot_token)

keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("خداحافظی کن")],
        [KeyboardButton("خودت رو معرفی کن")],
        [KeyboardButton("وارد کردن اسم")],
    ],
    resize_keyboard=True,
)

keyboard_str = ["خداحافظی کن", "خودت رو معرفی کن", "وارد کردن اسم"]


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("سلام به ربات تلگرامی من خوش آمدی ☺", reply_markup=keyboard)


@app.on_message(filters.text)
def handle_markups_message(client, message):
    if message.text == "خداحافظی کن":
        say_goodbye(client, message)
    elif message.text == "خودت رو معرفی کن":
        say_introduction(client, message)
    elif message.text == "وارد کردن اسم":
        get_name(client, message)
    else:
        message.reply_text("ورودی غیر معتبر است", reply_markup=keyboard)


def get_name(client, message):
    message.reply_text("اسم خودت را بنویس و بفرست")
    name = message.text
    name = str(name).strip()
    return name


def say_goodbye(client, message):
    message.reply_text("خداحافظ دوست من")


def say_introduction(client, message):
    message.reply_text(
        "سلام.\nمن یک ربات هستم که فقط هستم که باشم و به هیچ دردی هم رسما نمی‌خورم (البته فعلا)"
    )


app.run()
