```markdown
# 🚀 FastAPI CI/CD Pipeline — Local Self-Hosted Infrastructure

[![CI/CD Pipeline](https://github.com/AvotraAder/DevOps-Project-1/actions/workflows/deploy.yml/badge.svg)](https://github.com/AvotraAder/DevOps-Project-1/actions)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

Un pipeline CI/CD automatisé de bout en bout pour une application **FastAPI** containerisée avec **Docker**, déployée sur une infrastructure virtuelle **Debian (VMware)** via un **GitHub Self-Hosted Runner**.

---

## 📌 Architecture du Projet

```text
[ Developer PC ] --( git push )--> [ GitHub Repository ]
                                            |
                                            | (Triggers Workflow)
                                            v
                                  [ GitHub Actions CI ]
                                  - Run Pytest Unit Tests
                                            |
                                            | (Dispatch Job)
                                            v
                                  [ Local Debian VM ]
                                  - GitHub Self-Hosted Runner
                                  - Docker Build & Container Run
                                            |
                                            v
                                 [ App Online: Port 8000 ]

```

---

## 🛠️ Tech Stack & Outils

* **Framework API :** Python 3.11 / FastAPI
* **Conteneurisation :** Docker
* **CI/CD Orchestration :** GitHub Actions
* **Environnement de Déploiement :** VM Debian 12 (VMware - Network NAT)
* **Agent de Déploiement :** GitHub Self-Hosted Runner (service Systemd)

---

## 📁 Structure du Dépôt

```text
DevOps-Project-1/
├── .github/
│   └── workflows/
│       └── deploy.yml      # Pipeline CI/CD automatisé
├── src/
│   ├── main.py             # Code de l'application FastAPI
│   ├── requirements.txt    # Dépendances Python
│   └── test_main.py        # Tests unitaires Pytest
├── Dockerfile              # Instructions de build de l'image Docker
├── .gitignore
└── README.md

```

---

## ⚙️ Fonctionnement du Pipeline CI/CD

Le workflow `.github/workflows/deploy.yml` s'exécute automatiquement à chaque `push` sur la branche `main` :

1. **Job `test` (Cloud GitHub) :**
* Récupération du code.
* Installation de Python 3.11 et des dépendances.
* Exécution des tests unitaires avec `pytest`.


2. **Job `deploy` (Self-Hosted Debian VM) :**
* Le Runner local intercepte la tâche.
* Construction (`docker build`) de la nouvelle image Docker.
* Arrêt et suppression de l'ancien conteneur s'il existe.
* Lancement du nouveau conteneur avec relance automatique (`--restart always`).



---

## 🚀 Déploiement & Configuration Locale

### Préréquis sur la VM Debian

1. **Installer Docker & configurer les droits :**
```bash
sudo apt update && sudo apt install -y docker.io
sudo usermod -aG docker $USER
newgrp docker

```


2. **Installer le Runner GitHub en service arrière-plan :**
```bash
mkdir ~/actions-runner && cd ~/actions-runner
# Télécharger et configurer via les commandes de votre dépôt (Settings > Actions > Runners)
./config.sh --url [https://github.com/AvotraAder/DevOps-Project-1](https://github.com/AvotraAder/DevOps-Project-1) --token <TON_TOKEN>

# Installer le service systemd
sudo ./svc.sh install
sudo ./svc.sh start

```



---

## 🧪 Tester l'Application en Local

Une fois le pipeline exécuté avec succès :

1. Récupérer l'adresse IP de la VM Debian :
```bash
hostname -I

```


2. Accéder à l'API depuis le navigateur du PC hôte :
* **Endpoint principal :** `http://<IP_DE_TA_VM>:8000/`
* **Documentation Swagger interactive :** `http://<IP_DE_TA_VM>:8000/docs`



---

## 👤 Auteur

* **Avotra Ader** - *[DevOps-Project-1](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/AvotraAder/DevOps-Project-1)*

```

```
