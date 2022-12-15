#!/bin/bash

if [[ -x "$(command -v pyenv)" ]]
then
    echo "pyenv is installed the rest of the 
    script will set up the environement"
else
    echo "we need to install pyenv, please follow this guide 
    https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu"
fi

$ pyenv local Python 3.10.8

$ python -m venv .venv

$ source .venv/bin/activate

$ pip3 install -r requirements.txt