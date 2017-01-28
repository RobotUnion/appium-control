#!/usr/bin/env python

import os, sys
sys.path.append(os.path.realpath(os.getcwd() + '/lib'))

import adb
import json

sys.stderr.write( json.dumps({'devices': adb.devices()}))

print "Content-type: application/json"
print
print json.dumps({'devices': adb.devices()})

