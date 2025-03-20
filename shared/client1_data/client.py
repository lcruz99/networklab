#!/usr/bin/env python3

import requests
import os


os.environ["SSLKEYLOGFILE"] = "sslkeys.log"

url = "https://172.20.0.3:4443"
try:
    response = requests.get(url, cert=("certs/public.crt", "certs/private.key"), verify=False)
    print("Response:", response.text)
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)
