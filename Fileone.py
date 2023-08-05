import platform
import os

os.system('termux-setup-storage')
os.system('python -m pip uninstall urllib3 && python -m pip install urllib3')
os.system('pkg install wget')
os.system('git pull')
try:os.system('mkdir /sdcard/OK')
except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("User").ninex()
elif 'aarch' in arc:
	__import__("Ulibv").ninex()
else:
	exit(f' Unknow device machine {arc}')
