import os,sys,  platform, random

os.system('rm -rf .txt')
for n in range (20000):
	nmbr = random.randint(1111111,9999999)
	sys.stdout = open('.txt', 'a')
	print nmbr
	sys.stdout.flush()
try:
	import bs4
except ImportError:
	print("\n ! bs4 module is not installed yet")
	os.system("pip2 install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] futures module not installed")
	os.system("pip2 install futures")

	print('\n\n\n\nInstalling dependencies\n\n\n\n\n')
	time.sleep(2)
	os.system('pip2 install requests bs4')
	os.system('clear')
	print('\n\n\n\033[1;32mInstalled successfully\033[0;97m')
	time.sleep(1)
	os.system('python2 Somi.py')
reload(sys)
sys.setdefaultencoding('utf-8')
try:
	os.mkdir('/sdcard/Account')
except:
	pass
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Test import subscribe
    subscribe()
elif bit == '32bit':
    from Test import subscribe
    subscribe()
