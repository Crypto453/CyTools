import colorama 
import os
import git

os.system("clear")
os.system("python3 banner.py")
print("\n[ 1 ] LITEDDOS \n[ 2 ] Hammer \n[ 3 ] Slowloris \n[ 4 ] hulk [ 99 ] Volver")
info_bb = int(input("===> "))
if info_bb == 1:
	r_a = input("Escriba la ruta: ")
	git.Git(f"{r_a}").clone("https://github.com/4L13199/LITEDDOS")
	print(f"Instalacion completada, Guardado en {r_a}")
	os.system("python3 CyTools.py")
elif info_bb == 2:
    r_b = input("Escriba la ruta: ")
    git.Git(f"{r_b}").clone("https://github.com/cyweb/hammer")
    print(f"Instalacion completada, Guardado en {r_b}")
    os.system("python3 CyTools.py")
elif info_bb == 3:
    r_c = input("Escriba la ruta: ")
    git.Git(f"{r_c}").clone("https://github.com/gkbrk/slowloris")
    print(f"Instalacion completada, Guardado en {r_c}")
    os.system("python3 CyTools.py")
elif info_bb == 4:
    r_d = input("Escriba la ruta: ")
    git.Git(f"{r_d}").clone("https://github.com/gkbrk/slowloris")
    print(f"Instalacion completada, Guardado en {r_d}")
    os.system("python3 CyTools.py")
elif info_bb == 5:
    os.system("python3 CyTools.py")
else:
	print("ERROR!!!!!!!!")
	os.system("python3 CyTools.py")
