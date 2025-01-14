#!/usr/bin/python3
import sys

# Vérifie si des arguments sont fournis
if len(sys.argv) == 1:
    print("Usage: ./script.py <arguments>")
    sys.exit(1)

# Affiche chaque argument
for arg in sys.argv[1:]:
    print(arg)
