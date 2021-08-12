import colorama
import os
import git
os.system("clear")
banner_a = ("\n  ____     _____           _ ")    

banner_b = ("\n / ___|   |_   _|__   ___ | |___ ")

banner_c = ("\n| |  | | | || |/ _ | / _ || / __|")

banner_d =("\n| |__| |_| || | (_) | (_) | |__ ")

banner_e = ("\n |____|__, ||_||___/ |___/|_|___/")

banner_f = ("\n      |___/                     ") 

banner_x = (banner_a + banner_b + banner_c + banner_d + banner_e + banner_f)

print(chr(27)+"[1;33m"+banner_x)

print("\033[;36m"+"\nCreador: Crypto445 ")

print(chr(27)+"[1;33m"+"Elija su opcion: ")
opciones = ["[ 1 ]Banner", "[ 2 ]Herramientas", "[ 3 ]Sobre la herramienta", "[ 4 ] Salir"]
for n in opciones:
	print(n)
user_a = int(input("===> "))
if user_a == 3:
	print("\033[;36m"+"Creador: @Crypto445")
	readme = os.system("cat README.md")
	quit()
elif user_a == 1:
	os.system("python3 banner.py")
elif user_a == 4:
	quit()	
elif user_a == 2:
	clear = os.system("clear")
	print(chr(27)+"[1;33m"+banner_x)
	opciones_a = ["[ 1 ] Information Gathering", "[ 2 ] Vulnerability Scanner", "[ 3 ] Explotation Tools", "[ 4 ] Wireless Testing", "[ 5 ] Forensics Tools", "[ 6 ] Web Hacking", "[ 7 ] Stress Testing", "[ 8 ] Sniffing & Spoofing", "[ 9 ] Password Attacks", "[ 10 ] Maintaining Access", "[ 11 ] IP-Tracking tools", "[ 12 ] DDOS Attacks", "[ 13 ] SPAM"]  
	for lista in opciones_a:
		print(lista)

usuario = int(input("===> "))
if usuario == 1:
	clear_a = os.system("clear")
	print(banner_x)
	
	print("\n[ 1 ] nmap \n[ 2 ] Nikto \n[ 3 ] sqlmap \n[ 4 ] Sublist3r \n[ 5 ] dmitry \n[ 6 ] dnsenum \n[ 7 ] Trackout \n[ 8 ] Infoga \n[ 99 ]Volver")
	info = int(input("===> "))
	if info == 1: 
		os_a = int(input("Que os usas? \n[ 1 ] Termux \n[ 2 ] Ubuntu u otro \n===> "))
		if os_a == 1:
			os.system("pkg install nmap")
		elif os_a == 2: 
		    os.system("sudo apt install nmap")
		else:
		    print("ERROR!!!!")
		    os.system("python3 CyTools.py")
	elif info == 2:
	    ab = input("Escriba la ruta: ")
	    git.Git(f"{ab}").clone("git clone https://github.com/sullo/nikto")
	    print(f"Instalacion completada y guardado en {ab}")
	    os.system("python3 CyTools.py")
	elif info == 3:
	    os_c = input("Escriba la ruta: ")
	    git.Git(f"{os_c}").clone("https://github.com/sqlmapproject/sqlmap")
	    print(f"Instalacion completada y guardado en {os_c}")
	    os.system("python3 CyTools.py")
	elif info == 4:
	    ruta_b = input("Escriba la ruta: ")
	    git.Git(f"{ruta_b}").clone("https://github.com/aboul3la/Sublist3r")    
	    print(f"Instalacion completa y guardado en {ruta_b}")
	    os.system("python3 CyTools.py")
	elif info == 5:
	    ruta_c = input("Escriba la ruta: ")
	    git.Git(f"{ruta_c}").clone("https://github.com/jaygreig86/dmitry")	
	    print(f"Instalacion completada guardado en {ruta_c}")
	    os.system("python3 CyTools.py")
	elif info == 6:
	    ruta_d = input("Escriba la ruta: ")
	    git.Git(f"{ruta_d}").clone("https://github.com/fwaeytens/dnsenum")
	    print(f"Instalacion completada y guardado en {ruta_d}")
	    os.system("python3 CyTools.py")
	elif info == 7:
	    ruta_e = input("Escriba la ruta: ")
	    git.Git(f"{ruta_e}").clone("https://github.com/abaykan/TrackOut")
	    print(f"Instalacion completada guardado en {ruta_e}")
	    os.system("python3 CyTools.py")
	elif info == 8:
	    ruta_f = input("Escriba la ruta: ")
	    git.Git(f"{ruta_f}").clone("https://github.com/m4ll0k/Infoga")
	    print(f"Instalacion completada y guardado en {ruta_f}")   
	    os.system("python3 CyTools.py")
	elif info == 99:
	    os.system("python3 CyTools.py")
	else:
	    print("ERROR!!!")
	    os.system("python3 CyTools.py")
elif usuario == 2:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] Xshell \n[ 2 ] BlackBox \n[ 3 ] reng3r \n[ 4 ] Lynis \n[ 5 ] OpenVas \n[ 6 ] a-xex \n[ 7 ] XAttacker \n[ 99 ] Salir")
    info_b = int(input("===> "))
    if info_b == 1:
        Tool_a = input("Escriba la ruta: ")
        git.Git(f"{Tool_a}").clone("https://github.com/Manisso/Xshell")
        print(f"Instalacion completada guardado en {Tool_a}")
        os.system("python3 CyTools.py")
    elif info_b == 2:
    	Tool_b = input("Escriba la ruta: ")
    	git.Git(f"{Tool_b}").clone("https://github.com/StackExchange/blackbox")
    	print(f"Instalacion completada, guardado en {Tool_b}")
    	os.system("python3 CyTools.py")
    elif info_b == 3:
        Tool_c = input("Escriba la ruta: ")
        git.Git(f"{Tool_c}").clone("https://github.com/floriankunushevci/rang3r")
        os.system("python3 CyTools.py")	
    elif info_b == 4:
    	Tool_d = input("Escriba la ruta: ")
    	git.Git(f"Tool_d").clone("https://github.com/CISOfy/lynis")
    	os.system("python3 CyTools.py")
    elif info_b == 5:
        Tool_e = input("Escriba la ruta: ")
        git.Git(f"{Tool_e}").clone("https://github.com/greenbone/openvas-scanner")
        os.system("python3 CyTools.py")
    elif info_b == 6:
        Tool_f = input("Escriba la ruta: ")
        git.Git(f"{Tool_f}").clone("https://github.com/farinap5/A-xex")
        os.system("python3 CyTools.py")
    elif info_b == 7:
        Tool_g = input("Escriba la ruta: ")
        git.Git(f"{Tool_g}").clone("https://github.com/Moham3dRiahi/XAttacker")
        os.system("python3 CyTools.py")
    elif info_b == 99:
        os.system("python3 CyTools.py") 
    else:
        print("ERROR!!!")
        os.system("python3 CyTools.py")
elif usuario == 3:
	os.system("clear")
	print(banner_x)
	print("\n[ 1 ] ATSCAN \n[ 2 ] beef \n[ 3 ] routersploit \n[ 4 ] shellnoob \n[ 5 ] Reverse shell Factory \n[ 6 ] websploit \n[ 7 ] Metasploit Framework \n[ 8 ] Social-Engineer-toolkit \n[ 9 ] Xerosploit \n[ 10 ] roxysploit \n[ 11 ] txtool \n[ 99 ] Salir")
	info_c = int(input("===> "))
	if info_c == 1:
		herra_a = input("Escriba la ruta: ")
		git.Git(f"{herra_a}").clone("https://github.com/AlisamTechnology/ATSCAN")
		print(f"Instalacion completada, guardado en {herra_a}")
		os.system("python3 CyTools.py")
	elif info_c == 2:
	    herra_b = input("Escriba la ruta: ")
	    git.Git(f"{herra_b}").clone("https://github.com/beefproject/beef")
	    print(f"Instalacion completada, guardado en {herra_b}")
	    os.system("python3 CyTools.py")
	elif info_c == 3:
	    herra_c = input("Escriba la ruta: ")
	    git.Git(f"{herra_c}").clone("https://github.com/threat9/routersploit")
	    print(f"Instalacion completada, Guardado en {herra_c}")
	    os.system("python3 CyTools.py")
	elif info_c == 4:
	    herra_d = input("Escriba la ruta: ")
	    git.Git(f"{herra_d}").clone("https://github.com/reyammer/shellnoob")
	    print(f"Instalacion completada, Guardado en {herra_d}")
	    os.system("python3 CyTools.py")
	elif info_c == 5:
	    herra_e = input("Escriba la ruta: ")
	    git.Git(f"{herra_e}").clone("https://github.com/farinap5/rsfac")
	    print(f"Instalacion completada, Guardado en {herra_e}")   
	    os.system("python3 CyTools.py")
	elif info_c == 6:
	    herra_f = input("Escriba la ruta: ")
	    git.Git(f"{herra_f}").clone("https://github.com/websploit/websploit")
	    print(f"Instalacion completada, Guardado en {herra_f}")
	    os.system("python3 CyTools.py")
	elif info_c == 7:
	    herra_g = input("Escriba la ruta: ")
	    git.Git(f"{herra_g}").clone("https://github.com/rapid7/metasploit-framework")
	    print(f"Instalacion completada, Guardado en {herra_g} ")
	    os.system("python3 CyTools.py")
	elif info_c == 8:
	    herra_h = input("Escriba la ruta: ")
	    git.Git(f"{herra_h}").clone("https://github.com/trustedsec/social-engineer-toolkit")
	    print(f"Instalacion completada, Guardado en {herra_h}")
	    os.system("python3 CyTools.py")
	elif info_c == 9:
	   herra_i = input("Escriba la ruta: ")
	   git.Git(f"{herra_i}").clone("https://github.com/LionSec/xerosploit")
	   print(f"Instalacion completada, Guardado en {herra_i}")
	   os.system("python3 CyTools.py")
	elif info_c == 10:
	    herra_j = input("Escriba la ruta: ")
	    git.Git(f"{herra_j}").clone("https://github.com/andyvaikunth/roxysploit")
	    print(f"Instalacion completada, Guardado en {herra_j}")
	    os.system("python3 CyTools.py")
	elif info_c == 11:
	    herra_k = input("Escriba la ruta: ")
	    git.Git(f"{herra_k}").clone("https://github.com/kuburan/txtool")
	    print(f"Instalacion completada, Guardado en {herra_k}")
	    os.system("python3 CyTools.py")
	elif info_c == 99:
		os.system("python3 CyTools.py")
	else:
		print("ERROR!!!")
		os.system("python3 CyTools.py")
elif usuario == 4:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] Aircrack-ng \n[ 2 ] Fluxion \n[ 3 ] Wifi-Hacker \n[ 4 ] Wifite \n[ 5 ] Wifite2 \n[ 6 ] reaver \n[ 7 ] Pyrit \n[ 8 ] pixiewps \n[ 99 ]Salir")
    info_d = int(input("===> "))
    if info_d == 1:
        To_a = input("Escriba la ruta: ")
        git.Git(f"{To_a}").clone("https://github.com/aircrack-ng/aircrack-ng")
        print(f"Instalacion completada, Guardado en {To_a}")
        os.system("python3 CyTools.py")
    elif info_d == 2:
    	To_b = input("Escriba la ruta: ")
    	git.Git(f"{To_b}").clone("https://github.com/FluxionNetwork/fluxion")
    	print(f"Instalacion completada, Guardado en {To_b}")
    	os.system("python3 CyTools.py")
    elif info_d == 3:
    	To_c = input("Escriba la ruta: ")
    	git.Git(f"{To_c}").clone("https://github.com/esc0rtd3w/wifi-hacker")
    	print(f"Instalacion completada, Guardado en {To_c}")
    	os.system("python3	CyTools.py")
    elif info_d == 4:
    	To_d = input("Escriba la ruta: ")
    	git.Git(f"{To_d}").clone("https://github.com/derv82/wifite")
    	print(f"Instalacion compleatada, Guardado en {To_d}")
    	os.system("python3 CyTools.py")
    elif info_d == 5:
        To_e = input("Escriba la ruta: ")
        git.Git(f"{To_e}").clone("https://github.com/derv82/wifite2")
        print(f"Instalacion completada, Guardado en {To_e}")
        os.system("python3 CyTools.py")
    elif info_d == 6:
        To_f = input("Escriba la ruta: ")
        git.Git(f"{To_f}").clone("https://github.com/t6x/reaver-wps-fork-t6x")
        print(f"Instalacion completada, Guardado en {To_f}")
        os.system("python3 CyTools.py")
    elif info_d == 7:
        To_g = input("Escriba la ruta: ")
        git.Git(f"{To_g}").clone("https://github.com/JPaulMora/Pyrit")
        print(f"Instalacion completada, Guardado en {To_g}")   
        os.system("python3 CyTools.py")
    elif info_g == 8:
    	To_h = input("Escriba la ruta: ")
    	git.Git(f"{To_h}").clone("https://github.com/wiire-a/pixiewps")
    	print(f"Instalacion completada, Guardado en {To_h}")
    	os.system("python3 CyTools.py")
    elif info_h == 99:
        os.system("python3 CyTools.py")	
elif usuario == 5:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] RegRipper2.8 \n[ 2 ] BinWalk \n[ 3 ] bulk_extractor \n[ 4 ] capstone \n[ 5 ] cuckoo \n[ 6 ] distorm \n[ 7 ] dumpzilla \n[ 8 ] extundelete \n[ 9 ] foremost \n[ 10 ] p0f \n[ 11 ] pdf-parser \n[ 12 ] volatility \n[ 13 ] xplico \n[ 99 ] Salir")
    info_e = int(input("===> "))
    if info_e == 1:
    	Too_a = input("Escriba la ruta: ")
    	git.Git(f"{Too_a}").clone("https://github.com/kireyn/RegRipper2.8")
    	print(f"Instalacion completada, Guardado en {Too_a}")
    	os.system("python3 CyTools.py")
    elif info_e == 2:
        Too_b = input("Escriba la ruta: ")
        git.Git(f"{Too_b}").clone("https://github.com/ReFirmLabs/binwalk")
        print(f"Instalacion completada, Guardado en {Too_b}")
        os.system("python3 CyTools.PY")	
    elif info_e == 3:
        Too_c = input("Escriba la ruta: ")
        git.Git(f"{Too_c}").clone("https://github.com/simsong/bulk_extractor")
        print(f"Instalacion completada, Guardado en {Too_c}")
        os.system("python3 CyTools.py")
    elif info_e == 4:
        Too_d = input("Escribe la ruta: ")
        git.Git(f"{Too_d}").clone("https://github.com/aquynh/capstone")
        print(f"Instalacion completada, Guardado en {Too_d}")
        os.system("python3 CyTools.py")
    elif info_e == 5:
        Too_e = input("Escribe la ruta: ")
        git.Git(f"{Too_e}").clone("https://github.com/cuckoosandbox/cuckoo")
        print(f"Instalacion completada, Guardado en {Too_e}")
        os.system("python3 CyTools.py")
    elif info_e == 6:
        Too_f = input("Escriba la ruta: ")
        git.Git(f"{Too_f}").clone("https://github.com/gdabah/distorm")
        print(f"Instalacion completada, Guardado en {Too_f}")
        os.system("python3 CyTools.py")
    elif info_e == 7:
        Too_g = intput("Escriba la ruta: ")
        git.Git(f"{Too_g}").clone("https://github.com/Busindre/dumpzilla")
        print(f"Instalacion Completada, Guardado en {Too_g}")
        os.system("python3 CyTools.py")    
    elif info_e == 8:
    	Too_h = input("Escriba la ruta: ")
    	git.Git(f"{Too_h}").clone("https://github.com/cherojeong/extundelete")
    	print(f"Instalacion completada, Guardado en {Too_h}")
    	os.system("python3 CyTools.py")
    elif info_e == 9:
        Too_i = input("Escriba la ruta: ")
        git.Git(f"{Too_i}").clone("https://github.com/jonstewart/foremost")
        print(f"Instalacion completada, Guardado en {Too_i}")
        os.system("python3 CyTools.py")
    elif info_e == 10:
    	Too_j = input("Escriba la ruta: ")
    	git.Git(f"{Too_j}").clone("https://github.com/p0f/p0f")
    	print(f"Instalacion completada, Guardado en {Too_j}")
    	os.system("python3 CyTools")
    elif info_e == 11:
        Too_k = input("Escriba la ruta: ")
        git.Git(f"{Too_k}").clone("https://github.com/smalot/pdfparser")
        print(f"Instalacion completada, Guardado en {Too_k}")
        os.system("python3 CyTools.py")	
    elif info_e == 12:
        Too_l = input("Escriba la ruta: ")
        git.Git(f"{Tool_l}").clone("https://github.com/volatilityfoundation/volatility")
        print(f"Instalacion completada, Guardado en {Too_l}")
    elif info_e == 13:
        Too_m = input("Escriba la ruta: ")
        git.Git(f"{Too_m}").clone("https://github.com/xplico/xplico")
        print(f"Instalacion completada, Guardado en {Too_m}")
        os.system("python3 CyTools.py")
    elif info_e == 99:
        os.system("python3 CyTools.py")
elif usuario == 6:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] Brutex \n[ 2 ] PadBuster \n[ 3 ] doork \n[ 4 ] smap \n[ 5 ] sqlmap \n[ 6 ] zaproxy \n[ 7 ] sqlmate \n[ 8 ] sqlscan \n[ 9 ] deblaze \n[ 99 ] Salir")
    info_f = int(input("===> "))
    if info_f == 1:
        To_a = input("Escriba la ruta: ")
        git.Git(f"{To_a}").clone("https://github.com/1N3/BruteX")
        print(f"Instalacion completada, Guardado en {To_a}")
        os.system("python3 CyTools.py")
    elif info_f == 2:
        t_b = input("Escriba la ruta: ")
        git.Git(f"{t_b}").clone("https://github.com/AonCyberLabs/PadBuster") 
        print(f"Instalacion completada, Guardado en {t_b}")
        os.system("python3 CyTools.py")
    elif info_f == 3:
        t_c = input("Escriba la ruta: ")
        git.Git(f"{t_c}").clone("https://github.com/AeonDave/doork")
        print(f"Instalacion completada, Guardado en {t_c}")
        os.system("python3 CyTools.py") 
    elif info_f == 4:
        t_d = input("Escriba la ruta: ")
        git.Git(f"{t_d}").clone("https://github.com/zju3dv/SMAP")
        print(f"Instalacion completada, Guardado en {t_d}")
        os.system("python3 CyTools.py")
    elif info_f == 5:
        t_e = input("Escriba la ruta: ")
        git.Git(f"{t_e}").clone("https://github.com/sqlmapproject/sqlmap")
        print(f"Instalacion completada, Guardado en {t_e}") 
        os.system("python3 CyTools.py")
    elif info_f == 6:
    	t_f = input("Escriba la ruta: ")
    	git.Git(f"{t_f}").clone("https://github.com/zaproxy/zaproxy")
    	print(f"Instalacion completada, Guardado en {t_f}")
    	os.system("python3 CyTools.py")
    elif info_f == 7:
        t_g = input("Escriba la ruta: ")
        git.Git(f"{t_g}").clone("https://github.com/s0md3v/sqlmate")
        print(f"Instalacion completada, Guardado en {t_g}")
        os.system("python3 CyTools.py")
    elif info_f == 8:
        t_h = input("Escriba la ruta: ")
        git.Git(f"{t_h}").clone("https://github.com/Cvar1984/sqlscan")
        print(f"Instalacion completada, Guardado en {t_h}")
        os.system("python3 CyTools.py")
    elif info_f == 9:
        t_i = input("Escriba la ruta: ")
        git.Git(f"{t_i}").clone("https://github.com/SpiderLabs/deblaze")
        print(f"Instalacion completada, Guardado en {t_i}")
        os.system("python3 CyTools.py")
    elif info_f == 99:
        os.system("python3 CyTools.py")
    else:
         print("ERROR!!!")
         os.system("python3 CyTools.py")
elif usuario == 7:
	os.system("clear")
	print(banner_x)
	print("\n[ 1 ] DHCPig \n[ 2 ] torshammer \n[ 3 ] termineter \n[ 4 ] santet-online \n[ 5 ] hydra [ 99 ] Salir")
	info_z = int(input("===> "))
	if info_z == 1:
		v_a = input("Escriba la ruta: ")
		git.Git(f"{v_a}").clone("https://github.com/kamorin/DHCPig")
		print(f"Instalacion completada, Guardado en {v_a}")
		os.system("python3 CyTools.py")
	elif info_z == 2:
	    v_b = input("Escriba la ruta: ")
	    git.Git(f"Instalacion completada, Guardado en {v_b}")
	    os.system("python3 CyTools.py")
	elif info_z == 3:
	    v_c = input("Escriba la ruta: ")
	    git.Git(f"{v_c}").clone("https://github.com/rsmusllp/termineter")
	    print(f"Instalacion completada, Guardado en {v_c}")
	    os.system("python3 CyTools.py")
	elif info_z == 4:
	    v_d = input("Escriba la ruta: ")
	    git.Git(f"v_d").clone("https://github.com/Gameye98/santet-online")
	    print(f"Instalacion completada, Guardado en {v_d}")
	    os.system("python3 CyTools.py")
	elif info_z == 5:
	    v_e = input("Escriba la ruta: ") 
	    git.Git(f"{v_e}").clone("https://github.com/vanhauser-thc/thc-hydra")
	    print(f"Instalacion completada, Guardado en {v_e}")
	    os.system("python3 CyTools.py")
	elif info_z == 99:
	    os.system("python3 CyTools.py")
	else:
	    print("ERROR!!!!")
	    os.system("python3 CyTools.py")
elif usuario == 8:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] Responder \n[ 2 ] SocialBox \n[ 3 ] Bettercap \n[ 4 ] Dnschef \n[ 5 ] xspy \n[ 6 ] SET \n[ 99 ] Salir")
    info_x = int(input("===> "))
    if info_x == 1:
      f_a =	input("Escriba la ruta: ")
      git.Git(f"{f_a}").clone("https://github.com/SpiderLabs/Responder")
      print(f"Instalacion completada, Guardado en {f_a}")
      os.system("python3 CyTools.py")
    elif info_x == 2:
        f_b = input("Escriba la ruta: ")
        git.Git(f"{f_b}").clone("https://github.com/Cyb0r9/SocialBox")
        print(f"Instalacion completada, Guardado en {f_b}")
        os.system("python3 CyTools.py")
    elif info_x == 3:
        f_c = input("Escriba la ruta: ")
        git.Git(f"{f_c}").clone("https://github.com/bettercap/bettercap")
        print(f"Instalacion completada, Guardado en {f_c}")
        os.system("python3 CyTools.py")
    elif info_x == 4:
        f_d = input("Escriba la ruta: ")
        git.Git(f"{f_d}").clone("https://github.com/iphelix/dnschef")
        print(f"Instalacion completada, Guardado en {f_d}")
        os.system("python3 CyTools.py")
    elif info_x == 5:
        f_e = input("Escriba la ruta: ")
        git.Git(f"{f_e}").clone("https://github.com/mnp/xspy")
        print(f"Instalacion completada, Guardado en {f_e}")
        os.system("python3 CyTools.py")
    elif info_x == 6:
    	f_f = input("Escriba la ruta: ")
    	git.Git(f"{f_f}").clone("https://github.com/trustedsec/social-engineer-toolkit")
    	print(F"Instalacion completada, Guardado en {f_f}")
    	os.system("python3 CyTools.py")
    elif info_x == 99:
        os.system("python3 CyTools.py")
    else:
        print("ERROR!!!")
        os.system("python3 CyTools.py")
elif usuario == 9:
	os.system("clear")
	print(banner_x)
	print("\n[ 1 ] Hydra \n[ 2 ] Medusa \n[ 3 ] Hashcat \n[ 4 ] Cupp \n[ 5 ] Crunch \n[ 99 ] Salir")
	info_y = int(input("===> "))
	if info_y == 1:
		h_a = input("Escriba la ruta: ")
		git.Git(f"{h_a}").clone("https://github.com/vanhauser-thc/thc-hydra")
		print(f"Instalacion completada, Guardado en {h_a}")
		os.system("python3 CyTools.py")
	elif info_y == 2:
	    h_b = input("Escriba la ruta: ")
	    git.Git(f"{h_b}").clone("https://github.com/pymedusa/Medusa")
	    print(f"Instalacion completada, Guardado en {h_b}")
	    os.system("python3 CyTools.py")
	elif info_y == 3:
	    h_c = input("Escriba la ruta: ")
	    git.Git(f"{h_c}").clone("https://github.com/hashcat/hashcat")
	    print(f"Instalacion completada, Guardado en {h_c}")
	    os.system("python3 CyTools.py")
	elif info_x == 4:
	    h_d = input("Escriba la ruta: ")
	    git.Git(f"{h_d}").clone("https://github.com/Mebus/cupp")
	    print(f"Instalacion completada, Guardado en {h_d}")
	    os.system("python3 CyTools.py")
	elif info_x == 5:   
	    h_e = input("Escriba la ruta: ")
	    git.Git(f"{h_e}").clone("https://github.com/crunchsec/crunch")
	    print(f"Instalacion completada , Guardado en {h_e}")
	    os.system("python3 CyTools.py")
	elif info_x == 99:
		os.system("python3 CyTools.py")
	else: 
	    print("ERROR!!!")
	    os.system("python3 CyTools.py")
elif usuario == 10:
	os.system("clear")
	print(banner_x)
	print("\n[ 1 ] Ridenum \n[ 2 ] pwnat \n[ 3 ] nishang \n[ 4 ] httptunnel \n[ 5 ] dbd \n[ 6 ] PowerSploit \n[ 7 ] Intersect-2.5 \n[ 99 ] Salir")
	info_cd = int(input("Escriba la ruta: "))
	if info_cd == 1:
		z_a = input("Escriba la ruta: ")
		git.Git(f"{z_a}").clone("https://github.com/trustedsec/ridenum")
		print(f"Instalacion completada, Guardado en {z_a}")
		os.sytem("python3 CyTools.py")
	elif info_cd == 2:
	    z_b = input("Escriba la ruta: ")
	    git.Git(f"{z_b}").clone("https://github.com/samyk/pwnat")
	    print(f"Instalacion completada, Guardado en {z_b}")
	    os.system("python3 CyTools.py")
	elif info_cd == 3:
	    z_c = input("Escriba la ruta: ")
	    git.Git(f"{z_c}").clone("https://github.com/samratashok/nishang")
	    print(f"Instalacion completada, Guardado en {z_c}")
	    os.system("python3 CyTools.py")
	elif info_cd == 4:
	    z_d = input("Escriba la ruta: ")
	    git.Git(f"{z_d}").clone("https://github.com/larsbrinkhoff/httptunnel")
	    print(f"Instalacion completada, Guardado en {z_d}")
	    os.system("python3 CyTools.py")
	elif info_cd == 5:
	    z_e = input("Escriba la ruta: ")
	    git.Git(f"{z_e}").clone("https://github.com/gitdurandal/dbd")
	    print(f"Instalacion completada, Guardado en {z_e}")
	    os.system("python3 CyTools.py")
	elif info_cd == 6:
	    z_f = input("Escriba la ruta: ")
	    git.Git(f"{z_e}").clone("https://github.com/PowerShellMafia/PowerSploit")
	    print(f"Instalacion completada, Guardado en {z_f}")
	    os.system("python3 CyTools.py")
	elif info_cd == 7:
	    z_g = input("Escriba la ruta: ")
	    git.Git(f"{z_g}").clone("https://github.com/deadbits/Intersect-2.5")
	    print(f"Instalacion completada, Guardado en {z_g}")
	    os.system("python3 CyTools.py")
	elif info_cd == 99:
	    os.system("python3 CyTools.py")
	else:
	     print("ERROR!!!")
	     os.system("python3 CyTools.py") 
elif usuario == 11:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] IP-TRACER \n[ 2 ] IPGeoLocation \n[ 3 ] trackout \n[ 4 ] trape \n[ 5 ] IP-FY \n[ 99 ] Salir")
    info_hh = int(input("===> "))
    if info_hh == 1:
    	w_a = input("Escriba la ruta: ")
    	git.Git(f"{w_a}").clone("https://github.com/rajkumardusad/IP-Tracer")
    	print(f"Instalacion completada, Guardado en {w_a}")
    	os.system("python3 CyTools.py")
    elif info_hh == 2:
        w_b = input("Escriba la ruta: ")
        git.Git(f"{w_b}").clone("https://github.com/maldevel/IPGeoLocation")
        print(f"Instalacion completada, Guardado en {w_b}")
        os.system("python3 CyTools.py")
    elif info_hh == 3:
        w_c = input("Escriba la ruta: ")
        git.Git(f"{w_c}").clone("https://github.com/abaykan/TrackOut")
        print(f"Instalacion completada, Guardado en {w_c}")
        os.system("python3 CyTools.py")
    elif info_hh == 4:
        w_d = input("Escriba la ruta: ")
        git.Git(f"{w_d}").clone("https://github.com/jofpin/trape")
        print(f"Instalacion completada, Guardado en {w_d}")
        os.system("python3 CyTools.py")
    elif info_hh == 5:
        w_e = input("Escriba la ruta: ")
        git.Git(f"{w_e}").clone("https://github.com/T4P4N/IP-FY")
        print(f"Instalacion completada, Guardado en {w_e}")
        os.system("python3 CyTools.py")
    elif info_hh == 6:
        os.system("python3 CyTools.py")

    else:
        print("ERROR!!!")
        os.system("python3 CyTools.py")
elif usuario == 12:
    os.system("python3 setup.py")

elif usuario == 13:
    os.system("clear")
    print(banner_x)
    print("\n[ 1 ] SETSMS \n[ 2 ] TBomb")
    info_mm = int(input("===> "))
    if info_mm == 1:
    	l_a = input("Escriba la ruta: ")
    	git.Git(f"{l_a}").clone("https://github.com/Darkmux/SETSMS")
    	print(f"Instalacion completada, Guardado en {l_a}")
    	os.system("python3 CyTools.py")
    elif info_mm == 2:
        l_b = input("Escriba la ruta: ")
        git.Git(f"{l_b}").clone("https://github.com/TheSpeedX/TBomb")
        print(f"Instalacion completada, Guardado en {l_b}")
        os.system("python3 CyTools.py")
    else:
        print("ERROR!!!!")
        os.system("python3 CyTools.py")
else:
    print("ERROR!!!")
    os.system("python3 CyTools.py")            	




    	 











	             	



                         



