from telethon import TelegramClient, events
import re
import telebot
import requests
import random
import asyncio
from colorama import Fore
from os import system
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

api_id = 28949197
api_hash = '34d5a2099c3b58576b9e4f50b7da25b1'

client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'

TokenAthena = "6896553582:AAFfzMtaXsytASs6eW82aJL9AO9E5-zxGHw"
id_channel_athena = -1002025657065
bot = telebot.TeleBot(TokenAthena, parse_mode="html")
system("clear")
def verificar(ccn):
    with open('tarjetas.txt', 'r') as f: r = f.read()
    if ccn in r:
        return True
    else: 
        return False
reply_markup = InlineKeyboardMarkup(
                [
             
                    [
                        InlineKeyboardButton( 
                            "𝘙𝘌𝘍𝘌𝘙𝘌𝘕𝘊𝘐𝘈𝘚 𝘒𝘖𝘐𝘊𝘏𝘐",
                            url="https://t.me/+hiB-EQKUFiZmOTJh"  
                        
                        ),
                    ],
                ]
            )
            
        
                        
@client.on(events.NewMessage)                              
@client.on(events.MessageEdited)
async def my_event_handler(event):
    global resp
    text = event.raw_text 
   
    res = text.split()
    responses = ['Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅','Payment Successful! ✅ ','Approved! ✅','𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑪𝑵 ✅','Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅','APPROVED ✅','VIVA ✅ ','𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅','Aprobada ✅','Approved! 🟩','CARD CCN! ✅','APPROVED ✅ ','✅Appr0ved','Approved','Auth Complete ✅','APPROVED ✓ ','Approved ✅','Approved!✅','𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ✅']
    if any(response in text for response in responses):
            
            x = re.findall(r'\d+', text)
 
              
            if len(x) == 0:
                
                return
            if len(x) == 1:
                
                return
            elif len(x) == 2:
                
                return
            elif len(x) == 3:
                
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return
            cxc = (f"{cc}")
            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:                
                return
            if len(yy) == 2:
                yy = '20'+yy
            tarj = f'{cc}|{mm}|{yy}|{cvv}'           
            v = verificar(cc)
            if v == True:
                return
            tarj = f'{cc}|{mm}|{yy}|{cvv}'
            with open('tarjetas.txt', 'a') as d:
                d.write(tarj+"\n")
            if 'Approved' == 'Approved':
                bin = cxc[0:6]
                rs = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()            
                country = rs["country"]
                flag = rs["country_flag"]
                bank = rs["bank"]
                brand = rs["brand"]
                type = rs["type"]
                level = rs["level"] 
                extra2 = cxc[0:12]
                xountry = country
                api = requests.get(f"https://randomuser.me/api/?nat={xountry}&inc=name,location").json()
                name = api["results"][0]["name"]["first"]
                lastname = api["results"][0]["name"]["last"] 
                street = api["results"][0]["location"]["street"]["name"]
                complement = api["results"][0]["location"]["street"]["number"]
                
                vbvr = random.randint(1,2)
                
                if vbvr == 1 or country == "MX" or bin == "499998":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    new2 = (f"""
<b><i>𝘒𝘖𝘐𝘊𝘏𝘐 𝘚𝘊𝘙𝘈𝘗𝘗𝘌𝘙 𝘝𝘐𝘗 𝘉𝘌𝘛𝘈 </i></b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
𝘛𝘈𝘙𝘑𝘌𝘛𝘈 ⇰ ✽ <code>{cc}|{mm}|{yy}|{cvv}</code>
𝘙𝘌𝘚𝘗𝘜𝘌𝘚𝘛𝘈 ⇰ ✽ <b>Approved! ✅</b> GATE AUTH
3𝘋 𝘝𝘌𝘙𝘐𝘍𝘐𝘊𝘈𝘊𝘐𝘖𝘕 ⇰ ✽ <b>No ✅</b> avs approved
𝘌𝘟𝘛𝘙𝘈 𝘉𝘐𝘕 ⇰ ✽ <code>{extra2}xxxx|{mm}|{yy}|rnd</code>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
𝘉𝘐𝘕 𝘐𝘕𝘍𝘖 ⇰ ✽ <b>{brand} {level} {type}</b>
𝘉𝘈𝘕𝘊𝘖 ⇰ ✽ <b>{bank}</b>
𝘗𝘈𝘐𝘚 ⇰ ✽ <b>{country} {flag}</b>
𝘕𝘖𝘛𝘈 ⇰ ✽ 𝘕𝘖 𝘝𝘜𝘌𝘓𝘝𝘈𝘕 𝘈 𝘏𝘈𝘊𝘌𝘙 𝘙𝘌𝘊𝘏𝘌𝘊𝘒 𝘔𝘈𝘛𝘈𝘕 𝘓𝘈 𝘓𝘐𝘝𝘌
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Owner ⇰ ♛ @GatoOnichan2 
""")
                #bot.send_message(id_channel_athena, text) 
                    img3 = "https://i.gifer.com/8zSy.gif"
                    
                    print(f"\n ✅ {Fore.LIGHTWHITE_EX}#Card Tested: {Fore.LIGHTBLUE_EX}{cc}|{mm}|{yy}|{cvv} {Fore.LIGHTWHITE_EX}/ {country}|{flag}\n" 
                             f"  {Fore.LIGHTWHITE_EX}#Seccesfully Sended - ID Channel: {Fore.LIGHTBLUE_EX}{id_channel_athena}")
                 
                    bot.send_photo(id_channel_athena,img3, new2, reply_markup=reply_markup)
                     
                elif vbvr == 2 or bin == "451015":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    new2 = (f"""
<b><i>𝘒𝘖𝘐𝘊𝘏𝘐 𝘚𝘊𝘙𝘈𝘗𝘗𝘌𝘙 𝘝𝘐𝘗 𝘉𝘌𝘛𝘈 </i></b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
𝘛𝘈𝘙𝘑𝘌𝘛𝘈 ⇰ ✽ <code>{cc}|{mm}|{yy}|{cvv}</code>
𝘙𝘌𝘚𝘗𝘜𝘌𝘚𝘛𝘈 ⇰ ✽ <b>Approved! ✅</b> GATE AUTH
3𝘋 𝘝𝘌𝘙𝘐𝘍𝘐𝘊𝘈𝘊𝘐𝘖𝘕 ⇰ ✽ <b>Yes ❌</b> 
𝘌𝘟𝘛𝘙𝘈 𝘉𝘐𝘕 ⇰ ✽ <code>{extra2}xxxx|{mm}|{yy}|rnd</code>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
𝘉𝘐𝘕 𝘐𝘕𝘍𝘖 ⇰ ✽ <b>{brand} {level} {type}</b>
𝘉𝘈𝘕𝘊𝘖 ⇰ ✽ <b>{bank}</b>
𝘗𝘈𝘐𝘚 ⇰ ✽ <b>{country} {flag}</b>
𝘕𝘖𝘛𝘈 ⇰ ✽  𝘕𝘖 𝘝𝘜𝘌𝘓𝘝𝘈𝘕 𝘈 𝘏𝘈𝘊𝘌𝘙 𝘙𝘌𝘊𝘏𝘌𝘊𝘒 𝘔𝘈𝘛𝘈𝘕 𝘓𝘈 𝘓𝘐𝘝𝘌
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Owner ⇰ ♛ @GatoOnichan2
""")
                #bot.send_message(id_channel_athena, text) 
                    img3 = "https://i.gifer.com/8zSy.gif"
                   
                    print(f"\n  ❌ {Fore.LIGHTWHITE_EX}#Card Tested: {Fore.LIGHTBLUE_EX}{cc}|{mm}|{yy}|{cvv} {Fore.LIGHTWHITE_EX}/ {country}|{flag}\n" 
                             f"  {Fore.LIGHTWHITE_EX}#Seccesfully Sended - ID Channel: {Fore.LIGHTBLUE_EX}{id_channel_athena}")
                 
                    bot.send_photo(id_channel_athena,img3, new2, reply_markup=reply_markup)
                    
    else:
        pass
        
        
client.start()
client.run_until_disconnected()
