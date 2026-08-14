import os, sys
sys.path.insert(0, 'C:/Users/e031093/dev/vima')
os.chdir('C:/Users/e031093/dev/vima')
from dotenv import load_dotenv
load_dotenv('config/.env', override=True)

consumer_key = os.environ.get('BIN_LOOKUP_CONSUMER_KEY', '')
key_path = os.environ.get('BIN_LOOKUP_SIGNING_KEY_PATH', '')
key_password = os.environ.get('BIN_LOOKUP_SIGNING_KEY_PASSWORD', 'foobar!!')

print('consumer_key (first 40):', consumer_key[:40])
print('key_path:', key_path)
full_path = key_path if os.path.isabs(key_path) else os.path.join('C:/Users/e031093/dev/vima', key_path)
print('full_path:', full_path)
print('file exists:', os.path.exists(full_path))

import oauth1.authenticationutils as au
from oauth1.oauth import OAuth
import json, requests

try:
    signing_key = au.load_signing_key(full_path, key_password)
    print('Key loaded OK')
    url = 'https://sandbox.api.mastercard.com/bin-resources/bin-ranges?page=1&size=10'
    body = json.dumps([{"key": "binNum", "value": "543210"}])
    auth_header = OAuth.get_authorization_header(url, 'POST', body, consumer_key, signing_key)
    print('Authorization header (first 80):', auth_header[:80])
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': auth_header,
    }
    resp = requests.post(url, data=body, headers=headers, timeout=15)
    print('Status:', resp.status_code)
    print('Response:', resp.text[:500])
except Exception as e:
    print('ERROR:', e)
