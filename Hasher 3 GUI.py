"""
========================================================================
Partie Mackedzoa_Logiciel
========================================================================
"""

print("Monter avec python 3.7.3")
print('Logiciel de Mackedzoa')
print("Cryptage pbkdf2_hmac")
print("Mackedzoa@gmail.com")
print("\t Mackedzoa¢2020 Tous les droits réservés")

"""
========================================================================
Partie IMPORTATITON DE BIBLIOTHEQUE
========================================================================
"""

from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from os import path
import socketserver
import http.server
import webbrowser
import pyperclip
import binascii
import hashlib
import pathlib
import socket
import shutil
import pickle
import os

"""
========================================================================
Partie DEFINITION DE FONCTION
========================================================================
"""

Doc_Chy = '''Logiciel by Me ¢ 2024 Tous les droits réservés
    Bonjour, je suis mackedzoa le developpeur de ce logiciel
    Dans la section : Option (ou Chiffrement) nous devez savoir ceci :
    
    \n
        * Le chiffrement par le bouton  "-> Chiffrer" se fait via l'algorithme "pbkdf2_hmac"
        * Sachez que le 'vide' laisser dans la barre d'insertion du clé est un 'caractère' donc peut être chiffrer par la fonction citée plus haut
        * Il est possible avec l'option 'Copier Hash' d'obtenir un hash via l'algorithme "pbkdf2_hmac" sans avoir saisi une clé ou sans avoir envoyer celui-ci !!!
        * Il est possible avec l'option 'Copier Sign' de copier la signature d'un fichier, directemetn sans aller aux outlis signatures. 
        * Sachez également que l'option 'Polymorphe' vous donnera des indications sur les 'options' utilisées par l'algorithme de chiffrement
        * L'option 'Polymorphe' est doté d'une copie automatiquer dans le presse papier, donc faites attention, de ne rien avoir d'important dans le presse papier avant de l'utiliser !!! 
    \n
    
    Si vous avez des améliorations à apporter écrivez à : Mackedzoajunior@gmail.com
    -------------------------------------------------------------------------------'''

Doc_Chy2 = '''Les menus sont les suivants :
        * Fichier : Permet la selection des fichiers pour le partage ou pour la manipulation, elle est également utilisée pour annuler toute opération, fermer une fenêtre ou encore Enreigistrer le fichier crypté.
        * Options : Permet l'utlisation des fonctionnalités sur les chaînes c-à-d effacer l'écran, copier la signature ou des hash ainsi que d'activer la fonction ploymorphe... Elle est également dotée d'une fonction de documentation personnelle.
        * Outils  : Permet le partage de fichier, le cryptage et le décryptage de fichier de plus en permet de comparer deux fichiers par leurs signatures.
        * Aide    : Permet d'approfondir les connaissance sur ce logiciel.
    \n
    Utilisation et particularités :
    \n
        Comment Partager un fichier ? Il suffit de cliquer sur le menu 'Fichier' puis sur 'Partager' choisir un fichier à partager puis aller à l'onglet Outils. \nEt cliquer sur 'Partager-Fichier'\n\n

        Comment Chiffer un fichier  ? Ici vous devez cliquer sur le menu 'Fichier' puis sur 'Ouvrir' choisir un fichier à modifier puis saisir *Une clé* dans la zone de saisie le plus haute. \nEnsuite aller à l'onglet Outils et cliquer sur 'Chiffrage-Fichier'. Enfin cliquez sur 'Enreigister sous' dans le menu 'Fichier' et obtener le fichier crypté et avec .mck comme extension\n\n

        Comment Déchiffer un fichier ? Ici vous devez cliquer sur le menu 'Fichier' puis sur 'Ouvrir' choisir un fichier à modifier puis saisir *La clé*\n dans la boîte de dialogue le plus haute. \nEnsuite aller à l'onglet Outils et cliquer sur 'DéChiffrage-Fichier'. Enfin cliquez sur 'Enreigister sous' dans le menu 'Fichier' et obtener le fichier décrypté et sans .mck comme extension\n\n

        Comment obtenir la signature d'un fichier  ? Facile :) , cliquer sur le menu 'Fichier' puis sur 'Ouvrir' choisir un fichier à modifier puis aller à l'onglet Outils et cliquer sur 'Signature-Fichier'\n\n

        Comment comparer 2 fichiers ? cliquer sur le menu 'Fichier' puis sur 'Modifier-Fichier' choisir un fichier à comparer, faites un clique gauche dans la zone de saisie 'Fichier1' et coller le nom du premier fichier... \nEnsuite, reffaite l'opreation cette fois-ci dans la zone de saisie 'Fichier2' puis aller à l'onglet Outils et cliquer sur 'Comparaison-2-Fichiers'\n\n

        Comment comment obtenir un hash ? Saisissez simplementm la clé à hasher (Crée une empreinte) et enfin cliquer sur bouton Chiffrer.\n\n

        C'est quoi le plymorphisme ? C'est simplement la création d'une empreinte sous plusieurs formes selon certain paramètres aui vous seront donnés.\n Pour réaliser le polymorphisme, il est simple : Saisissez la clé à hasher, puis aller à l'onglet 'Option' et cliquer sur 'Polymorphisme'\n\n

'''

def Test():
    os.system("Readme.txt")

def Hashe():
    code_compris = code_entree.get()
    code_compris = code_compris.encode()
    entre_crypte = hashlib.sha256(code_compris).hexdigest()
    return entre_crypte

def Polymorphisme():
    code_compris = code_entree.get()
    code_compris = code_compris.encode()
    inter = os.O_RANDOM
    salt = os.urandom(16)
    masque = hashlib.pbkdf2_hmac("sha256", code_compris , salt , inter)
    hashex = binascii.hexlify(masque)
    label.config(text=f'Votre hash polymorphe est : {hashex} \nVotre sel est : {salt} \nVotre tour est : {inter}')
    pyperclip.copy(f'Votre hash polymorphe est : {hashex} \nVotre sel est : {salt} \nVotre tour est : {inter}')


def Info():
    info_sup = Toplevel(present)
    info_sup.title('''À propos de Mackedzoa 2024 GUI''')
    info = Label(info_sup, text=Doc_Chy)
    info.pack()

def Info2():
    info_sup = Toplevel(present)
    info_sup.title('''À propos de Mackedzoa 2024 GUI''')
    info = Label(info_sup, text=Doc_Chy2)
    info.pack()
    
def Internet():
    webbrowser.open("http://www.mackedzoa.e-monsite.com")
 
def Presspapier():
    pyperclip.copy(Hashe())

def Afficher():
    label.config(text=f'Votre hash est : {Hashe()}')

def Effacer():
    label.config(text='')
    pyperclip.copy('')
    label4.config(text='')

def generate_html():
    files = os.listdir("share")

    html_links = ""
    for filename in files:
        if(filename != "Serveur.exe" and filename != 'index.html' and filename != "_internal"):
            file_url = f"http://localhost/{filename}"
            html_links += f"<a href='{file_url}'>{filename}</a><br>\n"

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Liste des fichiers partagés</title>
    </head>
    <body>
        <div style="display: flex;flex-direction: row;align-items: center;margin: 0 auto;width: 80%;font-family: Arial, sans-serif;">
            <p style="font-size: 24px;font-weight: bold;margin-right: 10px;">Liste des fichiers partagés</p>
            <p style="font-size: 16px;line-height: 1.5;">{html_links}</p>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w") as f:
        f.write(html_template.format(html_links=html_links))
    
def Server():
    generate_html()
    shutil.copy("index.html","share")
    os.chdir("share")
    os.system("Serveur.exe")
    label.config(text="Serveur demarré sur le port 80")
    os.chdir("..")
    label.config(text="Serveur fermé")
    
def Sign():
    filePath = code_entree3.get()
    fileObj = open(filePath, 'rb')
    d = fileObj.read(8096)
    m = hashlib.md5(d)
    while True:
        d = fileObj.read(8096)
        if not d:
                break
                pass
    return m.hexdigest()

def AfficheSign():
    label4.config(text=f'La signature de {code_entree3.get()} est : {Sign()}')
    
def Sign1():
    filePath1 = code_entree1.get()
    fileObj1 = open(filePath1, 'rb')
    d1 = fileObj1.read(8096)
    m1 = hashlib.md5(d1)
    while True:
        d1 = fileObj1.read(8096)
        if not d1:
                break
                pass
    return m1.hexdigest()

def Sign2():
    filePath2 = code_entree2.get()
    fileObj2 = open(filePath2, 'rb')
    d2 = fileObj2.read(8096)
    m2 = hashlib.md5(d2)
    while True:
        d2 = fileObj2.read(8096)
        if not d2:
                break
                pass
    return m2.hexdigest()

def Comparer():
    if Sign1() == Sign2():
        return 1
    else :
        return 2

def AfficheCompa():
    if Comparer() == 1:
        label4.config(text="Vos fichiers sont identiques")
    elif Comparer() == 2:
        label4.config(text=f"Vos fichier ne sont pas identiques \nLa signature de {code_entree1.get()} est : {Sign1()}\nLa signature de {code_entree2.get()} est : {Sign2()}")
    else :
        label4.config(text="Erreur dans le processus")
        
def Crypt():
    Entree = code_entree3.get()
    Sortie = Entree+".mck"
    
    cle = code_entree.get()
    cles = hashlib.sha256(cle.encode('utf-8')).digest()

    with open(Entree,'rb') as fic_entree:
        with open(Sortie,'wb') as fic_sorie:
            i = 0
            while fic_entree.peek():
                j = ord(fic_entree.read(1))
                k = i % len(cles)
                l = bytes([j^cles[k]])
                fic_sorie.write(l)
                i = i + 1
    label4.config(text=f"Le {Entree} crypté en {Sortie}")

def Decrypt():
    Entree = code_entree3.get()
    Sortie = Entree.rstrip(".mck")
    print(f"{Sortie}")

    cle = code_entree.get()
    cles = hashlib.sha256(cle.encode('utf-8')).digest()

    with open(Entree,'rb') as fic_entree:
        with open(Sortie,'wb') as fic_sorie:
            i = 0
            while fic_entree.peek():
                j = ord(fic_entree.read(1))
                k = i % len(cles)
                l = bytes([j^cles[k]])
                fic_sorie.write(l)
                i = i + 1
                
    dest = filedialog.askdirectory()
    #dest = dest.replace('/', '\\')
    print(f"copy '{Sortie}' '{dest}'")
    #fileO = str(pathlib.Path.cwd())+ f"Sortie" 
    shutil.copy(Sortie, dest)
    #os.system(f"copy '{Sortie}' {dest}")
    label4.config(text=f"Le {Sortie} décrypté !!!")
    messagebox.showinfo("Decrypter !", "Le Fichier a été decrypté avec succes.")
    
def Reset():
    pyperclip.copy('')
    label.config(text='')
    label4.config(text='')
    os.chdir(pathlib.Path.cwd())
    #code_entree.delete()

def FicOuvert():
    fileOpen = filedialog.askopenfilename()
    shutil.copy(fileOpen, pathlib.Path.cwd())
    code_entree3.insert(INSERT, path.basename(fileOpen))
    messagebox.showinfo("Ouverture !", "Le Fichier a bien été ouvert.")

def paste_text3():
    code_entree3.insert(INSERT, pyperclip.paste())
def copy_text3():
    pyperclip.copy(code_entree3.get())
    messagebox.showinfo("Copié !", "Le texte a été copié dans le presse-papiers.")

def paste_text2():
    code_entree2.insert(INSERT, pyperclip.paste())
def copy_text2():
    pyperclip.copy(code_entree2.get())
    messagebox.showinfo("Copié !", "Le texte a été copié dans le presse-papiers.")

def paste_text1():
    code_entree1.insert(INSERT, pyperclip.paste())
def copy_text1():
    pyperclip.copy(code_entree1.get())
    messagebox.showinfo("Copié !", "Le texte a été copié dans le presse-papiers.")

def paste_text():
    code_entree.insert(INSERT, pyperclip.paste())
def copy_text():
    pyperclip.copy(code_entree.get())
    messagebox.showinfo("Copié !", "Le texte a été copié dans le presse-papiers.")

def cptoshare():
    share = str(pathlib.Path.cwd())+ "\share"
    fileO = filedialog.askopenfilename()
    shutil.copy(fileO, share)
    messagebox.showinfo("Partage !", "Le Fichier est prêt à être partager.")

def Press():
    pyperclip.copy(Sign())

def Savefile():
    choice = filedialog.askdirectory()
    choice = choice.replace('/', '\\')
    os.system(f"move *.mck {choice}")
    messagebox.showinfo("Enregistrement réussit !", "Le Fichier a bien été enregistrer.")

"""
========================================================================
Partie PROMPT
========================================================================
"""

os.system("DEl *.mck")


"""
========================================================================
Partie PARAMETRE FENETRE
========================================================================
"""

present = Tk()# present devient tkinter 
present.title("Mackedzoa Hasher 2024 All Options")

present.minsize(640, 480)
present.maxsize(1366, 768)
present.positionfrom("user")
present.sizefrom("user")
present.resizable(width=False, height=False)
present.iconbitmap('icon.ico')

"""
========================================================================
Partie MENU
========================================================================
"""

mainmenu = Menu(present)

Fichier = Menu(mainmenu, tearoff=0)
Fichier.add_command(label='Ouvrir', command=FicOuvert)

Fichier.add_separator()
Fichier.add_command(label='Partager', command=cptoshare)
Fichier.add_command(label='Enregister', command=Savefile)
Fichier.add_command(label='Réinitialiser', command=Reset)
Fichier.add_separator()
Fichier.add_command(label='Fermer', command=present.quit)

Option = Menu(mainmenu, tearoff=0)
Option.add_command(label='Effacer', command=Effacer)
Option.add_separator()
Option.add_command(label='Copier Hash', command=Presspapier)
Option.add_command(label='Copier Sign', command=Press)
Option.add_command(label='Polymorphisme', command=Polymorphisme)
Option.add_separator()
Option.add_command(label='À propos de', command=Info)

Outils = Menu(mainmenu, tearoff=0)
Outils.add_command(label='Démarrer le Partage', command=Server)
Outils.add_separator()
Outils.add_command(label='Signature-Fichier', command=AfficheSign)
Outils.add_command(label='Chiffrage-Fichier', command=Crypt)
Outils.add_command(label='Déchiffrage-Fichier', command=Decrypt)
Outils.add_separator()
Outils.add_command(label='Comparaison-2-Fichiers', command=AfficheCompa)

Aide = Menu(mainmenu, tearoff=0)
Aide.add_command(label='Documentation', command=Info2)
Aide.add_separator()
Aide.add_command(label='Site web du dev', command=Internet)

mainmenu.add_cascade(label='Fichier',menu=Fichier)
mainmenu.add_cascade(label='Option',menu=Option)
mainmenu.add_cascade(label='Outils',menu=Outils)
mainmenu.add_cascade(label='Aide',menu=Aide)

present.config(menu=mainmenu)

"""
========================================================================
Partie CONTENU
========================================================================
"""

x = Widget.winfo_width(present)
y = Widget.winfo_height(present)


label0 = Label(present, text="Saisir une clé :", font="bold", fg="green")
label0.pack()
code_entree = Entry(present, bd=10, width=25, font="bold", fg='red')
code_entree.pack()
right_click_menu0 = Menu(present, tearoff=0)
right_click_menu0.add_command(label="Copier", command=copy_text)
right_click_menu0.add_command(label="Coller", command=paste_text)
code_entree.bind("<Button-3>", lambda event: right_click_menu0.tk_popup(event.x, event.y))

label1 = Label(present, text="Fichier 1 :", font="bold", fg="green")
label1.pack(side=LEFT)
code_entree1 = Entry(present, bd=5, width=13, font="bold", fg="red")
code_entree1.pack(side=LEFT)
right_click_menu1 = Menu(present, tearoff=0)
right_click_menu1.add_command(label="Copier", command=copy_text1)
right_click_menu1.add_command(label="Coller", command=paste_text1)
code_entree1.bind("<Button-3>", lambda event: right_click_menu1.tk_popup(event.x, event.y))

code_entree2 = Entry(present, bd=5, width=13, font="bold", fg="red")
code_entree2.pack(side=RIGHT)
label2 = Label(present, text="Fichier 2 :", font="bold", fg="green")
label2.pack(side=RIGHT)
right_click_menu2 = Menu(present, tearoff=0)
right_click_menu2.add_command(label="Copier", command=copy_text2)
right_click_menu2.add_command(label="Coller", command=paste_text2)
code_entree2.bind("<Button-3>", lambda event: right_click_menu2.tk_popup(event.x, event.y))

label4 = Label(present, text="", font="bold", fg="black" , bg="yellow")
label4.pack(side=BOTTOM)

code_entree3 = Entry(present, bd=10, width=20, font="bold", fg='red')
code_entree3.pack(side=BOTTOM)
label3 = Label(present, text="Fichier :", font="bold", fg="green")
label3.pack(side=BOTTOM)
right_click_menu = Menu(present, tearoff=0)
right_click_menu.add_command(label="Copier", command=copy_text3)
right_click_menu.add_command(label="Coller", command=paste_text3)
code_entree3.bind("<Button-3>", lambda event: right_click_menu.tk_popup(event.x, event.y))

button_de_soumission = Button(present, text="-> Chiffrer", width=15, font="bold", fg="black", bg="yellow", command=Afficher)
button_de_soumission.pack()

label = Label()
label.pack()

present.mainloop()
