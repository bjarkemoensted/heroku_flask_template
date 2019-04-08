#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:29:16 2018

@author: ahura
"""

from glob import glob
import os
import string
import sys
from subprocess import Popen
import random

# Go to where this script is
_here = os.path.dirname(os.path.realpath(__file__))
os.chdir(_here)

# General requirements (not speficied in any python file)
general = set(["tensorflow"])

def make_temp_filename():
    alf = string.ascii_uppercase + string.ascii_lowercase + string.digits
    fn = None
    old = set(glob("*.txt"))
    print(old)

    while fn is None or fn in old:
        fn = ''.join(random.choice(alf) for _ in range(16))+'.txt'
    return fn

def readreqs(filename):
    with open(filename) as f:
        oldreqs = set(line.strip() for line in f)
    return oldreqs

def go():
    # Read in old requirements
    try:
        oldreqs = readreqs("requirements.txt")
        #
    except FileNotFoundError:
        oldreqs = set([])

    # Generate temp file with new requirements
    tmpfile = make_temp_filename()
    tmppath = os.path.join(_here, tmpfile)

    try:
        print("Writing new reqs to %s." % tmpfile)
        p = Popen(['pipreqs', '--savepath', tmppath, "."])
        p.wait()
        print("Status", p)
        newreqs = readreqs(tmpfile)
        newreqs.update(general)
        os.remove(tmppath)
    except Exception as e:
        print("Error, removing temp file")
        os.remove(tmppath)
        raise

    # If any changes have occurred, update req file
    if newreqs == oldreqs:
        print("No change in requirements. Nothing to do.")
    else:
        print("updating requirements file...")
        with open('requirements.txt', 'w') as f:
            f.write("\n".join(sorted(newreqs)))
        #
    print("Done!")

if __name__ == '__main__':
    go()