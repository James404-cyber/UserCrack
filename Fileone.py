import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/ids/OK')
except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Jm").menu()
elif 'aarch' in arc:
	__import__("Passall").menu()
else:
	exit(f' Unknow device machine {arc}')
