#!/bin/bash
pkg update && pkg upgrade -y
pkg install git python python-pip -y
git clone https://github.com/DragonSCP/dragonscriptproxy.git
cd dragonscriptproxy
pip install -r requirements.txt
python dragon_ssh_script.py
