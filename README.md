
# Osint-serv  
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org)  
Outil d’OSINT polyvalent avec fonctions de lookup, profilage, test de charge, crash-site et plus.

---

## Fonctionnalités

- **Lookup complet :**  
  - Recherche de personnes, usernames, adresses, IPs, emails, BSSID, téléphones
  - Tracer des emails jusqu'à leur IP
  - Graph Facebook, recherche Google, Instagram, Twitter
- **Profiler :**  
  - Créer, visualiser et analyser des profils de cibles
- **Crash-site :**  
  - Envoie massif de paquets lourds pour test de résistance
- **Big Serv :**  
  - Test de charge personnalisé (requêtes, cadence, etc.)
- **Hash Decrypter**

---

## Installation

### Termux (Android) :
```bash
pkg update && pkg upgrade
pkg install git python
git clone git@github.com:Ttrhh/Osint-serv.git
cd Osint-serv
pip install -r requirements.txt
python3 LittleBrother.py
```

### Linux :
```bash
sudo apt update && sudo apt install git python3 python3-pip
git clone git@github.com:Ttrhh/Osint-serv.git
cd Osint-serv
pip3 install -r requirements.txt
python3 LittleBrother.py
```

---

## Utilisation

Lance simplement le script :
```bash
python3 LittleBrother.py
```

Navigue dans le menu principal :

```
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Test de charge (Big Serv)
 [5] Crash-site
 [6] Clear country
 [7] Quitter
```

---

## Avertissement

> Ce projet est fourni uniquement à des fins éducatives.  
> L’auteur **ne cautionne** aucune utilisation illégale de ce script.  
> **Vous êtes responsable** de vos actions.

---

## Auteur

Développé par [Ttrhh](https://github.com/Ttrhh)  
Projet : [Osint-serv](https://github.com/Ttrhh/Osint-serv)

---
