#!/usr/bin/env python3
import os

print(os.popen("cat input.txt | python3 script.py").read())
