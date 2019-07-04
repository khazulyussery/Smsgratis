from twilio.rest import Client
import os
import time

os.system('clear')
print ("""\033[1;35m
       ++++++++++++++++++++++++++
	💌SMS GRATIS BY KHAZUL💌
        ++++++++++++++++++++++++
\033[1;36m       Sms Gratis coded by Khazul

\033[1;35m📝Note : Untuk SID dan Akses token bisa
         hubungi admin khazul.

\033[1;99m☎Contact Person :
📞Instagram : khazulsocialmedia_store
📞Facebook  : Khazul Yussery
📞Telegram  : https://t.me//khazul11

""")

#

def send_sms(msg, to):
	sid = "#"
	auth_token = "#"
	number = "#"
	client = Client(sid, auth_token)
	message = client.messages.create(body=msg, from_=number, to=to)

if __name__ =="__main__":
	msg = input("\033[1;33mMasukkan Pesan : ")
	to = input("Nomor Tujuan (+62) : ")
	print(' ')
	time.sleep(1)
	print('\033[1;32m[+]Sending ...💌💌')
	time.sleep(1)
	send_sms(msg, to)
