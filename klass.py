import os,time,sys
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.01)
def klass():
	os.system("termux-media-player play /sdcard/ooo.mp3")
klass()
os.system("clear")
jalan("""\033[1;35m
███████╗░█████╗░██╗░░██╗██████╗░
██╔════╝██╔══██╗██║░░██║██╔══██╗
█████╗░░███████║███████║██║░░██║
██╔══╝░░██╔══██║██╔══██║██║░░██║
██║░░░░░██║░░██║██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░""")
time.sleep(2)
os.system("clear")
jalan("""\033[1;37m▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒
▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒
▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒
▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒
▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒
▒▒▒▌────────▌▒▒▒▒▒▒▒
▒▒█─────────▐▒▒▒▒▒▒▒
▒▐▌─▐───────▐▄▄▒▒▒▒▒
▒▐▌─▐────────▄▀▀█▒▒▒
▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒
▐▌────██▀█░█▄▒▄▄█▀▀▌
▐▌──▌▐───▐░░▐▀░░░░░▌
▐▌──▌────▐░░▐░░░░░░▌
▐───▌────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█─────▀█▐▄▄▄█▀▀▒
▀▄▄─▐───────▄█▒▒▒▒▒▒
▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒
▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒
""")
time.sleep(2)
os.system('clear')
jalan("🇺​​​​​🇵​​​​​🇩​​​​​🇦​​​​​🇹​​​​​🇪​​​​​")
print(' ')
jalan("""\033[1;32m────────▄▄▄▄▄▄▄▄▄
────────▌▐░▀░▀░▀▐
────────▌░▌░░░░░▐
────────▌░░░░░░░▐
────────▄▄▄▄▄▄▄▄▄
──▄▀▀▀▀▀▌▄█▄░▄█▄▐▀▀▀▀▀▄
─█▒▒▒▒▒▐░░░░▄░░░░▌▒▒▒▒▒█
▐▒▒▒▒▒▒▒▌░░░░░░░▐▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒█░▀▀▀▀▀░█▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▒▌
▐▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▌
▐▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▌
▐▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▄▄▄▄▄▄▄▄▄▐▒▒▒▒▒▒▌
▐▄▄▄▄▄▄▌▌███████▌▐▄▄▄▄▄▄▌
─█▀▀▀▀█─▌███▌███▌─█▀▀▀▀█
─▐░░░░▌─▌███▌███▌─▐░░░░▌
──▀▀▀▀──▌███▌███▌──▀▀▀▀
────────▌███▌███▌
────────▌███▌███▌
──────▐▀▀▀██▌█▀▀▀▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒
""")
time.sleep(2)
def list():
	jalan("\033[1;36m[1]Update Termux")
	jalan("\033[1;37m[2]Install pkg Termux")
	jalan("\033[1;35m[3]Install Metasploit")
	jalan("\033[1;32m[4]Root Termux")
	jalan("\033[1;33m[5]Ngrok")
	jalan("\033[1;31m[6]Kali Links")
	jalan("\033[1;34m[7]Contact with me  😍  😘  ❤️")
list()
print(' ')
choose = input ("\033[1;31m[?]choose : ")
print(' ')
if choose =='1':
	os.system('clear')
	jalan("""\033[1;31m
████████╗███████╗██████╗░███╗░░░███╗██╗░░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║░░░██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░░██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░░██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░""")  
	os.system(" pkg update && pkg upgrade -y")
	os.system("xdg-open https://api.whatsapp.com/send?phone=+966568781867")
	os.system("python3 klass.py")
elif choose =='2':
	os.system("clear")
	jalan("""\033[1;33m
██████╗░██╗░░██╗░██████╗░
██╔══██╗██║░██╔╝██╔════╝░
██████╔╝█████═╝░██║░░██╗░
██╔═══╝░██╔═██╗░██║░░╚██╗
██║░░░░░██║░╚██╗╚██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░""")
	os.system(" apt update && apt upgrade -y ; pkg install git -y ; pkg install python -y ; pkg install python2 -y ; pkg install figlet -y ; pkg install wget -y ; pkg install root-repo ; pkg install unstable-repo ; pkg install x11-repo ; pkg install ruby -y ; pkg install nano -y ; pkg install toilet -y ;pkg install locate -y ; gem install figlet ; pip install wordlist ; pkg install termux-api -y ; pkg install ncurses-utils -y ; pip install youtube-dl ; apt install golang -y ; apt install php -y ; apt install cmatrix -y ; pkg install cowsay -y ; pkg install ruby -y ; pkg install openssh -y ; pkg install unzip -y ; pkg install tor -y ; pkg install tar -y ; pkg install net-tools -y ; pkg install zip -y ; pkg install unrar -y ; pkg install clang -y ; pkg install w3m -y ; pkg install proot -y ; pip2 install wget ; pip install --upgrade pip ; pkg install python2-dev -y ; pip2 install mechanize ; pkg install man -y ; pip install argument ; pkg install graphviz -y ; apt install tty-clock -y ; gem install bundler ; gem install bundle ")
	os.system("python3 klass.py")
elif choose =='3':
	os.system("clear")
	jalan("""\033[1;31m🇲​​​​​🇪​​​​​🇹​​​​​🇦​​​​​🇸​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇮​​​​​🇹​​​​​""")
	print(' ')
	os.system(" pkg update && pkg upgrade -y ; pkg install unstable-repo -y ; pkg install metasploit -y ; apt -f install -y ; msfconsole")
elif choose =="4":
	os.system("clear")
	jalan("""\033[1;34m
─────────────────────────────────────────────────────────────────
─████████████████───██████████████─██████████████─██████████████─
─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒████████▒▒██───██▒▒██████▒▒██─██▒▒██████▒▒██─██████▒▒██████─
─██▒▒██────██▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██─────
─██▒▒████████▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██─────
─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██─────
─██▒▒██████▒▒████───██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██─────
─██▒▒██──██▒▒██─────██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██─────
─██▒▒██──██▒▒██████─██▒▒██████▒▒██─██▒▒██████▒▒██─────██▒▒██─────
─██▒▒██──██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒██─────
─██████──██████████─██████████████─██████████████─────██████─────
─────────────────────────────────────────────────────────────────""")
	os.system(" apt update && apt upgrade && apt install curl proot wget ruby ; curl -LO https://raw.githubusercontent.com/Hax4us/TermuxAlpine/master/TermuxAlpine.sh; chmod 777 TermuxAlpine.sh ; ./TermuxAlpine.sh ; startalpine;")
	os.system("https://api.whatsapp.com/send?phone=+966568781867")	
	os.system("python3 klass.py")
elif choose =="5":
	os.system("clear")
	jalan("""\033[1;35m
███╗░░██╗░██████╗░██████╗░░█████╗░██╗░░██╗
████╗░██║██╔════╝░██╔══██╗██╔══██╗██║░██╔╝
██╔██╗██║██║░░██╗░██████╔╝██║░░██║█████═╝░
██║╚████║██║░░╚██╗██╔══██╗██║░░██║██╔═██╗░
██║░╚███║╚██████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")
	time.sleep(1)
	print(' ')
	print(' ')
	jalan("\033[1;35m[1] Ngrok tcp")
	jalan("\033[1;33m[2] Ngrok http")
	print(' ')
	choose =input("\033[1;36m[?] choose : ")
	if choose =='1':
		os.system(" pkg install proot ; ngrok tcp 444")
	elif choose =="2":
			os.system(" pkg install proot ; ngrok http 4444")
			os.system("python3 klass.py")
		
elif choose =="6":
	os.system("clear")
	jalan("""\033[1;31m
██╗░░██╗░█████╗░██╗░░░░░██╗
██║░██╔╝██╔══██╗██║░░░░░██║
█████═╝░███████║██║░░░░░██║
██╔═██╗░██╔══██║██║░░░░░██║
██║░╚██╗██║░░██║███████╗██║
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝""")
	time.sleep(1)
	jalan("🇰​​​​​🇦​​​​​🇱​​​​​🇮​​​​​")
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh ; ./start-kali.sh")
	os.system("python3 klass.py")		
elif choose =="7":
	os.system("clear")
	jalan("""\033[1;31m_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██
""")
	time.sleep(1)
	jalan("🇫​​​​​🇦​​​​​🇭​​​​​🇩​​​​​")
	os.system("xdg-open https://api.whatsapp.com/send?phone=+966568781867")
	os.system("python3 klass.py")



