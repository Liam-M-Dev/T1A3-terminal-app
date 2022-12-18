#!/bin/bash
if [[ -x "$(command -v python)" ]]
then 
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3.10.8" ]]
    then
        echo "Python 3.10 is the version you have, we can setup the rest now"
    else
        echo "This is the incorrect version of python, but you do have it installed
        we can set up the correct version in the venv" >&2
        exit 1
    fi
else
    echo "Error:
    There's no python installed, please go to https://installpython3.com/
    and install python to continue" >&2
    exit 1
fi


if [[ -x "$(command -v pip)" ]]
then
    pipv="$(pip -V)"
    if [[ $pipv == "pip 22"* ]]
    then
        echo "you have pip installed and the correct version"
    else
        echo "the version you have is out of date, just need to upgrade this"
        pip install --upgrade pip
        exit 1
    fi
else
    echo "Error:
    Pip isn't installed, please follow the instructions from 
    https://pip.pypa.io/en/stable/installation/ to install" >&2
    exit 1
fi
