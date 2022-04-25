import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Passall")._site_ope_()
elif 'aarch' in arc:
	__import__("Passall64")._site_ope_()
else:
	exit(f' Unknow device machine {arc}')
