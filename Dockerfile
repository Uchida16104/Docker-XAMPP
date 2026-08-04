FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sudo \
    wget \
    curl \
    build-essential \
    net-tools \
    apache2 \
    php \
    php-cli \
    php-curl \
    php-xml \
    php-mysql \
    php-mbstring \
    php-zip \
    git \
    unzip \
    vim \
    procps \
    file \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libgtk2.0-0 \
    libcanberra-gtk-module \
 && rm -rf /var/lib/apt/lists/*

###################################################
# Linuxbrew
###################################################

RUN useradd -m -s /bin/bash linuxbrew && \
    echo "linuxbrew ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER linuxbrew
WORKDIR /home/linuxbrew

RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

ENV PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:${PATH}"

USER root

###################################################
# XAMPP
###################################################

COPY xampp-linux-x64-8.2.12-0-installer.run /tmp/

RUN chmod +x /tmp/xampp-linux-x64-8.2.12-0-installer.run

RUN /tmp/xampp-linux-x64-8.2.12-0-installer.run \
    --mode unattended

COPY src /opt/lampp/htdocs

EXPOSE 80

CMD ["/bin/bash","-c","/opt/lampp/lampp start && ifconfig && tail -f /dev/null"]
