import jwt
from datetime import datetime
from pprint import pprint as pp

secret = "abcdef"
algo = "HS256"
payload = {
	'some': 'payload', 
	'iss': 'dinesh inc.',
	'exp': datetime.timestamp(datetime.now())
}

encoded = jwt.encode(payload, secret)
# time.sleep(1)
decoded = jwt.decode(encoded, secret)
print(str(encoded))
pp(decoded)