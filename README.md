<div align="center">

# 🚀 FastAPI CI/CD Pipeline
### Self-Hosted Local Infrastructure

[![CI/CD Pipeline](https://github.com/AvotraAder/DevOps-Project-1/actions/workflows/deploy.yml/badge.svg)](https://github.com/AvotraAder/DevOps-Project-1/actions)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Debian](https://img.shields.io/badge/Debian_12-A81D33?style=flat-square&logo=debian&logoColor=white)](https://www.debian.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

End-to-end automated CI/CD pipeline for a **FastAPI** application containerized with **Docker**, deployed on a **Debian (VMware)** virtual infrastructure via a **GitHub Self-Hosted Runner**.

[Features](#-features) •
[Architecture](#-architecture) •
[Installation](#-installation) •
[Usage](#-usage) •
[Author](#-author)

</div>

---

## ✨ Features

- ⚡ **Automatic deployment** on every `push` to `main`
- 🧪 **Unit tests** automatically executed with Pytest
- 🐳 **Docker containerization** with automatic restart
- 🏠 **100% self-hosted infrastructure**, zero cloud costs
- 📖 **Auto-generated Swagger documentation** by FastAPI

---

## 🏗 Architecture

```mermaid
flowchart LR
    A[💻 Developer] -->|git push| B[📦 GitHub Repository]
    B -->|Trigger| C[⚙️ GitHub Actions CI]
    C -->|pytest| D{Tests OK?}
    D -->|✅| E[🖥️ Debian VM<br/>Self-Hosted Runner]
    D -->|❌| F[🚫 Pipeline Stop]
    E -->|docker build & run| G[🚀 App Live<br/>:8000]

    style A fill:#4A90D9,color:#fff
    style B fill:#24292e,color:#fff
    style C fill:#2088FF,color:#fff
    style E fill:#A81D33,color:#fff
    style G fill:#2ECC71,color:#fff
```

### Pipeline Workflow

| Step | Environment | Actions |
|---|---|---|
| **1. Test** | ☁️ GitHub Cloud | Code checkout → Setup Python 3.11 → Install dependencies → `pytest` |
| **2. Deploy** | 🖥️ Debian VM (self-hosted) | `docker build` → stop/remove old container → run new container (`--restart always`) |

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| API Framework | Python 3.11 · FastAPI |
| Containerization | Docker |
| CI/CD Orchestration | GitHub Actions |
| Deployment Environment | Debian 12 (VMware, NAT network) |
| Deployment Agent | GitHub Self-Hosted Runner (systemd service) |

---

## 📁 Repository Structure

```
DevOps-Project-1/
├── .github/
│   └── workflows/
│       └── deploy.yml      # Automated CI/CD pipeline
├── src/
│   ├── app.py              # FastAPI application code
│   ├── requirements.txt     # Python dependencies
│   └── test_app.py         # Pytest unit tests
├── Dockerfile                # Docker image build instructions
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Debian 12 VM (VMware, NAT or bridge network)
- Administrator access (`sudo`) on the VM
- GitHub repository with runner configuration rights

### 1. Install Docker on the VM

```bash
sudo apt update && sudo apt install -y docker.io
sudo usermod -aG docker $USER
newgrp docker
```

### 2. Install GitHub Runner

```bash
mkdir ~/actions-runner && cd ~/actions-runner

# Configure using commands provided in
# Settings > Actions > Runners > New self-hosted runner
./config.sh --url https://github.com/AvotraAder/DevOps-Project-1 --token <YOUR_TOKEN>

# Install and start the systemd service
sudo ./svc.sh install
sudo ./svc.sh start
```

> 💡 The runner now runs in the background and listens for jobs triggered by GitHub Actions.

---

## 🧪 Usage

Once the pipeline has executed successfully:

**1. Get the VM's IP address**

```bash
hostname -I
```

**2. Access the application**

| Resource | URL |
|---|---|
| 🌐 Main endpoint | `http://<YOUR_VM_IP>:8000/` |
| 📖 Swagger documentation | `http://<YOUR_VM_IP>:8000/docs` |
| 📘 ReDoc documentation | `http://<YOUR_VM_IP>:8000/redoc` |

---

## 🔧 Pipeline Configuration

The `.github/workflows/deploy.yml` file runs automatically on every `push` to the `main` branch:

**Job 1: `test` (GitHub Cloud)**
- Retrieves code
- Installs Python 3.11 and dependencies
- Runs unit tests with `pytest`

**Job 2: `deploy` (Self-Hosted Debian VM)**
- Local runner intercepts the task
- Builds (`docker build`) the new Docker image
- Stops and removes old container if it exists
- Launches new container with automatic restart (`--restart always`)

---

## 🗺 Roadmap

- [ ] Add reverse proxy (Nginx / Traefik) + HTTPS
- [ ] Slack/Discord notifications on deployment failure
- [ ] Monitoring with Prometheus + Grafana
- [ ] Integration tests in addition to unit tests
- [ ] Multi-stage Docker builds for optimization

---

## 🔍 Troubleshooting

**Runner is not showing up in GitHub Actions**
```bash
# Check runner status
cd ~/actions-runner && ./run.sh
```

**Docker permission denied error**
```bash
sudo usermod -aG docker $USER
newgrp docker
# Restart the runner
sudo systemctl restart actions.runner
```

**Application not accessible from host machine**
```bash
# Verify container is running
docker ps

# Check VM network configuration
hostname -I
```

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Avotra Ader**

[![GitHub](https://img.shields.io/badge/GitHub-DevOps--Project--1-181717?style=flat-square&logo=github)](https://github.com/AvotraAder/DevOps-Project-1)
[![Twitter](https://img.shields.io/badge/Twitter-@AvotraAder-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com)

---

<div align="center">

If this project helped you, consider giving it a ⭐!

[⬆ Back to top](#-fastapi-cicd-pipeline)

</div>
