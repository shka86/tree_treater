#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pathlib

files = list(pathlib.Path.cwd().glob('**/*'))

tree = ""

for file in files:
    tree += str(file) + "\n"

print(tree)

with open("tree.txt", 'w') as f:
    f.write(tree)
