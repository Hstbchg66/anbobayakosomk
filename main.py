import requests,re
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from gate6 import Tele
from colorama import Fore
sto = {"stop":False}
token = "7385888101:AAFK-HYuxPtc_1oEO5aXw4kQuPxhJG7YK48" #توكنك
id =6898845629  #ايديك
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,'''• Thank You For Start • The Bot.

• This Bot For Checking CCs Only.

• You Must Have an VIP Subscription To Use The Bot.

• Send /vip To See The Prices of Subscription.

• Send /gate To See The Gateway Statuse.

• Send /stop To Stop The Bot.

• Onwer ⇾ @Mohamed_Was_Here'''.format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())

@bot.message_handler(commands=["vip"])
def start(message):
 bot.send_message(message.chat.id,'''• VIP Plans 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1 Day ⇾ 20EGP
3 Days ⇾ 60EGP
1 Week ⇾ 200EGP
1 Month ⇾400EGP 
Life Time ⇾ 800EGP ( غير محدود )
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• Available Payment Methods ⇾ Vodafone Cash - USDT
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• Owner ⇾ @Mohamed_Was_Here'''.format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
 
@bot.message_handler(commands=["gate"])
def start(message):
 bot.send_message(message.chat.id,'''َٰ𝚂ٍ𝚃ٓ𝚁𝙸ٍّ𝙿ٍ𝙴 ٍّ𝙲َ𝙷َٰ𝙰ٓ𝚁ٍ𝙶ٍ𝙴 6$
َٰ𝙰ٍّ𝙲ٍ𝚃𝙸ُ𝚅َٰ𝙰ٍ𝚃ٍ𝙴َ𝙳
َ𝙳َٰ𝙰ٍ𝚃ٍ𝙴 ⇾ 12/06/2024 ✅'''.format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup()) 
 
 @bot.message_handler(commands=["stop"])
 def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'Check Ended')
    
@bot.message_handler(content_types=["document"])
def main(message):
 bad=0
 nok=0
 ok = 0
 last=0
 otp=0
 ko = (bot.reply_to(message,"#Was_Mohamed").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "-------"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "--------"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           lucifer1 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u8')
           res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           lucifer3 = types.InlineKeyboardButton(f"• Charge 💸 : [ {ok} ] •",callback_data='u2')
           lucifer4 = types.InlineKeyboardButton(f"• OTP ⚠️ : [ {nok} ] •",callback_data='u2')
           lucifer5 = types.InlineKeyboardButton(f"• Declined ❌️ : [ {bad} ] •",callback_data='u1')
           lucifer6 = types.InlineKeyboardButton(f"• Total :) [ {total} ] •",callback_data='u1')
           lucifer7 = types.InlineKeyboardButton(f"• #Was_Mohamed •",callback_data='u1')
           mes.add(lucifer1,res,lucifer3,lucifer4,lucifer5,lucifer6,lucifer7)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text='''Gateway ⇾ Stripe Charge 3.18$
    ''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"حدث خطأ اثناء فحص هذه البطاقه وتم تخطيها {cc}")
                  last = "Your card was declined."
           if "Retry" in last:
               bot.reply_to(message,"- Dont Check Again , Limit Reched Contact @Mohamed_Was_Here To Update ✅")
               return
           elif "Your card was declined." in last or "generic_decline" in last:
               bad +=1
               print(Fore.YELLOW+cc+"->"+Fore.RED+last)
               
           elif "OK" in last:
               ok +=1
               respo = f'''
⦏ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ⦐ 

[↯] 𝗖𝗖 ⇾ <code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘 ⇾ Stripe Charge 3.18$
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 ⇾ Payment Successful.

[↯] 𝗕𝗢𝗧 𝗕𝗬 ⇾ @Mohamed_Was_Here
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           elif "3D-AUTH" in last:
               nok += 1
               respo = f'''
⦏ 𝐄𝐫𝐫𝐨𝐫 ⚠️ ⦐ 

[↯] 𝗖𝗖 ⇾ <code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘 ⇾ Stripe Charge 3.18$
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 ⇾ OTP ⚠️

[↯] 𝗕𝗢𝗧 𝗕𝗬 ⇾ @Mohamed_Was_Here
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
       if sto["stop"] == False:
           bot.reply_to(message,'#－ 𝖯𝗋𝗈𝖼𝖼𝖾𝗌𝗌 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾 ✅.')
 else:
     bot.reply_to(message,'#- Sorry This Not 4U')
       
print("STARTED -> @Mohamed_Was_Here ✅🏴‍☠️")
bot.polling()