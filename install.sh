#!/bin/bash

apt-get update
apt-get install -y openjdk-21-jre wget unzip

wget https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-x86_64.tar.gz
tar xf signal-cli-x86_64.tar.gz
mv signal-cli-* signal-cli
