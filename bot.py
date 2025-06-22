
import requests
import time

BOT_TOKEN = "7729867827:AAHHtvt23GBRNQhrxpYgAQu-05tVJnyGj-E"
ADMIN_ID = 2114059145
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

def send_message(chat_id, text):
    requests.post(API_URL + "sendMessage", data={"chat_id": chat_id, "text": text})

def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    response = requests.get(API_URL + "getUpdates", params=params)
    return response.json()

def generate_fake_info():
    return "👤 الاسم: محمد أحمد\n📧 الايميل: test@example.com\n📞 الهاتف: +201234567890\n🏠 العنوان: القاهرة - مصر"

def check_card_live(card_number):
    # محاكاة لفحص البطاقة (للتجربة فقط)
    if card_number.startswith("4"):
        return True
    else:
        return False

def main():
    last_update_id = None
    control_panel = (
        "🔥 VIRUS BOT PRO | ميدو الحراق 🔥\n"
        "-----------------------\n"
        "/gen ➔ توليد بطاقات\n"
        "/otp ➔ فحص OTP\n"
        "/passed ➔ فحص Passed\n"
        "/fake ➔ معلومات وهمية\n"
        "/check ➔ فحص فيزا Live or Dead\n"
        "/admin ➔ لوحة التحكم\n"
    )

    while True:
        updates = get_updates(offset=last_update_id)
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "")

            if text == "/start":
                send_message(chat_id, control_panel)

            elif text == "/admin":
                if chat_id == ADMIN_ID:
                    send_message(chat_id, "✅ تم فتح لوحة التحكم للمسؤول")
                else:
                    send_message(chat_id, "❌ لا يوجد صلاحية للوصول الى لوحة التحكم")

            elif text == "/otp":
                send_message(chat_id, "🔐 محاكاة فحص OTP: تم إرسال كود التحقق (وهمي)")

            elif text == "/passed":
                send_message(chat_id, "✅ تم تمرير البطاقة بنجاح (محاكاة Passed)")

            elif text == "/fake":
                send_message(chat_id, generate_fake_info())

            elif text.startswith("/check"):
                parts = text.split(" ")
                if len(parts) == 2:
                    card_number = parts[1]
                    if check_card_live(card_number):
                        send_message(chat_id, "✅ البطاقة Live (وهمية)")
                    else:
                        send_message(chat_id, "❌ البطاقة Dead (وهمية)")
                else:
                    send_message(chat_id, "❗ استخدم الأمر بهذا الشكل: /check 4111111111111111")

            else:
                send_message(chat_id, "❓ أمر غير معروف")
        time.sleep(1)

if __name__ == "__main__":
    main()
