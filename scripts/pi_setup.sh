#/bin/sh

# general update
sudo apt update
sudo apt upgrade

# zsh + ohmyzsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

