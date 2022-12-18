#!/bin/bash
if command -v python3 &> /dev/null
then
  python3 main.py
elif command -v python &> /dev/null
then
  python main.py
else
  echo "Error:
    Something has gone wrong, please ensure that the previous scripts have installed
    python3, pip and venv correctly. For manual guides, check the help documentation" >&2
  exit 1
fi