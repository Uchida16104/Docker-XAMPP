# Docker XAMPP

A portable Docker-based XAMPP development environment built on **Ubuntu 24.04**.

This project automatically installs **XAMPP 8.2.12**, prepares an Apache/PHP development environment, installs Linuxbrew (Homebrew for Linux), and provides a simple workflow for launching the container under WSL.

---

# Features

- Ubuntu 24.04 base image
- XAMPP 8.2.12 unattended installation
- Apache Web Server
- PHP runtime
- PHP CLI
- PHP Extensions
  - php-curl
  - php-xml
  - php-mysql
  - php-mbstring
  - php-zip
- Git
- Curl
- Wget
- Vim
- Build tools
- Linuxbrew (Homebrew)
- Docker Compose support
- Automatic volume mounting
- Automatic container startup
- Windows launcher
- Interactive shell
- PHP information test page

---

# Software Stack

| Software | Version |
|-----------|----------|
| Ubuntu | 24.04 |
| Docker | Latest |
| Docker Compose | v2 |
| XAMPP | 8.2.12 |
| Apache | Included in XAMPP |
| PHP | Included in XAMPP |
| Linuxbrew | Latest |

---

# Directory Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── startup.cmd
├── manual.txt
└──  src/
     └── index.php
```

---

# Requirements

- Windows 10 / Windows 11
- WSL2
- Ubuntu
- Docker
- Docker Compose

---

# First-Time Setup

Install WSL

```powershell
wsl --install
```

Enter Ubuntu

```bash
wsl -d Ubuntu
```

Update packages

```bash
sudo apt update
```

Install Docker

```bash
sudo apt install docker.io docker-compose-v2 podman-docker -y
```

Start Docker

```bash
sudo service docker start
```

Return to Windows.

---

# Build

```bash
docker compose build
```

---

# Run

```bash
docker compose up -d
```

---

# Stop

```bash
docker compose down
```

---

# Container

The container is named

```
xampp
```

Open a shell

```bash
docker exec -it xampp bash
```

---

# Installed Packages

The Docker image installs the following development packages.

- sudo
- wget
- curl
- build-essential
- net-tools
- apache2
- php
- php-cli
- php-curl
- php-xml
- php-mysql
- php-mbstring
- php-zip
- git
- unzip
- vim
- procps
- file
- libx11-6
- libxext6
- libxrender1
- libxtst6
- libgtk2.0-0
- libcanberra-gtk-module

---

# Linuxbrew

Linuxbrew is installed automatically.

PATH

```
/home/linuxbrew/.linuxbrew/bin
/home/linuxbrew/.linuxbrew/sbin
```

---

# XAMPP Installation

The installer runs automatically.

```
--mode unattended
```

No manual installation is required after the Docker image is built.

---

# Volume Mapping

```
./src
      │
      ▼
/opt/lampp/htdocs
```

Any files placed in `src/` are immediately available through Apache inside the container.

---

# Port Mapping

Host

```
80
```

↓

Container

```
80
```

---

# Startup Process

Container startup performs the following actions.

1. Start XAMPP
2. Display network information
3. Keep the container alive

```
lampp start
ifconfig
tail -f /dev/null
```

---

# Windows Launcher

`startup.cmd` automates the development workflow.

It performs the following tasks.

- Launch WSL
- Build Docker image
- Start Docker Compose
- Detect container IP
- Open browser automatically
- Enter interactive shell

---

# Test Page

The default application contains

```php
<?php
phpinfo();
?>
```

This confirms that PHP is working correctly.

---

# Access

If port forwarding is available

```
http://localhost
```

or

```
http://CONTAINER_IP
```

---

# Development Workflow

```
Edit source

↓

Save

↓

Docker Volume

↓

Apache

↓

Browser
```

No rebuild is required for normal PHP file changes.

---

# Example

```
src/

    index.php

↓

Docker Volume

↓

/opt/lampp/htdocs

↓

Apache

↓

Browser
```

---

# Customization

You may freely add

- PHP projects
- Laravel
- WordPress
- Composer
- Node.js
- MySQL clients
- Additional PHP extensions

by extending the Dockerfile.

---

# Troubleshooting

## Docker is not running

```bash
sudo service docker start
```

---

## Container is stopped

```bash
docker ps -a
```

Restart

```bash
docker start xampp
```

---

## View logs

```bash
docker logs xampp
```

---

## Enter container

```bash
docker exec -it xampp bash
```

---

# Future Improvements

Possible enhancements include

- MySQL container
- phpMyAdmin
- Composer
- Node.js
- npm
- HTTPS
- SSL certificates
- Redis
- MailHog
- Xdebug
- VS Code Dev Containers

---

# License

MIT License

---

# Author

Hirotoshi Uchida

GitHub

https://github.com/Uchida16104

---

# Acknowledgements

- Ubuntu
- Docker
- Apache
- PHP
- XAMPP
- Linuxbrew
