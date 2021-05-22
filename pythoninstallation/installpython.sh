#!/bin/bash
source ./logger.sh
python_installer() {
  sudo su - <<EOF
  wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tgz --directory-prefix=/usr/local/bin/ && cd /usr/local/bin/
  tar -xvzf Python-3.7.10.tgz && cd Python-3.7.10
  ./configure --enable-optimizations
  make altinstall
  pip 3.7 install --upgrade pip
EOF
}

python_installer
