#!/bin/bash

# Install Java
apt-get update
apt-get install -y default-jre curl

# Download the latest signal-cli JAR
curl -L https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-cli-0.11.12.1.jar -o signal-cli.jar

echo "signal-cli JAR downloaded."#!/bin/bash

apt-get update
apt-get install -y default-jre wget curl unzip

echo "Downloading signal-cli..."
curl -L https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-x86_64.tar.gz -o signal-cli.tar.gz

echo "Extracting..."
tar -xzf signal-cli.tar.gz

mv signal-cli-* signal-cli
chmod +x signal-cli/bin/signal-cli

echo "Installation finished."
