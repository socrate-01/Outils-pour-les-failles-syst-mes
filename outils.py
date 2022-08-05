#!/usr/bin/python3
import nmap
import os
sc = nmap.PortScanner()
print("""                                  __          
  __________   ________________ _/  |_  ____  
 /  ___/  _ \_/ ___\_  __ \__  \\   __\/ __ \ 
 \___ (  <_> )  \___|  | \// __ \|  | \  ___/ 
/____  >____/ \___  >__|  (____  /__|  \___  >
     \/           \/           \/          \/ """)

#Ensuite on créé la fonction qui nous permettra d'effectuer les tâches élucidées au préalable
def main():
    s=input("1-scanner le réseau\n2-détecter les problèmes\n3-exploitation\nVeuiller entrer un chiffre parmi ces options : ")
    if s=='1':
        nmap()
    if s=='2':
        vuln()
    if s=='3':
        os.system('./msfconsole')
    else:
        print("Veuiller entrer un chiffre compris entre 1 et 3")

def nmap():
    print("------------------Scanner Réseau--------------")
    ip=input("\nVeuiller renseigner vôtre addresse ip svp : ")
    sc.scan(ip,"1-1024")
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    print("------------------Bonjour--------------")
    ip=input("\nVeuiller renseigner vôtre addresse ip svp : ")
    print(os.system('nmap -sV --script=vulscan/vulscan.nse '+ip))






#Définir main comme étant la fonction par défaut du script
if __name__== "__main__":
    main()