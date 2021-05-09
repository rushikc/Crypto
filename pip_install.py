package_list = [
    'selenium',
    'bs4',
    'twilio',
    'wappdriver',
    'pyrebase',
    'python-firebase'
]

import os

for k in package_list:
    os.system("pip3 install " + k)
