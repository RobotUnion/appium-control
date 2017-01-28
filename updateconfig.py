#!/usr/bin/env python

import json

config = json.load(open('nodeconfig.json.dist'))
print json.dumps(config)
