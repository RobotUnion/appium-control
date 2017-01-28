#!/usr/bin/env python

import os
import json

def devices():
    adb= '/opt/android-sdk-linux/platform-tools/adb'
    command = adb + ' devices';
    device_ids = [devLine.split()[0] for devLine in os.popen(command).readlines()[1:-1]]
    devices = [{'id': devId, 'name': os.popen(adb + ' -s ' + devId + ' shell getprop ro.product.model').read().strip()} for devId in device_ids]
    return devices
 
#response = {'devices': devices}

