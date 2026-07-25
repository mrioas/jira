#!/usr/bin/sh --debug
set -e

if [[ -d "./ware/" ]]; then
  rm -rf ./ware/
  rm -rf bin/
fi
# Activating VE from source bash,zsh,fis bash,zsh,fish

if [[ $SHELL == "/usr/bin/zsh" || $SHELL == "/usr/bin/bash" ]]; then
  echo "Creating the Enviroment Virtual"
  python -m venv ware
  echo "Activating the Enviroment Virtual"
  source ware/bin/activate
elif [[ $SHELL == "/usr/bin/fish" ]]; then
  source ware/bin/activate.fish
fi
#if []:
#  source ware/bin/activate
