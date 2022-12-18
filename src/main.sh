#!/bin/bash
if command -v python3 &> /dev/null
then
  python3 main.py
fi

if command -v python &> /dev/null
then
  python main.py
fi