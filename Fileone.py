import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/OK')
except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Multi").ninex()
elif 'aarch' in arc:
	__import__("Multi").ninex()
else:
	exit(f' Unknow device machine {arc}')
