import requests
import time

URL = "http://127.0.0.1:5000/verify-otp"

def test_otp(otp):
    start = time.time()
    r = requests.post(URL, json={"otp": otp})
    end = time.time()
    return r.status_code, end - start

for otp in ["000000", "123456"]:
    status, t = test_otp(otp)
    print(f"OTP={otp} | Status={status} | Time={t:.6f}")
