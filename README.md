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
