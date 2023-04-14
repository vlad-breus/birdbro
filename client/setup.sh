#!/bin/bash

# Update the system
sudo apt-get update && sudo apt-get upgrade -y

# Install Python and required packages
sudo apt-get install -y python3 python3-pip
pip3 install -r requirements.txt

# Install additional packages if necessary (e.g., for audio input)
# sudo apt-get install -y <package_name>

echo "Setup completed. Run the client using 'python3 main.py'"
