import sys
import pyotp
import configparser
import os

def read_config():
    config = configparser.ConfigParser()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')
    config.read(config_path)
    return config

config = read_config()
secret = config['auth']['secret']

totp = pyotp.TOTP(secret)
otp = totp.now()

OUTPUT_FILE = sys.argv[1]
with open(OUTPUT_FILE, 'w') as f:
    f.write(otp)
    f.flush()

#print(otp)