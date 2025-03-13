import pyotp
import sys

OUTPUT_FILE = sys.argv[1]

# 二段階認証のシークレットキー
secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

totp = pyotp.TOTP(secret)
otp = totp.now()

with open(OUTPUT_FILE, 'w') as f:
    f.write(otp)
    f.flush()

print(otp)