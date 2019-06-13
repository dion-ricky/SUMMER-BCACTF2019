#!/usr/bin/env python3
import os

print(os.popen("dig TXT hole.sketchy.dev | grep bcactf").read())
