#!/bin/sh
pip2 install -U -t lib -r requirements.txt

python3 -c "import os;import binascii;print('SECRET_KEY = ' + repr(binascii.hexlify(os.urandom(24))))" > gwax_flask/secrets.py
