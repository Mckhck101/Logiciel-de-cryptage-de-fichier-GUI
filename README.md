# Logiciel de Cryptographie Mackedzoa

## Présentation

**Mackedzoa** est un logiciel de cryptographie développé en Python avec une interface graphique Tkinter.
Il permet de chiffrer, déchiffrer, signer et comparer des fichiers, ainsi que de générer des empreintes cryptographiques.

Le logiciel utilise principalement les algorithmes suivants :

* **SHA-256** : génération de hash
* **PBKDF2-HMAC-SHA256** : dérivation de clé et polymorphisme
* **MD5** : signature de fichiers
* **XOR avec clé dérivée SHA-256** : chiffrement et déchiffrement de fichiers

Extension propriétaire utilisée : **.mck**

---

## Fonctionnalités principales

### 1. Chiffrement de fichier

* Sélection d’un fichier
* Saisie d’une clé
* Génération d’un fichier chiffré avec extension `.mck`

### 2. Déchiffrement de fichier

* Sélection d’un fichier `.mck`
* Saisie de la clé correspondante
* Restauration du fichier original

### 3. Génération de hash

* Hash SHA-256 d’un texte ou mot de passe

### 4. Polymorphisme cryptographique

* Génération d’un hash avec :

  * sel aléatoire
  * nombre de tours
  * PBKDF2-HMAC-SHA256

### 5. Signature de fichier

* Génération d’une empreinte MD5 d’un fichier

### 6. Comparaison de fichiers

* Vérification si deux fichiers sont identiques via leur signature

### 7. Partage de fichiers

* Copie de fichiers dans le dossier **share**
* Génération d’une page HTML listant les fichiers

---

## Installation

### Prérequis

Python 3.7 ou supérieur

Modules requis :

```
tkinter
pyperclip
hashlib
shutil
pathlib
pickle
```

Installer pyperclip si nécessaire :

```
pip install pyperclip
```

---

## Lancement

Exécuter le script principal :

```
python Hasher 3 GUI.py
```

---

## Utilisation

### Chiffrer un fichier

1. Cliquer sur **Fichier → Ouvrir**
2. Sélectionner le fichier
3. Entrer une clé
4. Cliquer sur **Outils → Chiffrage-Fichier**
5. Sauvegarder

Résultat :

```
fichier.txt.mck
```

---

### Déchiffrer un fichier

1. Ouvrir le fichier `.mck`
2. Entrer la clé
3. Cliquer sur **Déchiffrage**

---

### Générer un hash

Entrer un texte puis cliquer sur :

```
Chiffrer
```

---

### Obtenir la signature d’un fichier

Menu :

```
Outils → Signature-Fichier
```

---

## Structure du projet

```
Mackedzoa/
│
├── main.py
├── README.txt
├── licence.txt
├── share/
├── Serveur.exe
└── fichiers .mck
```

---

## Sécurité

Important :

* La sécurité dépend de la clé choisie
* Ne perdez jamais votre clé
* Un fichier chiffré sans la clé est irrécupérable

---

## Auteur

Edzoa Ahanda Cyrille Mackenzy Bryan
Projet : Mackedzoa Cryptography Software
Email : [Mackedzoa@gmail.com](mailto:Mackedzoa@gmail.com)

Copyright © 2024 Mackedzoa
Tous droits réservés

---

## Licence

Ce logiciel est distribué sous la licence **Mackedzoa Licence 1.0**.
Voir le fichier :

```
licence.txt
```

---
### Avis au futur lecteur : Readme dev avec IA.
