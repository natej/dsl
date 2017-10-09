#!/usr/bin/env python3
from __future__ import print_function

# dsl2.py

import sys
import importlib

def get_args(dsl_args):
    """return args, kwargs"""
    args = []
    kwargs = {}
    for dsl_arg in dsl_args:
        if '=' in dsl_arg:
            k, v = dsl_arg.split('=', 1)
            kwargs[k] = v
        else:
            args.append(dsl_arg)
    return args, kwargs

# the source file is the 1st argument to the script
if len(sys.argv) != 2:
    print('usage: %s <src.dsl>' % sys.argv[0])
    sys.exit(1)

sys.path.insert(0, '/Users/nathan/code/dsl/modules')

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        mod = importlib.import_module(parts[0])
        args, kwargs = get_args(parts[2:])
        getattr(mod, parts[1])(*args, **kwargs)
