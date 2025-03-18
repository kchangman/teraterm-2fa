import sys
import pyotp

secret = sys.argv[2]

totp = pyotp.TOTP(secret)
otp = totp.now()

OUTPUT_FILE = sys.argv[1]
with open(OUTPUT_FILE, 'w') as f:
    f.write(otp)
    f.flush()

#print(otp)