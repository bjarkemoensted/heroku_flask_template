#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to automatically deploy to heroku. You can do
python deploy "commit message"

Created on Thu Nov 15 19:31:10 2018

@author: ahura
"""

import make_requirements
from subprocess import call
import sys
import string
import random

def rand():
    alf = string.ascii_uppercase + string.ascii_lowercase + string.digits
    s = ''.join(random.choice(alf) for _ in range(16))
    with open("deleteme.txt", "w") as f:
        f.write(s)

def deploy(msg):
    make_requirements.go()
    print("Deploying...")
    call("git add .".split())
    call(["git", "commit", "-m", '"%s"'%msg])
    call(["git", "push"])
    print("Deployed "+msg)

if __name__ == '__main__':
    msg = "Deploying yet again."
    if len(sys.argv) > 1:
        msg = sys.argv[1]

    deploy(msg)