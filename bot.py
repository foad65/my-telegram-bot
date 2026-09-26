import telebot
from telebot import types

TOKEN = "8593138513:AAEmIYQIzXYgiNd-txMp6DGms_wOXLGBU8M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("💼 خدماتنا")
    btn2 = types.KeyboardButton("💰 الأسعار")
    btn3 = types.KeyboardButton("📞 تواصل معنا")
    markup.add(btn1, btn2, btn3)

    name = message.from_user.first_name or "صديقنا"
    welcome_text = (
        f"أهلاً بك يا {name} في بوت الخدمات!\n\n"
        "اختر أحد الأقسام من الأزرار بالأسفل 👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "💼 خدماتنا":
        bot.reply_to(message, "نقدم خدمات رقمية وتصاميم مميزة وتطوير محتوى ذكي.")
    elif message.text == "💰 الأسعار":
        bot.reply_to(message, "الأسعار مناسبة وتبدأ حسب تفاصيل الطلب، تواصل معنا لمعرفة التفاصيل!")
    elif message.text == "📞 تواصل معنا":
        bot.reply_to(message, "أهلاً بك! يمكنك إرسال استفسارك هنا مباشرة.")

print("البوت شغال الآن وجاهز لاستقبال الرسائل...")
bot.infinity_polling()
